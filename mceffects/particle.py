from .math import *
from .output import Output


class Particle:
    """
    Particle
    """

    @staticmethod
    def _create(name: str, pos: Vec3, delta: Vec3 | None = None, speed: float | None = 0.0, count: int | None = 1,
                force: bool = False):

        if delta is None:
            Output.write(f"particle {name} {str(pos)}")
        else:
            Output.write(f"particle {name} {str(pos)} {str(delta)} {speed:.4f} {count} {'force' if force else 'normal'}")

    @staticmethod
    def _create_param(name: str, param, pos: Vec3, delta: Vec3 | None = None, speed: float | None = 0.0,
                      count: int | None = 1, force: bool = False):

        if delta is None:
            Output.write(f"particle {str(param)} {name} {str(pos)}")
        else:
            Output.write(f"particle {str(param)} {name} {str(pos)} {str(delta)} {speed:.4f} {count} {'force' if force else 'normal'}")

    @staticmethod
    def _particle(name: str):
        def internal1(_):
            def internal2(pos: Vec3, delta: Vec3 | None = None, speed: float | None = 0.0, count: int | None = 1,
                          force: bool = False):

                Particle._create(name, pos, delta, speed, count, force)

            return internal2

        return internal1

    @staticmethod
    def _particle_param(name: str):
        def internal1(_):
            def internal2(pos: Vec3, param, delta: Vec3 | None = None, speed: float | None = 0.0,
                          count: int | None = 1, force: bool = False):

                Particle._create_param(name, param, pos, delta, speed, count, force)

            return internal2

        return internal1

    @staticmethod
    @_particle("ambient_entity_effect")
    def ambient_entity_effect(self):
        pass

    @staticmethod
    @_particle("angry_villager")
    def angry_villager(self):
        pass

    @staticmethod
    @_particle("ash")
    def ash(self):
        pass

    @staticmethod
    @_particle_param("block")
    def block(self):
        pass

    @staticmethod
    @_particle_param("block_marker")
    def block_marker(self):
        pass

    @staticmethod
    @_particle("bubble")
    def bubble(self):
        pass

    @staticmethod
    @_particle("bubble_column_up")
    def bubble_column_up(self):
        pass

    @staticmethod
    @_particle("bubble_pop")
    def bubble_pop(self):
        pass

    @staticmethod
    @_particle("campfire_cosy_smoke")
    def campfire_cosy_smoke(self):
        pass

    @staticmethod
    @_particle("campfire_signal_smoke")
    def campfire_signal_smoke(self):
        pass

    @staticmethod
    @_particle("cloud")
    def cloud(self):
        pass

    @staticmethod
    @_particle("composter")
    def composter(self):
        pass

    @staticmethod
    @_particle("crimson_spore")
    def crimson_spore(self):
        pass

    @staticmethod
    @_particle("crit")
    def crit(self):
        pass

    @staticmethod
    @_particle("current_down")
    def current_down(self):
        pass

    @staticmethod
    @_particle("damage_indicator")
    def damage_indicator(self):
        pass

    @staticmethod
    @_particle("dolphin")
    def dolphin(self):
        pass

    @staticmethod
    @_particle("dragon_breath")
    def dragon_breath(self):
        pass

    @staticmethod
    @_particle("dripping_dripstone_lava")
    def dripping_dripstone_lava(self):
        pass

    @staticmethod
    @_particle("dripping_dripstone_water")
    def dripping_dripstone_water(self):
        pass

    @staticmethod
    @_particle("dripping_honey")
    def dripping_honey(self):
        pass

    @staticmethod
    @_particle("dripping_lava")
    def dripping_lava(self):
        pass

    @staticmethod
    @_particle("dripping_obsidian_tear")
    def dripping_obsidian_tear(self):
        pass

    @staticmethod
    @_particle("dripping_water")
    def dripping_water(self):
        pass

    @staticmethod
    @_particle_param("dust")
    def dust(self):
        pass

    @staticmethod
    @_particle_param("dust_color_transition")
    def dust_color_transition(self):
        pass

    @staticmethod
    @_particle_param("effect")
    def effect(self):
        pass

    @staticmethod
    @_particle("elder_guardian")
    def elder_guardian(self):
        pass

    @staticmethod
    @_particle("electric_spark")
    def electric_spark(self):
        pass

    @staticmethod
    @_particle("enchant")
    def enchant(self):
        pass

    @staticmethod
    @_particle("enchanted_hit")
    def enchanted_hit(self):
        pass

    @staticmethod
    @_particle("end_rod")
    def end_rod(self):
        pass

    @staticmethod
    @_particle_param("entity_effect")
    def entity_effect(self):
        pass

    @staticmethod
    @_particle("explosion")
    def explosion(self):
        pass

    @staticmethod
    @_particle("explosion_emitter")
    def explosion_emitter(self):
        pass

    @staticmethod
    @_particle("falling_dripstone_lava")
    def falling_dripstone_lava(self):
        pass

    @staticmethod
    @_particle("falling_dripstone_water")
    def falling_dripstone_water(self):
        pass

    @staticmethod
    @_particle_param("falling_dust")
    def falling_dust(self):
        pass

    @staticmethod
    @_particle("falling_honey")
    def falling_honey(self):
        pass

    @staticmethod
    @_particle("falling_lava")
    def falling_lava(self):
        pass

    @staticmethod
    @_particle("falling_nectar")
    def falling_nectar(self):
        pass

    @staticmethod
    @_particle("falling_obsidian_tear")
    def falling_obsidian_tear(self):
        pass

    @staticmethod
    @_particle("falling_spore_blossom")
    def falling_spore_blossom(self):
        pass

    @staticmethod
    @_particle("falling_water")
    def falling_water(self):
        pass

    @staticmethod
    @_particle_param("firework")
    def firework(self):
        pass

    @staticmethod
    @_particle("fishing")
    def fishing(self):
        pass

    @staticmethod
    @_particle("flame")
    def flame(self):
        pass

    @staticmethod
    @_particle("flash")
    def flash(self):
        pass

    @staticmethod
    @_particle("glow")
    def glow(self):
        pass

    @staticmethod
    @_particle("glow_squid_ink")
    def glow_squid_ink(self):
        pass

    @staticmethod
    @_particle("happy_villager")
    def happy_villager(self):
        pass

    @staticmethod
    @_particle("heart")
    def heart(self):
        pass

    @staticmethod
    @_particle_param("instant_effect")
    def instant_effect(self):
        pass

    @staticmethod
    @_particle_param("item")
    def item(self):
        pass

    @staticmethod
    @_particle("item_slime")
    def item_slime(self):
        pass

    @staticmethod
    @_particle("item_snowball")
    def item_snowball(self):
        pass

    @staticmethod
    @_particle("landing_honey")
    def landing_honey(self):
        pass

    @staticmethod
    @_particle("landing_lava")
    def landing_lava(self):
        pass

    @staticmethod
    @_particle("landing_obsidian_tear")
    def landing_obsidian_tear(self):
        pass

    @staticmethod
    @_particle("large_smoke")
    def large_smoke(self):
        pass

    @staticmethod
    @_particle("lava")
    def lava(self):
        pass

    @staticmethod
    @_particle("mycelium")
    def mycelium(self):
        pass

    @staticmethod
    @_particle("nautilus")
    def nautilus(self):
        pass

    @staticmethod
    @_particle_param("note")
    def note(self):
        pass

    @staticmethod
    @_particle("poof")
    def poof(self):
        pass

    @staticmethod
    @_particle("portal")
    def portal(self):
        pass

    @staticmethod
    @_particle("rain")
    def rain(self):
        pass

    @staticmethod
    @_particle("scrape")
    def scrape(self):
        pass

    @staticmethod
    @_particle("sculk_charge")
    def sculk_charge(self):
        pass

    @staticmethod
    @_particle("sculk_charge_pop")
    def sculk_charge_pop(self):
        pass

    @staticmethod
    @_particle("sculk_soul")
    def sculk_soul(self):
        pass

    @staticmethod
    @_particle("shriek")
    def shriek(self):
        pass

    @staticmethod
    @_particle("smoke")
    def smoke(self):
        pass

    @staticmethod
    @_particle("sneeze")
    def sneeze(self):
        pass

    @staticmethod
    @_particle("snowflake")
    def snowflake(self):
        pass

    @staticmethod
    @_particle("sonic_boom")
    def sonic_boom(self):
        pass

    @staticmethod
    @_particle("soul")
    def soul(self):
        pass

    @staticmethod
    @_particle("soul_fire_flame")
    def soul_fire_flame(self):
        pass

    @staticmethod
    @_particle("spit")
    def spit(self):
        pass

    @staticmethod
    @_particle("spore_blossom_air")
    def spore_blossom_air(self):
        pass

    @staticmethod
    @_particle("splash")
    def splash(self):
        pass

    @staticmethod
    @_particle("squid_ink")
    def squid_ink(self):
        pass

    @staticmethod
    @_particle("sweep_attack")
    def sweep_attack(self):
        pass

    @staticmethod
    @_particle("totem_of_undying")
    def totem_of_undying(self):
        pass

    @staticmethod
    @_particle("underwater")
    def underwater(self):
        pass

    @staticmethod
    @_particle("vibration")
    def vibration(self):
        pass

    @staticmethod
    @_particle("warped_spore")
    def warped_spore(self):
        pass

    @staticmethod
    @_particle("wax_off")
    def wax_off(self):
        pass

    @staticmethod
    @_particle("wax_on")
    def wax_on(self):
        pass

    @staticmethod
    @_particle("white_ash")
    def white_ash(self):
        pass

    @staticmethod
    @_particle("witch")
    def witch(self):
        pass
