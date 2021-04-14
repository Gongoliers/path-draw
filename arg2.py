# TODO: Assign these
options = []
values = []
arguments = []

def argument_parse():
		# program_name = values.pop(0)

		for option in options:
			option_token = option.lstrip("-")
			index_of_option_token = option.find(option_token)

			matching_value_token = values.pop(0) if len(values) > 0 else ""

			if matching_value_token == "" and index_of_option_token == 1:
				matching_value_token = option_token[1:]
				option_token = option_token[0]

			if matching_value_token == "" and index_of_option_token == 2 and "=" in option_token:
				index_of_equal = option_token.find("=")
				matching_value_token = option_token[index_of_equal + 1:]
				option_token = option_token[0:index_of_equal]

			arguments[option_token] = matching_value_token
