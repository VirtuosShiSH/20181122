import unreal
import re

throwable_sm_assets = []
throwable_bp_assets = []

# output = False
output = True

def logit0(info):
        unreal.log(info)

def logit1(info):
    if output:
        unreal.log_warning(info)

def logit2(info):
        unreal.log_error(info)

all_level_actors = unreal.EditorLevelLibrary.get_all_level_actors()

def fix_label_prefix():
    p_static = re.compile('\d\d\d_Pickups_StaticReference')
    p_throwable = re.compile('\d\d\d_ThrowableBreakable')
    p_ThrowableBP = re.compile('^BP_.*_Throwable_C')
    StaticRefCount = 0
    ThrowableCount = 0
    
    specials = {}   #=Dictionary of special replacement. BP Name -> Original Item Name In Level
    specials['BP_Panzer_Officer_Hat'] = 'Panzer_Officer_hat'
    specials['BP_Wehrmacht_Soldier_Helmet_M'] = 'HelmetGermany'

    for actor in all_level_actors:
        # if str(actor.get_name())=='BP_BindersClose3':
        #     logit1(dir(actor))
        #     logit1(actor.get_full_name())
        #     logit1(actor.get_fname())

        # if str(actor.get_name())=='BP_BindersClose2':
        # if str(actor.get_name())=='HelmetGermany13':
        #     #logit1(dir(actor))
        #     logit1(actor.get_full_name())
        #     logit1(actor.get_fname())

        if (len((p_static.findall(actor.get_full_name())))):#item in StaticReferrence Level
            logit1("Static Reference Object = " + actor.get_name())# + " / type = " + str(type(actor)))
            StaticRefCount += 1
            if (len(p_ThrowableBP.findall(actor.get_full_name()))):#check if item is throwable BP
                logit2('Warning: '+ str(actor.get_fname()) + " is Throwable but in the StaticReference Level! Please check.")
        if (len((p_throwable.findall(actor.get_full_name())))):#Item in ThrowableBreakable Level
            if not actor.is_child_actor():#Item is not child actor like breakables
                logit1("ThrowableBreakable Object = " + actor.get_name())# + " / type = " + str(type(actor)))
                if (len(p_ThrowableBP.findall(actor.get_full_name()))):#check if item is throwable BP
                    ThrowableCount += 1
                    if str(actor.get_actor_label()).startswith('S_'):
                        logit1(str(actor.get_fname()) + " is BP Actor with wrong prefix")
                        old_name = str(actor.get_actor_label())
                        new_name = old_name.replace('S_','BP_')
                        actor.set_actor_label(new_name)
                        logit0(old_name + ' --> ' + new_name + ' done.')
                    if str(actor.get_actor_label()).startswith('SM_'):
                        logit1(str(actor.get_fname()) + " is BP Actor with wrong prefix")
                        old_name = str(actor.get_actor_label())
                        new_name = old_name.replace('SM_','BP_')
                        actor.set_actor_label(new_name)
                        logit0(old_name + ' --> ' + new_name + ' done.')
                    continue
                else:
                    actor_special = False
                    for key in specials.keys():#check all special objects
                        p_spe = re.compile('^'+key)
                        p_spe1 = re.compile('^'+specials[key])
                        if len(p_spe.findall(actor.get_full_name())):
                            ThrowableCount += 1
                            actor_special = True
                            logit1('^^^special replacement^^^')
                            if len(p_spe1.findall(actor.get_name())):
                                old_name = str(actor.get_actor_label())
                                new_name = old_name.replace(specials[key],key)
                                actor.set_actor_label(new_name)
                                logit0(old_name + ' --> ' + new_name + ' done.')
                            continue
                    if actor_special == False:
                        logit2('Warning: '+ str(actor.get_fname()) + " is not Throwable/Special but in the ThrowableBreakable Level! Please check.")
            else:
                logit1('Child Object = '+ str(actor.get_fname()))


    logit0('Objects Count of StaticReference = '+ str(StaticRefCount))
    logit0('Objects Count of ThrowableBreakable = '+ str(ThrowableCount))
    logit0('DONE')

fix_label_prefix()