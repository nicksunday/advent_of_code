# Advent of Code scaffolding
# Usage:
#   just new 2025 01 go
#   just new 2025 01 python
#   just new 2025 01           (defaults to go)

default_lang := "go"
templates := "templates"

# Create a new day with optional language (go or python)
new year day lang=default_lang:
    #!/usr/bin/env bash
    set -euo pipefail
    
    dir="{{year}}/day{{day}}"
    
    if [[ -d "$dir" ]]; then
        echo "Directory $dir already exists!"
        exit 1
    fi
    
    mkdir -p "$dir"
    touch "$dir/input.txt"
    touch "$dir/example.input.txt"
    
    case "{{lang}}" in
        go)
            cp "{{templates}}/main.go" "$dir/main.go"
            echo "Created $dir with Go boilerplate"
            ;;
        python|py)
            cp "{{templates}}/solution.py" "$dir/solution.py"
            echo "Created $dir with Python boilerplate"
            ;;
        *)
            echo "Unknown language: {{lang}}. Use 'go' or 'python'."
            exit 1
            ;;
    esac

# Run solution
# just run 2025 01           -> uses input.txt
# just run 2025 01 example   -> uses example.input.txt
# just run 2025 01 example1  -> uses example1.input.txt
run year day input="":
    #!/usr/bin/env bash
    set -euo pipefail
    dir="{{year}}/day{{day}}"
    cd "$dir"
    
    if [[ -f "main.go" ]]; then
        go run . {{input}}
    elif [[ -f "solution.py" ]]; then
        python solution.py {{input}}
    else
        echo "No main.go or solution.py found in $dir"
        exit 1
    fi