def generate_svg(diameter_mm, vertical_lines, horizontal_lines, margin):
    r = diameter_mm / 2
    usable = r - margin
    svg = [
        f'<svg width="{diameter_mm}mm" height="{diameter_mm}mm" viewBox="{-(r)} {-(r)} {diameter_mm} {diameter_mm}" xmlns="http://www.w3.org/2000/svg">',
        f'<circle cx="0" cy="0" r="{r}" fill="none" stroke="black" stroke-width="0.1"/>'
    ]

    # Vertical lines
    if vertical_lines > 1:
        dx = 2 * usable / (vertical_lines - 1)
        for i in range(vertical_lines):
            x = -usable + i * dx
            svg.append(f'<line x1="{x}" y1="{-usable}" x2="{x}" y2="{usable}" stroke="black" stroke-width="0.1" />')

    # Horizontal lines
    if horizontal_lines > 1:
        dy = 2 * usable / (horizontal_lines - 1)
        for i in range(horizontal_lines):
            y = -usable + i * dy
            svg.append(f'<line x1="{-usable}" y1="{y}" x2="{usable}" y2="{y}" stroke="black" stroke-width="0.1" />')

    svg.append('</svg>')
    return "\n".join(svg)
