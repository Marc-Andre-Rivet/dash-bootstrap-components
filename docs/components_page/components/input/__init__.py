from pathlib import Path

import dash_core_components as dcc
import dash_html_components as html

from ...api_doc import ApiDoc
from ...helpers import (
    ExampleContainer,
    HighlightedSource,
    load_source_with_environment,
)
from ...metadata import get_component_metadata
from .radio_check_inline import inline_inputs
from .selected_styles import checklist as input_selected_styles
from .size import inputs as input_size
from .text_label import text_input as input_text_label
from .textarea import textareas as input_textarea
from .validation import inputs as input_validation

HERE = Path(__file__).parent

input_simple_source = (HERE / "simple.py").read_text()
input_text_label_source = (HERE / "text_label.py").read_text()
input_size_source = (HERE / "size.py").read_text()
input_validation_source = (HERE / "validation.py").read_text()
input_radio_check_source = (HERE / "radio_check.py").read_text()
input_textarea_source = (HERE / "textarea.py").read_text()
input_radio_check_inline_source = (HERE / "radio_check_inline.py").read_text()
input_selected_styles_source = (HERE / "selected_styles.py").read_text()
input_radio_check_standalone_source = (
    HERE / "radio_check_standalone.py"
).read_text()


def get_content(app):
    return [
        html.H2("Input components", className="display-4"),
        html.P(
            dcc.Markdown(
                "Documentation and examples for input components in "
                "_dash-bootstrap-components_."
            ),
            className="lead",
        ),
        html.P(
            dcc.Markdown(
                "*dash-bootstrap-components* has its own versions of some of "
                "the input components available in *dash-core-components*. "
                "They have been designed to share the same interface as the "
                "corresponding components in *dash-core-components* for "
                "familiarity, but have a few additional Bootstrap specific "
                "features."
            )
        ),
        html.H4("Input"),
        html.P(
            dcc.Markdown(
                "The input component allows for text or numeric input, its "
                "basic usage is the same as `dcc.Input`, but Bootstrap styles "
                "will be applied for you."
            )
        ),
        ExampleContainer(
            load_source_with_environment(
                input_simple_source, "text_input", {"app": app}
            )
        ),
        HighlightedSource(input_simple_source),
        html.H4("Labels and Text"),
        html.P(
            dcc.Markdown(
                "Use the `FormGroup` component along with `Label` and "
                "`FormText` to control the layout of your `Input` components. "
                "See the [documentation for forms](/l/components/form) for "
                "more details."
            )
        ),
        ExampleContainer(input_text_label),
        HighlightedSource(input_text_label_source),
        html.H4("Input size"),
        html.P(
            dcc.Markdown(
                "You can control the size of the `Input` using the `bs_size` "
                "keyword argument. It accepts the values `sm`, `md` or `lg` "
                "for small, medium or large sizes respectively."
            )
        ),
        ExampleContainer(input_size),
        HighlightedSource(input_size_source),
        html.H4("Input validation"),
        html.P(
            dcc.Markdown(
                "Add valid / invalid styles to your `Input` components using "
                "the `valid` and `invalid` keyword arguments."
            )
        ),
        ExampleContainer(input_validation),
        HighlightedSource(input_validation_source),
        html.H4("Textarea"),
        html.P(
            dcc.Markdown(
                "The `Textarea` component works like the "
                "*dash-core-components* analogue, but accepts the additional "
                "arguments `valid`, `invalid`, and `bs_size` much like "
                "`Input`."
            )
        ),
        ExampleContainer(input_textarea),
        HighlightedSource(input_textarea_source),
        html.H4("RadioItems and Checklist"),
        html.P(
            dcc.Markdown(
                "`RadioItems` and `Checklist` components also work like "
                "*dash-core-components*. Provided you specify an `id`, "
                "_dash-bootstrap-components_ will render custom themed radio "
                "buttons or checkboxes rather than using the native browser "
                "buttons. When using `Checklist` you can also specify "
                "`switch=True` to render toggle-like switches rather than "
                "checkboxes. If you prefer to use the native buttons and "
                "checkboxes, set `custom=False`. Note that there is no native "
                "browser switch, so if you set `custom=False` then `switch` "
                "will be ignored."
            )
        ),
        html.P(
            dcc.Markdown(
                "Use these components with `FormGroup` for automatic spacing "
                "and padding."
            )
        ),
        ExampleContainer(
            load_source_with_environment(
                input_radio_check_source, "inputs", {"app": app}
            )
        ),
        HighlightedSource(input_radio_check_source),
        html.P(
            dcc.Markdown(
                "Use the `inline` keyword to make the radioitems or "
                "checklists fit next to each other on a line."
            )
        ),
        ExampleContainer(inline_inputs),
        HighlightedSource(input_radio_check_inline_source),
        html.H4("Checked item styles"),
        html.P(
            dcc.Markdown(
                "Use the `labelCheckedStyle` and `labelCheckedClassName` "
                "arguments to apply different styles to the labels of checked "
                "items. When using custom inputs you can override the styles "
                "of the inputs using custom CSS. See the below example."
            )
        ),
        dcc.Markdown(
            """```css
#checklist-selected-style
  .custom-control-input:checked
  ~ .custom-control-label::before {
  background-color: #fa7268;
  border-color: #ea6258;
}

```
        """
        ),
        ExampleContainer(input_selected_styles),
        HighlightedSource(input_selected_styles_source),
        html.P(
            dcc.Markdown(
                "If you need more granular control over checkboxes and radio "
                "buttons, you can also create standalone components. Bind "
                "callbacks to the `checked` keyword to react to changes in "
                "the input state. To attach a label, create a FormGroup with "
                "`check=True` and use the label's `html_for` keyword to bind "
                "it to the checkbox."
            )
        ),
        ExampleContainer(
            load_source_with_environment(
                input_radio_check_standalone_source,
                "standalone_radio_check",
                {"app": app},
            )
        ),
        HighlightedSource(input_radio_check_standalone_source),
        ApiDoc(
            get_component_metadata("src/components/input/Input.js"),
            component_name="Input",
        ),
        ApiDoc(
            get_component_metadata("src/components/input/Textarea.js"),
            component_name="Textarea",
        ),
        ApiDoc(
            get_component_metadata("src/components/input/RadioItems.js"),
            component_name="RadioItems",
        ),
        ApiDoc(
            get_component_metadata("src/components/input/Checklist.js"),
            component_name="Checklist",
        ),
        ApiDoc(
            get_component_metadata("src/components/input/Checkbox.js"),
            component_name="Checkbox",
        ),
        ApiDoc(
            get_component_metadata("src/components/input/RadioButton.js"),
            component_name="RadioButton",
        ),
    ]
