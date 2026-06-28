import re
import sys

from vsest_common import field, is_empty, issue_state, issue_type, list_issues, load_config


def error(number, message):
    return f"Issue #{number}: {message}"


def evaluation_score(value):
    match = re.match(r"^\s*([012])(?:\s|$|-)", value or "")
    return match.group(1) if match else None


def validate(issues, config):
    errors = []
    codes = {}
    structured = 0
    valid_states = set(config["states"])
    valid_phases = set(config["phases"])
    rules = config["rules"]

    for issue in issues:
        type_name = issue_type(issue, config)
        if not type_name:
            continue

        structured += 1
        number = issue.get("number")
        body = issue.get("body") or ""
        type_config = config["issue_types"][type_name]

        for required in type_config["required_fields"]:
            if is_empty(field(body, required)):
                errors.append(error(number, f"falta el campo obligatorio {required}"))

        code = field(body, "Codigo")
        if not is_empty(code):
            normalized_code = code.casefold()
            if normalized_code in codes:
                errors.append(
                    error(
                        number,
                        f"Codigo duplicado {code} (tambien usado en issue #{codes[normalized_code]})",
                    )
                )
            else:
                codes[normalized_code] = number

        raw_state = field(body, "Estado")
        if raw_state and raw_state not in valid_states:
            errors.append(error(number, f"Estado invalido: {raw_state}"))

        phase = field(body, "Fase")
        if phase and phase not in valid_phases:
            errors.append(error(number, f"Fase invalida: {phase}"))

        if type_name == "riesgo":
            priority = field(body, "Prioridad")
            if priority and priority not in rules["risk_priorities"]:
                errors.append(error(number, f"Prioridad de riesgo invalida: {priority}"))

        if type_name == "evaluacion":
            result = field(body, "Resultado")
            if result and evaluation_score(result) not in set(rules["evaluation_results"]):
                errors.append(
                    error(number, f"Resultado invalido: {result}; debe comenzar por 0, 1 o 2")
                )

        if type_name == "zap" and issue_state(issue, config) == rules["zap_not_executable_state"]:
            has_cause = any(
                not is_empty(field(body, cause_field))
                for cause_field in rules["zap_cause_fields"]
            )
            if not has_cause:
                errors.append(
                    error(
                        number,
                        "ZAP No ejecutable sin causa en "
                        + " u ".join(rules["zap_cause_fields"]),
                    )
                )

        if type_name == "artefacto" and issue_state(issue, config) == "Cerrado":
            evidence = field(body, "Evidencia")
            placeholders = {value.casefold() for value in rules["evidence_placeholders"]}
            if is_empty(evidence) or evidence.casefold() in placeholders:
                errors.append(error(number, "artefacto Cerrado sin evidencia verificable"))

    return errors, structured


def main():
    try:
        config = load_config()
        errors, structured = validate(list_issues(config), config)
    except Exception as exc:
        print(f"Error de ejecucion: {exc}", file=sys.stderr)
        return 2

    if errors:
        print("\n".join(errors))
        print(f"\nValidacion fallida: {len(errors)} error(es) en {structured} issue(s) estructurado(s)")
        return 1

    print(f"Validacion completada: {structured} issue(s) estructurado(s), 0 errores")
    return 0


if __name__ == "__main__":
    sys.exit(main())
