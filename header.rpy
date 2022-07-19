init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="MAS Otter's brbs",
        description="New "Be right back" options.",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Otter's brbs",
            user_name="my-otter-self",
            repository_name=otter_MAS_brbs",
            submod_dir="/Submods/Otter's brb's",
            extraction_depth=3,
            redirected_files=(
                "README.md",
            )
        )