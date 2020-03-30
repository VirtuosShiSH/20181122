import unreal
import re


referenced_assets = []
non_referenced_assets = []
throwable_sm_assets = []
throwable_bp_assets = []

def logit0(info):
    unreal.log(info)

def logit(info):
    unreal.log_warning(info)

def logit2(info):
    unreal.log_error(info)

all_lib_assets = unreal.EditorAssetLibrary.list_assets("/Game/", True, False)
num_all_assets = len(all_lib_assets)
logit('Total assets count in library = '+ str(num_all_assets))
all_level_actors = unreal.EditorLevelLibrary.get_all_level_actors()


def check_lib_obj(index):
    temp_data = unreal.EditorAssetLibrary.find_asset_data(all_lib_assets[index])
    #print dir(temp_data)
    logit(">>>>>>TEMP DATA INFO START>>>>>>>>>>>")
    logit("asset_class = " + str(temp_data.asset_class))
    logit("asset_name = " + str(temp_data.asset_name))
    #logit("assign = " + temp_data.assign())
    #logit("cast = " + temp_data.cast())
    #logit("copy = " + temp_data.copy())
    #logit("get_asset = " + temp_data.get_asset())
    #logit("get_class = " + temp_data.get_class())
    #logit("get_editor_property = " + temp_data.get_editor_property())
    logit("get_export_text_name = " + temp_data.get_export_text_name())
    logit("get_full_name = " + temp_data.get_full_name())
    # logit("get_tag_value = " + temp_data.get_tag_value())
    logit("is_asset_loaded = " + str(temp_data.is_asset_loaded()))
    logit("is_redirector = " + str(temp_data.is_redirector()))
    logit("is_u_asset = " + str(temp_data.is_u_asset()))
    logit("is_valid = " + str(temp_data.is_valid()))
    logit("object_path = " + str(temp_data.object_path))
    logit("package_name = " + str(temp_data.package_name))
    logit("package_path = " + str(temp_data.package_path))
    #logit("set_editor_property = " + temp_data.set_editor_property())
    logit("static_struct = " + str(temp_data.static_struct()))
    logit("to_soft_object_path = " + str(temp_data.to_soft_object_path()))
    logit("to_tuple = " + str(temp_data.to_tuple()))
    logit(">>>>>>TEMP DATA INFO FINISH>>>>>>>>>>>")

#check_lib_obj(1)

def check_reference():
    with unreal.ScopedSlowTask(num_all_assets) as slow_find_task:
        slow_find_task.make_dialog(True)
        for asset_string in all_lib_assets:
            asset_data = unreal.EditorAssetLibrary.find_asset_data(all_lib_assets[0])
            if (asset_data.is_valid() and not asset_data.is_redirector()):
                # Find referencers
                referencers = unreal.EditorAssetLibrary.find_package_referencers_for_asset(asset_string, False)
                if(len(referencers) > 0):
                    referenced_assets.append(asset_string)
                else:
                    non_referenced_assets.append(asset_string)
            # if pressed "Cancel" button on dialog, task is cancel.
            if slow_find_task.should_cancel():
                print("Task cancelled.")
                del referenced_assets[:]
                del non_referenced_assets[:]
                break

            # Advance progress
            slow_find_task.enter_progress_frame(1, asset_string)
            
    # Display
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("[Found library assets] " + str(num_all_assets))
    print("[referenced assets] " + str(len(referenced_assets)))
    '''for asset_string in referenced_assets:
        print("    " + asset_string)
    print("---------------------")
    print("[Non referenced assets] " + str(len(non_referenced_assets)))
    for asset_string in non_referenced_assets:
        print("    " + asset_string)'''
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def rename_level_throwable_label():
    p = re.compile('\d\d\d.*ThrowableBreakable')
    p1 = re.compile('.*ThrowableBreakable')
    p2 = re.compile('<type \'Actor\'>')
    
    for actor in all_level_actors:
        if (len((p1.findall(actor.get_full_name())))>0):
            logit("Object Name = " + actor.get_name() + " / type = " + str(type(actor)))
            if (len(p2.findall(str(type(actor))))):
                if str(actor.get_actor_label()).startswith('S_'):
                    logit(str(actor.get_fname()) + " is Actor but With Wrong Prefix")
                    old_name = str(actor.get_actor_label())
                    new_name = old_name.replace('S_','BP_')
                    actor.set_actor_label(new_name)
                    logit0(old_name + ' --> ' + new_name + ' done.')
                if str(actor.get_actor_label()).startswith('SM_'):
                    logit(str(actor.get_fname()) + " is Actor but With Wrong Prefix")
                    old_name = str(actor.get_actor_label())
                    new_name = old_name.replace('SM_','BP_')
                    actor.set_actor_label(new_name)
                    logit0(old_name + ' --> ' + new_name + ' done.')
            else:
                logit2('Warning '+ str(actor.get_fname()) + " is not actor but in ThrowableBreakable!")

rename_level_throwable_label()