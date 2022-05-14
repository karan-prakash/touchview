![touch view header](/docs/header.jpg?raw=true)

# Features
---

Improve the Blender UI for keyboard-less users.

- viewport touch regions for camera control
- double-tap focus selection
- on-screen buttons for quick access to important features
- viewport rotation lock
- context-aware topology options
  - easily access retopology tools in sculpt mode
  - when multi-resolution modifier is active, quickly switch resolutions or subdivide/unsubdivide mesh
- customizable floating menu
  - assign up to 7 commands for each edit mode


![demo gif](/docs/demo.gif?raw=true)

# Planned Upgrades
---

- customizable double-tap action
- viewport camera toggle Gizmo for non-pen users
- scaleable Gizmos
- auto-retopology levels
- brush size/falloff UI

# Changelogs
---

<details open><summary><b>v1.1.0</b></summary><br>

- `ADDED` : Multi-resolution level limiter and gizmo status color

</details>

<details open><summary><b>v1.0.1</b></summary><br>

- `ADDED` : Optional include for MIDDLEMOUSE when disabling/enabling touch controls
- `FIXED` : Preferences bug preventing toggle of floating Gizmo

</details>

<details open><summary><b>v1.0.0</b></summary><br>

- `ADDED` : Toggle swap pan/rotate regions
- `ADDED` : Toggle floating menu button to N Panel
- `UPDATED` : Disabling touch controls no longer removes overlay (hot regions still work with custom keybinds and MIDDLEMOUSE)
- `UPDATED` : Disabling touch controls restores default LEFTMOUSE functionality

</details>

<details><summary><b>v0.9.6</b></summary><br>

- `ADDED` : undo/redo gizmo
- `ADDED` : overlay color selection
- `ADDED` : touch control toggle in settings
- `ADDED` : Alt+T to toggle touch controls
- `UPDATED` : N Panel now includes extra settings from addon menu
- `UPDATED` : Lock Rotation now addresses quadview data replication bug
- `UPDATED` : Limited floating gizmo to viewport area
- `UPDATED` : code cleanup and additional structure tweaks
- `REMOVED` : Gizmo Tooltips

</details>

<details><summary><b>v0.9.5</b></summary><br>

- `ADDED` : multires modifier support to gizmo bar (shows retopology tools when no modifier is present)
- `FIXED` : Gizmos now properly follow mode visibility rules
- `FIXED` : Double-tap selection now only runs in appropriate viewport modes

</details>

<details><summary><b>v0.9.4</b></summary><br>

- `ADDED` : Support for menus in floating gizmo
- `ADDED` : Mode-specific options for floating gizmo
- `UPDATED` : Dependence on active_object for mode detection
- `UPDATED` : Classes to follow Blender naming conventions
- `UPDATED` : Keymaps for touchview in all context
- `UPDATED` : Keymaps for context action assigned to pen

</details>

<details><summary><b>v0.9.3</b></summary><br>

- `ADDED` : Sculpt pivot mode gizmo
- `ADDED` : Customizable floating menu

</details>

<details><summary><b>v0.9.2</b></summary><br>

- `FIXED` : Issue delaying overlay viewport binding
- `FIXED` : Gizmo tools/panel overlap issue when "Region Overlap" enabled
- `REMOVED` : Viewport manager class
- `REMOVED` : Default keymap causing Move Operator to trigger when dragging over non-modal gizmos

</details>

<details><summary><b>v0.9.1</b></summary><br>

- `ADDED` : Tap for menu scroll

</details>

<details><summary><b>v0.9</b></summary><br>

- `ADDED` : N-Panel gizmo
- `UPDATED` : Code restructure
- `FIXED` : Dragging over gizmo moves selected object

</details>

<details><summary><b>v0.8</b></summary><br>

- `ADDED` : Gizmo to toggle fullscreen mode
- `UPDATED` : Settings to addon preferences to save across projects and scenes
- `FIXED` : Bugs impacting user experience
- `FIXED` : Doubletap now selects/activates tapped object instead of triggering fullscreen

</details>

<details><summary><b>v0.7</b></summary><br>

- `ADDED` : Gizmos for key features
- `ADDED` : Hide/show Gizmo and layout options
- `ADDED` : Locked viewport rotation for isometric viewports in quadview to address lock/unlock inconsistencies
- `FIXED` : Fullscreen Toggle no longer maximizes the window, only expands the View3D region

</details>

<details><summary><b>v0.6</b></summary><br>

- `UPDATED` : Scale of viewport overlay settings for more precision
- `FIXED` : Issues with determining locked state with quadviews

</details>

<details><summary><b>v0.5</b></summary><br>

- `ADDED` : Camera rotation lock in N-panel
- `FIXED` : Quad-view overlay compatibility
- `FIXED` : Rotation with panning when rotation is locked
- `FIXED` : Issue when locking view to Object or 3D Cursor

</details>

<details><summary><b>v0.4</b></summary><br>

- `ADDED` : Double-tap to toggle "focus" mode
- `ADDED` : Toggle Tools LEFT/RIGHT in UI

</details>

<details><summary><b>v0.3</b></summary><br>

- `FIXED` : Incorrect viewport calculation when N-panel is open
- `FIXED` : Refactored screen/area management code (additional major refactor needed)

</details>

<details><summary><b>v0.2</b></summary><br/>

- `FIXED` : Minor bug fixes and code cleanup

</details>

<details><summary><b>v0.1</b></summary><br>

- `ADDED` : Camera dolly on left and right of viewport
- `ADDED` : Camera pan from center of viewport
- `ADDED` : Camera rotate in any other area of viewport
- `ADDED` : Toggleable overlay to simplify resizing controls

</details>

# Issues

> Please [report any issues](https://github.com/nendotools/touchview/issues) you find and I'll do my best to address them.

> The add-on is free, but if it helps you, please consider [supporting me](https://nendo.gumroad.com/l/touchview).
