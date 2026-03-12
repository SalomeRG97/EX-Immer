import os
import glob

# Search in the given directory and all its subdirectories for HTML files
path = r'c:\Users\salom\Documents\EBEDIX\REAL ESTATE\PAGINA WEB\DESARROLLO\ex-view-real-estate\**\*.html'
html_files = glob.glob(path, recursive=True)

old_footer_span_3 = """                <div style="grid-column: span 3; grid-column-start: 6;">
                    <h4 class="mb-sm">Legal & Privacidad</h4>
                    <ul style="display: flex; flex-direction: column; gap: 8px;">
                        <li><a href="privacy-policy.html">Términos de servicio y políticas de privacidad</a></li>
                        <li><a href="legal-terms.html">Términos y servicios legales</a></li>
                    </ul>
                </div>

                <div style="grid-column: span 3; grid-column-start: 10;">
                    <h4 class="mb-sm">Síguenos</h4>"""

new_footer_english = """                <div style="grid-column: span 5; grid-column-start: 6;">
                    <h4 class="mb-sm">Legal & Privacy</h4>
                    <ul style="display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem;">
                        <li><a href="privacy-policy.html">Terms of Service & Privacy Policy</a></li>
                        <li><a href="legal-terms.html">Legal Terms & Services</a></li>
                    </ul>
                </div>

                <div style="grid-column: span 1; grid-column-start: 12;">
                    <h4 class="mb-sm">Follow Us</h4>"""

old_footer_span_5 = """                <div style="grid-column: span 5; grid-column-start: 6;">
                    <h4 class="mb-sm">Legal & Privacidad</h4>
                    <ul style="display: flex; flex-direction: column; gap: 8px;">
                        <li><a href="privacy-policy.html">Términos de servicio y políticas de privacidad</a></li>
                        <li><a href="legal-terms.html">Términos y servicios legales</a></li>
                    </ul>
                </div>

                <div style="grid-column: span 2; grid-column-start: 11;">
                    <h4 class="mb-sm">Síguenos</h4>"""

old_footer_span_3_nested = """                <div style="grid-column: span 3; grid-column-start: 6;">
                    <h4 class="mb-sm">Legal & Privacidad</h4>
                    <ul style="display: flex; flex-direction: column; gap: 8px;">
                        <li><a href="../privacy-policy.html">Términos de servicio y políticas de privacidad</a></li>
                        <li><a href="../legal-terms.html">Términos y servicios legales</a></li>
                    </ul>
                </div>

                <div style="grid-column: span 3; grid-column-start: 10;">
                    <h4 class="mb-sm">Síguenos</h4>"""

new_footer_english_nested = """                <div style="grid-column: span 5; grid-column-start: 6;">
                    <h4 class="mb-sm">Legal & Privacy</h4>
                    <ul style="display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem;">
                        <li><a href="../privacy-policy.html">Terms of Service & Privacy Policy</a></li>
                        <li><a href="../legal-terms.html">Legal Terms & Services</a></li>
                    </ul>
                </div>

                <div style="grid-column: span 1; grid-column-start: 12;">
                    <h4 class="mb-sm">Follow Us</h4>"""


for f_path in html_files:
    try:
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        
        # Patch spans in root files
        if old_footer_span_3 in content:
            content = content.replace(old_footer_span_3, new_footer_english)
            updated = True
        
        if old_footer_span_5 in content:
            content = content.replace(old_footer_span_5, new_footer_english)
            updated = True
            
        # Patch spans in nested files
        if old_footer_span_3_nested in content:
            content = content.replace(old_footer_span_3_nested, new_footer_english_nested)
            updated = True

        if updated:
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated footer in {os.path.basename(f_path)}")
            
    except Exception as e:
        print(f"Error processing {f_path}: {e}")

print("Done")
