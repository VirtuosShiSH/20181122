import unreal

workingPath = "/Game/"

@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

editorAssetLib = GetEditorAssetLibrary();

#all_asset_string = editorAssetLib.list_assets(workingPath, True, False)
all_asset_string = unreal.EditorAssetLibrary.list_assets(workingPath, True, False)
num_target_assets=len(all_asset_string)
unreal.log('Total assets count = '+ str(num_target_assets))
#print help(editorAssetLib)

temp_data = unreal.EditorAssetLibrary.find_asset_data(all_asset_string[0])
print dir(temp_data)

print ("asset_class = " + str(temp_data.asset_class))
print ("asset_name = " + str(temp_data.asset_name))
#print ("assign = " + temp_data.assign())
# print ("cast = " + temp_data.cast())
# print ("copy = " + temp_data.copy())
# print ("get_asset = " + temp_data.get_asset())
# print ("get_class = " + temp_data.get_class())
# print ("get_editor_property = " + temp_data.get_editor_property())
print ("get_export_text_name = " + temp_data.get_export_text_name())
print ("get_full_name = " + temp_data.get_full_name())
# print ("get_tag_value = " + temp_data.get_tag_value())
print ("is_asset_loaded = " + str(temp_data.is_asset_loaded()))
print ("is_redirector = " + str(temp_data.is_redirector()))
print ("is_u_asset = " + str(temp_data.is_u_asset()))
print ("is_valid = " + str(temp_data.is_valid()))
print ("object_path = " + str(temp_data.object_path))
print ("package_name = " + str(temp_data.package_name))
print ("package_path = " + str(temp_data.package_path))
#print ("set_editor_property = " + temp_data.set_editor_property())
print ("static_struct = " + str(temp_data.static_struct()))
print ("to_soft_object_path = " + str(temp_data.to_soft_object_path()))
print ("to_tuple = " + str(temp_data.to_tuple()))


referenced_assets = []
non_referenced_assets = []
throwable_bp_assets = []


with unreal.ScopedSlowTask(num_target_assets) as slow_find_task:
    slow_find_task.make_dialog(True)
    for asset_string in all_asset_string:
        asset_data = unreal.EditorAssetLibrary.find_asset_data(asset_string)

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
print("[Find assets] " + str(num_target_assets))
print("[referenced assets] " + str(len(referenced_assets)))
'''for asset_string in referenced_assets:
    print("    " + asset_string)
print("---------------------")
print("[Non referenced assets] " + str(len(non_referenced_assets)))
for asset_string in non_referenced_assets:
    print("    " + asset_string)'''

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
'''
if (len(all_asset_string) > 0):
    for asset in all_asset_string:
        deps = editorAssetLib.find_package_referencers_for_asset(asset, False)
        print type(asset)
        print type(deps[0])
        print (deps[0])
        print(deps[0].get_name())
        if (len(deps) == 0):
            print ">>>%s" % asset
            '''


