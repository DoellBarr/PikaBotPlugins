from pikabot import CMD_LIST
from pikabot.main_plugs.plug import *
from SysRuntime import *


@ItzSjDude(outgoing=True, pattern=r"help ?(.*)")
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "Do .help cmd")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a Plugin Nibba!😕")
        else:
            help_string = f"""Pïkå¢hµ Úsêrßð† {helpstr}"""
            results = await event.client.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()


@ItzSjDude(outgoing=True, pattern="syntax (.*)")
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in CMD_LIST:
        help_string = CMD_LIST[plugin_name]
        unload_string = (
            f"Use `.unload {plugin_name}` to remove this plugin.\n           © Pikabot"
        )
        if help_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n{help_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.plugins` or `.help` to get list of valid plugin names."
    await event.edit(plugin_syntax)
