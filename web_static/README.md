# Web Static

## Tasks

### 0. Inline styling
Write an HTML page that displays a header and a footer.

### 1. Head styling
Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as `0-index.html`)

### 2. CSS files
Write an HTML page that displays a header and a footer by using CSS files (same as `1-index.html`)
- You must have 3 CSS files:
    - `styles/2-common.css`: for global style (i.e. the body style)
    - `styles/2-header.css`: for header style
    - `styles/2-footer.css`: for footer style

### 3. Zoning done!
Write an HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

### 4. Search!
Write an HTML page that displays a header, footer and a filters box with a search button.
- Container:
    - between `header` and `footer` tags, add a `div`:
        - classname: `container`
- Filter section:
    - tag `section`
    - classname `filters`
    - inside the `.container`
- Button search:
    - tag `button`
    - text `Search`



### 5. More filters
Write an HTML page that displays a header, footer and a filters box.
- Locations and Amenities filters:
    - tag: `div`
    - classname: `locations` for location tag and `amenities` for the other
    - inside the section filters (same level as the `button` Search)


### 6. It's (h)over
Write an HTML page that displays a header, footer and a filters box with dropdown.
- Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
    - tag `ul`
    - classname `popover`

### 7. Display results
Write an HTML page that displays a header, footer, a filters box with dropdown and results.
- Add Places section:
    - tag: `section`
    - classname: `places`
    - same level as the filters section, inside `.container`

### 8. More details
Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.
Add more information to a `Place` article:
- Price by night:
    - tag: `div`
    - classname: `price_by_night`
- Information section:
    - tag: `div`
    - classname: `information`