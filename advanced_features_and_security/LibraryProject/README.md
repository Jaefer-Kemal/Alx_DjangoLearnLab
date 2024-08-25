# Permissions and Groups Setup

## Custom Permissions

- **Book Model:**
  - `can_view`: Allows viewing of books.
  - `can_create`: Allows creation of books.
  - `can_edit`: Allows editing of books.
  - `can_delete`: Allows deletion of books.

## Groups

- **Editors:**
  - `can_edit`
  - `can_create`
- **Viewers:**
  - `can_view`
- **Admins:**
  - `can_view`
  - `can_create`
  - `can_edit`
  - `can_delete`

## Views

- Use the `@permission_required` decorator to enforce permissions in views.
