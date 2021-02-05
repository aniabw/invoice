class Utils:

    def add_form_control_class(self):
        # visible_with_class = []
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

