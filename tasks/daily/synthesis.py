from module.screen import screen
from module.automation import auto
from module.logger import log
import time

import pygetwindow as gw


class Synthesis:
    @staticmethod
    def upgrade_relic():
        try:
            log.hr("准备升级遗器", 2)
            screen.change_to('bag_relicset')
            # 筛选规则
            if auto.click_element("./assets/images/share/synthesis/filter.png", "image", 0.9, max_retries=10):
                # 等待筛选界面弹出
                time.sleep(1)
                if auto.click_element("assets/images/zh_CN/relicset/statement.png","image", 0.9, max_retries=10):
                    if auto.click_element("./assets/images/zh_CN/relicset/not_max.png","image", 0.9, max_retries=10):
                        # 获取窗口坐标
                        window = gw.getWindowsWithTitle("崩坏：星穹铁道")[0]
                        if not window:
                            raise Exception("未找到崩坏：星穹铁道窗口")
                        # 获取窗口位置和大小
                        left, top = window.left, window.top
                        left = left + 136
                        top = top + 213
                        right = left + 235 - 136
                        bottom = top + 318 - 213
                        if auto.click_element_with_pos(((left,top),(right, bottom))):
                            for _ in range(10):
                                if auto.click_element("./assets/images/zh_CN/relicset/upgrade.png", "image", 0.9, max_retries=10):
                                    if auto.click_element("./assets/images/zh_CN/relicset/auto_in.png", "image", 0.9, max_retries=10):
                                        if auto.click_element("./assets/images/zh_CN/relicset/upgrade.png", "image", 0.9, max_retries=10):
                                            time.sleep(3)
                                            if auto.click_element("./assets/images/zh_CN/base/click_close.png", "image", 0.8, max_retries=10):
                                                log.info("升级遗器完成")
                                                screen.change_to('main')
                                                return True                                       
            log.error("升级遗器失败")
        except Exception as e:
            log.error(f"升级遗器失败: {e}")
        return False

    @staticmethod
    def consumables():
        try:
            log.hr("准备合成消耗品", 2)
            screen.change_to('consumables')
            # 筛选规则
            if auto.click_element("./assets/images/share/synthesis/filter.png", "image", 0.9, max_retries=10):
                # 等待筛选界面弹出
                time.sleep(1)
                if auto.click_element("防御类消耗品", "text", max_retries=10, crop=(472.0 / 1920, 347.0 / 1080, 970.0 / 1920, 268.0 / 1080)):
                    if auto.click_element("./assets/images/zh_CN/base/confirm.png", "image", 0.9, max_retries=10):
                        # 多次重试避免选中没反应
                        for _ in range(10):
                            auto.click_element("./assets/images/share/synthesis/defensive_medicine.png", "image", 0.8, max_retries=10)
                            if auto.find_element("./assets/images/share/synthesis/defensive_medicine_selected.png", "image", 0.8, max_retries=10):
                                if auto.click_element("./assets/images/zh_CN/synthesis/synthesis_button.png", "image", 0.9, max_retries=10):
                                    if auto.click_element("./assets/images/zh_CN/base/confirm.png", "image", 0.9, max_retries=10):
                                        if auto.click_element("./assets/images/zh_CN/base/click_close.png", "image", 0.8, max_retries=10):
                                            log.info("合成消耗品完成")
                                            return True
                                break
            log.error("合成消耗品失败")
        except Exception as e:
            log.error(f"合成消耗品失败: {e}")
        return False

    @staticmethod
    def material():
        try:
            log.hr("准备合成材料", 2)
            screen.change_to('material')
            # 筛选规则
            if auto.click_element("./assets/images/share/synthesis/filter.png", "image", 0.9, max_retries=10):
                # 等待筛选界面弹出
                time.sleep(1)
                if auto.click_element("通用培养材料", "text", max_retries=10, crop=(478.0 / 1920, 350.0 / 1080, 981.0 / 1920, 399.0 / 1080)):
                    if auto.click_element("./assets/images/zh_CN/base/confirm.png", "image", 0.9, max_retries=10):
                        # 多次重试避免选中没反应
                        for _ in range(10):
                            auto.click_element("./assets/images/share/synthesis/nuclear.png", "image", 0.9, max_retries=10)
                            if auto.find_element("./assets/images/share/synthesis/nuclear_selected.png", "image", 0.9, max_retries=10):
                                if auto.click_element("./assets/images/zh_CN/synthesis/synthesis_button.png", "image", 0.9, max_retries=10):
                                    if auto.click_element("./assets/images/zh_CN/base/confirm.png", "image", 0.9, max_retries=10):
                                        if auto.click_element("./assets/images/zh_CN/base/click_close.png", "image", 0.8, max_retries=10):
                                            log.info("合成材料完成")
                                            return True
                                break
            log.error("合成材料失败")
        except Exception as e:
            log.error(f"合成材料失败: {e}")
        return False

    @staticmethod
    def use_consumables(recursion=True):
        try:
            log.hr("准备使用消耗品", 2)
            screen.change_to('bag_consumables')
            # 筛选规则
            if auto.click_element("./assets/images/share/synthesis/filter.png", "image", 0.9, max_retries=10):
                # 等待筛选界面弹出
                time.sleep(1)
                if auto.click_element("防御类消耗品", "text", max_retries=10, crop=(472.0 / 1920, 347.0 / 1080, 970.0 / 1920, 268.0 / 1080)):
                    if auto.click_element("./assets/images/zh_CN/base/confirm.png", "image", 0.9, max_retries=10):
                        # 多次重试避免选中没反应
                        for _ in range(10):
                            if auto.click_element("./assets/images/share/synthesis/defensive_medicine.png", "image", 0.8, max_retries=10):
                                if auto.find_element("./assets/images/share/bag/defensive_medicine_selected.png", "image", 0.8, max_retries=10):
                                    if auto.click_element("./assets/images/zh_CN/base/use.png", "image", 0.9, max_retries=10):
                                        if auto.click_element("./assets/images/zh_CN/base/confirm.png", "image", 0.9, max_retries=10):
                                            auto.click_element("./assets/images/zh_CN/base/confirm.png", "image", 0.9, max_retries=2)
                                            if auto.find_element("./assets/images/screen/bag/bag_consumables.png", "image", 0.9, max_retries=10):
                                                log.info("使用消耗品完成")
                                                return True
                                    break
                                continue
                            elif recursion:
                                log.info("没有可用的消耗品，尝试合成")
                                if Synthesis.consumables():
                                    return Synthesis.use_consumables(False)
                                else:
                                    break
                            else:
                                break
            log.error("使用消耗品失败")
        except Exception as e:
            log.error(f"使用消耗品失败: {e}")
        return False
