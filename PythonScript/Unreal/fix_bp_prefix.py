import unreal
import re

throwable_sm_assets = []
throwable_bp_assets = []

def logit0(info):
    unreal.log(info)

def logit1(info):
    unreal.log_warning(info)

def logit2(info):
    unreal.log_error(info)

all_level_actors = unreal.EditorLevelLibrary.get_all_level_actors()

def fix_label_prefix():
    p0 = re.compile('\d\d\d_Pickups_StaticReference')
    p1 = re.compile('\d\d\d_ThrowableBreakable')
    p2 = re.compile('BP_.*_Throwable_C')
    StaticRefCount = 0
    ThrowableCount = 0
    
    for actor in all_level_actors:
        # if str(actor.get_name())=='BP_BindersClose3':
        #     logit1(dir(actor))
        #     logit1(actor.get_full_name())
        #     logit1(actor.get_fname())

        # if str(actor.get_name())=='BP_BindersClose2':
        #     #logit1(dir(actor))
        #     logit1(actor.get_full_name())
        #     logit1(actor.get_fname())

        if (len((p0.findall(actor.get_full_name())))):
            logit1("Object Name = " + actor.get_name() + " / type = " + str(type(actor)))
            StaticRefCount += 1
        if (len((p1.findall(actor.get_full_name())))):
            logit1("Object Name = " + actor.get_name() + " / type = " + str(type(actor)))
            if (len(p2.findall(actor.get_full_name()))):
                ThrowableCount += 1
                if str(actor.get_actor_label()).startswith('S_'):
                    logit1(str(actor.get_fname()) + " is Actor but With Wrong Prefix")
                    old_name = str(actor.get_actor_label())
                    new_name = old_name.replace('S_','BP_')
                    actor.set_actor_label(new_name)
                    logit0(old_name + ' --> ' + new_name + ' done.')
                if str(actor.get_actor_label()).startswith('SM_'):
                    logit1(str(actor.get_fname()) + " is Actor but With Wrong Prefix")
                    old_name = str(actor.get_actor_label())
                    new_name = old_name.replace('SM_','BP_')
                    actor.set_actor_label(new_name)
                    logit0(old_name + ' --> ' + new_name + ' done.')
            else:
                logit2('Warning '+ str(actor.get_fname()) + " is not actor but in ThrowableBreakable!")


    logit1('Total Objects Count in Static Reference = '+ str(StaticRefCount))
    logit1('Total Objects Count in Throwable = '+ str(ThrowableCount))
    logit0('DONE')

fix_label_prefix()