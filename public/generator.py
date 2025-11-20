def generate_svg(diameter_mm, vertical_lines, horizontal_lines, margin):
    r = diameter_mm / 2
    inner_r = r - margin  # grid must stay inside this smaller radius

    svg = [
        f'<svg width="{diameter_mm}mm" height="{diameter_mm}mm" '
        f'viewBox="{-(r)} {-(r)} {diameter_mm} {diameter_mm}" '
        f'xmlns="http://www.w3.org/2000/svg">',
        f'<circle cx="0" cy="0" r="{r}" fill="none" stroke="black" stroke-width="0.1"/>'
    ]

    # Vertical lines
    if vertical_lines > 1:
        dx = 2 * inner_r / (vertical_lines - 1)
        for i in range(vertical_lines):
            x = -inner_r + i * dx
            svg.append(
                f'<line x1="{x}" y1="{-inner_r}" x2="{x}" y2="{inner_r}" '
                f'stroke="black" stroke-width="0.1" />'
            )

    # Horizontal lines
    if horizontal_lines > 1:
        dy = 2 * inner_r / (horizontal_lines - 1)
        for i in range(horizontal_lines):
            y = -inner_r + i * dy
            svg.append(
                f'<line x1="{-inner_r}" y1="{y}" x2="{inner_r}" y2="{y}" '
                f'stroke="black" stroke-width="0.1" />'
            )

    svg.append('</svg>')
    return "\n".join(svg)
