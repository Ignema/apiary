# Apiary DSL Syntax Highlighting

Provides syntax highlighting for Apiary REST API DSL files (`.api` extension).

## Features

- Syntax highlighting for keywords (`api`, `model`, `endpoint`, etc.)
- HTTP method highlighting (GET, POST, PUT, PATCH, DELETE)
- Type highlighting (str, int, float, bool, datetime)
- String and comment highlighting
- Auto-closing brackets and quotes
- Code folding support

## Installation

This extension is bundled with the Apiary project. To use it:

1. Open VS Code
2. Go to Extensions view (Ctrl+Shift+X)
3. Click "..." menu → "Install from VSIX..."
4. Navigate to `.vscode/extensions/apiary-dsl` and select it

Or simply open any `.api` file in this workspace and VS Code should automatically recognize it.

## Example

```apiary
// Pet Store API
api "PetStore" version "1.0.0" at "/api/v1" using sqlite

model Pet table "pets" {
    name: str required indexed
    age: int required default 0
    weight: float
    vaccinated: bool default false
}

endpoint GET "/pets" -> Pet[] description "Get all pets"
endpoint POST "/pets" -> Pet description "Create a new pet"
```

## Supported Syntax

- **Keywords**: `api`, `model`, `endpoint`, `table`, `version`, `at`, `using`, `description`
- **HTTP Methods**: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- **Types**: `str`, `int`, `float`, `bool`, `datetime`
- **Modifiers**: `required`, `unique`, `indexed`, `default`
- **Databases**: `sqlite`, `postgres`
- **Comments**: `// line comments`
