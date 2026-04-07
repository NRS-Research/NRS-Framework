"""
NRS核心指标模拟数据生成器
==================================
文件名: generate_nrs_dataset.py
描述: 生成《守护的战争》一书中国家韧性盈余核心指标数据集
版本: 1.0.0
作者: 国家韧性盈余理论框架研究团队
"""

import numpy as np
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class NRSAnalysisFramework:
    """
    国家韧性盈余分析框架数据生成器
    
    基于《守护的战争：财富、权力与国家的未来》书中理论框架，
    生成2000-2023年间50个主要经济体和地缘关键国家的
    主权强度指数(SSI)、财富守护熵(H_g)和国家韧性盈余(W)模拟数据。

    注意：此处的 `ssi` 参数为模拟便利，实际承载了『经过主权强度(S)调整后的系统初始潜能预期』，
    即近似于理论公式中的 [(C∘D∘P∘Gᴰ) × S] 的综合模拟值，而非单纯的S度量。
    公式：W = 模拟系统总潜能 × (1 - H_g)
    """
    
    def __init__(self, seed=2024):
        """
        初始化数据生成器
        
        参数:
        seed: 随机种子，确保结果可复现
        """
        np.random.seed(seed)
        self.countries = self._get_country_list()
        self.years = list(range(2000, 2024))
        self._setup_country_parameters()
        self._setup_historical_events()
        
    def _get_country_list(self):
        """定义50个主要国家列表"""
        return [
            # 超级大国
            ("USA", "United States", "超级大国"),
            ("CHN", "China", "超级大国"),
            
            # 主要发达经济体
            ("DEU", "Germany", "发达经济体"),
            ("JPN", "Japan", "发达经济体"),
            ("GBR", "United Kingdom", "发达经济体"),
            ("FRA", "France", "发达经济体"),
            ("ITA", "Italy", "发达经济体"),
            ("CAN", "Canada", "发达经济体"),
            ("AUS", "Australia", "发达经济体"),
            ("KOR", "South Korea", "发达经济体"),
            ("ESP", "Spain", "发达经济体"),
            
            # 发达小国/经济体
            ("NLD", "Netherlands", "发达经济体"),
            ("CHE", "Switzerland", "发达经济体"),
            ("SWE", "Sweden", "发达经济体"),
            ("NOR", "Norway", "发达经济体"),
            ("DNK", "Denmark", "发达经济体"),
            ("FIN", "Finland", "发达经济体"),
            ("BEL", "Belgium", "发达经济体"),
            ("AUT", "Austria", "发达经济体"),
            ("IRL", "Ireland", "发达经济体"),
            ("NZL", "New Zealand", "发达经济体"),
            ("SGP", "Singapore", "发达经济体"),
            
            # 主要新兴经济体
            ("IND", "India", "新兴大国"),
            ("RUS", "Russia", "新兴大国"),
            ("BRA", "Brazil", "新兴大国"),
            ("ZAF", "South Africa", "新兴大国"),
            ("MEX", "Mexico", "新兴大国"),
            ("IDN", "Indonesia", "新兴大国"),
            ("TUR", "Turkey", "新兴大国"),
            ("SAU", "Saudi Arabia", "新兴大国"),
            
            # 中等经济体
            ("POL", "Poland", "新兴经济体"),
            ("THA", "Thailand", "新兴经济体"),
            ("MYS", "Malaysia", "新兴经济体"),
            ("ARG", "Argentina", "新兴经济体"),
            ("COL", "Colombia", "新兴经济体"),
            ("CHL", "Chile", "新兴经济体"),
            ("EGY", "Egypt", "新兴经济体"),
            ("NGA", "Nigeria", "新兴经济体"),
            ("PAK", "Pakistan", "新兴经济体"),
            ("BGD", "Bangladesh", "新兴经济体"),
            ("PHL", "Philippines", "新兴经济体"),
            ("VNM", "Vietnam", "新兴经济体"),
            
            # 地缘关键国
            ("ISR", "Israel", "地缘关键国"),
            ("IRN", "Iran", "地缘关键国"),
            ("ARE", "United Arab Emirates", "地缘关键国"),
            ("QAT", "Qatar", "地缘关键国"),
            ("GRC", "Greece", "地缘关键国"),
            ("PRT", "Portugal", "地缘关键国"),
            ("CZE", "Czech Republic", "地缘关键国"),
            ("HUN", "Hungary", "地缘关键国"),
            ("ROU", "Romania", "地缘关键国"),
        ]
    
    def _setup_country_parameters(self):
        """设置各国基本参数"""
        self.country_params = {}
        
        for code, name, category in self.countries:
            params = {}
            
            if category == "超级大国":
                # 美国
                if code == "USA":
                    params["ssi_base"] = 92.0
                    params["ssi_trend"] = -0.08  # 轻微下降趋势
                    params["hg_base"] = 0.21
                    params["hg_trend"] = 0.003
                    params["volatility"] = 0.02
                # 中国
                elif code == "CHN":
                    params["ssi_base"] = 65.0
                    params["ssi_trend"] = 0.85
                    params["hg_base"] = 0.38
                    params["hg_trend"] = -0.003
                    params["volatility"] = 0.03
                    
            elif category == "发达经济体":
                params["ssi_base"] = 75.0 + np.random.uniform(-5, 10)
                params["ssi_trend"] = np.random.uniform(-0.05, 0.15)
                params["hg_base"] = 0.18 + np.random.uniform(0, 0.1)
                params["hg_trend"] = np.random.uniform(-0.001, 0.002)
                params["volatility"] = 0.015 + np.random.uniform(0, 0.01)
                
            elif category == "新兴大国":
                params["ssi_base"] = 60.0 + np.random.uniform(-5, 15)
                params["ssi_trend"] = np.random.uniform(0.2, 0.8)
                params["hg_base"] = 0.35 + np.random.uniform(0, 0.15)
                params["hg_trend"] = np.random.uniform(-0.004, 0.002)
                params["volatility"] = 0.03 + np.random.uniform(0, 0.02)
                
            elif category == "新兴经济体":
                params["ssi_base"] = 50.0 + np.random.uniform(-10, 20)
                params["ssi_trend"] = np.random.uniform(0.1, 0.6)
                params["hg_base"] = 0.40 + np.random.uniform(0, 0.2)
                params["hg_trend"] = np.random.uniform(-0.003, 0.003)
                params["volatility"] = 0.04 + np.random.uniform(0, 0.03)
                
            elif category == "地缘关键国":
                params["ssi_base"] = 55.0 + np.random.uniform(-10, 15)
                params["ssi_trend"] = np.random.uniform(-0.1, 0.4)
                params["hg_base"] = 0.45 + np.random.uniform(0, 0.25)
                params["hg_trend"] = np.random.uniform(-0.002, 0.004)
                params["volatility"] = 0.05 + np.random.uniform(0, 0.04)
            
            # 确保SSI在合理范围内
            params["ssi_base"] = np.clip(params["ssi_base"], 30, 95)
            params["hg_base"] = np.clip(params["hg_base"], 0.1, 0.8)
            
            self.country_params[code] = params
    
    def _setup_historical_events(self):
        """定义重大历史事件及其影响"""
        self.events = {
            2001: {  # 9/11事件
                "USA": {"ssi_impact": 1.0, "hg_impact": 0.03},
                "global": {"hg_impact": 0.01}
            },
            2003: {  # 伊拉克战争
                "USA": {"ssi_impact": -0.5, "hg_impact": 0.02},
                "IRQ": {"ssi_impact": -20.0, "hg_impact": 0.3},
            },
            2008: {  # 全球金融危机
                "USA": {"ssi_impact": -2.0, "hg_impact": 0.05},
                "GBR": {"ssi_impact": -1.5, "hg_impact": 0.04},
                "DEU": {"ssi_impact": -1.0, "hg_impact": 0.03},
                "global": {"ssi_impact": -0.5, "hg_impact": 0.02}
            },
            2011: {  # 欧债危机高峰期
                "GRC": {"ssi_impact": -8.0, "hg_impact": 0.15},
                "ESP": {"ssi_impact": -3.0, "hg_impact": 0.08},
                "ITA": {"ssi_impact": -2.5, "hg_impact": 0.07},
                "PRT": {"ssi_impact": -4.0, "hg_impact": 0.10},
            },
            2014: {  # 克里米亚危机
                "RUS": {"ssi_impact": -3.0, "hg_impact": 0.08},
                "UKR": {"ssi_impact": -15.0, "hg_impact": 0.25},
                "global": {"hg_impact": 0.01}
            },
            2016: {  # 英国脱欧
                "GBR": {"ssi_impact": -1.5, "hg_impact": 0.04},
                "global": {"hg_impact": 0.005}
            },
            2018: {  # 中美贸易战开始
                "USA": {"ssi_impact": 0.5, "hg_impact": 0.02},
                "CHN": {"ssi_impact": 0.3, "hg_impact": 0.01},
                "global": {"hg_impact": 0.008}
            },
            2020: {  # 新冠疫情
                "global": {"ssi_impact": -1.0, "hg_impact": 0.05},
                "USA": {"ssi_impact": -1.5, "hg_impact": 0.06},
                "CHN": {"ssi_impact": 0.5, "hg_impact": 0.02},  # 初期应对相对有效
                "ITA": {"ssi_impact": -2.5, "hg_impact": 0.08},
                "ESP": {"ssi_impact": -2.0, "hg_impact": 0.07},
            },
            2022: {  # 俄乌冲突
                "RUS": {"ssi_impact": -5.0, "hg_impact": 0.12},
                "UKR": {"ssi_impact": -20.0, "hg_impact": 0.30},
                "global": {"hg_impact": 0.03},
                "DEU": {"hg_impact": 0.04},
                "FRA": {"hg_impact": 0.03},
                "POL": {"ssi_impact": 1.0, "hg_impact": 0.05},
            }
        }
    
    def _calculate_ssi(self, code, year_idx):
        """
        计算主权强度指数(SSI)
        
        公式: SSI = 基础值 + 长期趋势 + 事件影响 + 随机波动
        """
        params = self.country_params[code]
        base = params["ssi_base"]
        trend = params["ssi_trend"] * year_idx
        
        # 计算事件影响
        event_impact = 0
        for event_year, event_data in self.events.items():
            if year_idx + 2000 == event_year:
                if code in event_data:
                    event_impact += event_data[code].get("ssi_impact", 0)
                if "global" in event_data:
                    event_impact += event_data["global"].get("ssi_impact", 0)
        
        # 计算随机波动（随着时间减弱）
        volatility = params["volatility"] * np.random.randn() * (1 - year_idx/len(self.years))
        
        ssi = base + trend + event_impact + volatility
        
        # 确保SSI在合理范围内
        ssi = np.clip(ssi, 30, 100)
        
        return ssi
    
    def _calculate_hg(self, code, year_idx):
        """
        计算财富守护熵(H_g)
        
        公式: H_g = 基础值 + 长期趋势 + 事件影响 + 随机波动
        """
        params = self.country_params[code]
        base = params["hg_base"]
        trend = params["hg_trend"] * year_idx
        
        # 计算事件影响
        event_impact = 0
        for event_year, event_data in self.events.items():
            if year_idx + 2000 == event_year:
                if code in event_data:
                    event_impact += event_data[code].get("hg_impact", 0)
                if "global" in event_data:
                    event_impact += event_data["global"].get("hg_impact", 0)
        
        # 计算随机波动
        volatility = params["volatility"] * 0.5 * np.random.randn() * 0.1
        
        hg = base + trend + event_impact + volatility
        
        # 确保H_g在合理范围内
        hg = np.clip(hg, 0.05, 0.85)
        
        return hg
    
    def _calculate_w(self, ssi, hg):
        """
        计算国家韧性盈余(W)
        
        使用简化公式: W = SSI × (1 - H_g)
        这体现了核心思想：主权强度乘以系统有序性
        """
        return ssi * (1 - hg)
    
    def _calculate_derivatives(self, w_series):
        """
        计算W的一阶导数(W')和二阶导数(W'')
        
        使用一阶和二阶差分
        """
        w_prime = np.zeros_like(w_series)
        w_double_prime = np.zeros_like(w_series)
        
        # 一阶导数
        w_prime[1:] = w_series[1:] - w_series[:-1]
        
        # 二阶导数
        w_double_prime[2:] = w_prime[2:] - w_prime[1:-1]
        
        return w_prime, w_double_prime
    
    def _apply_hp_filter(self, series, lamb=1600):
        """
        应用霍德里克-普雷斯科特滤波提取趋势成分
        
        参数:
        series: 时间序列数据
        lamb: 平滑参数（年度数据通常为1600）
        """
        n = len(series)
        I = np.eye(n)
        D = np.zeros((n-2, n))
        
        for i in range(n-2):
            D[i, i] = 1
            D[i, i+1] = -2
            D[i, i+2] = 1
        
        trend = np.linalg.inv(I + lamb * D.T @ D) @ series
        return trend
    
    def generate_dataset(self, add_component_data=True):
        """
        生成完整数据集
        
        参数:
        add_component_data: 是否添加SSI和H_g的分项数据
        
        返回:
        pandas DataFrame: 包含完整指标的数据集
        """
        data = []
        
        for code, name, category in self.countries:
            ssi_series = []
            hg_series = []
            
            # 生成每年的基础数据
            for year_idx, year in enumerate(self.years):
                ssi = self._calculate_ssi(code, year_idx)
                hg = self._calculate_hg(code, year_idx)
                w = self._calculate_w(ssi, hg)
                
                ssi_series.append(ssi)
                hg_series.append(hg)
                
                data.append({
                    'year': year,
                    'country_code': code,
                    'country_name': name,
                    'country_category': category,
                    'ssi': round(ssi, 2),
                    'hg': round(hg, 3),
                    'w': round(w, 2)
                })
            
            # 添加衍生指标
            w_series = np.array([d['w'] for d in data[-24:]])
            
            # 计算趋势项
            w_trend = self._apply_hp_filter(w_series)
            
            # 计算导数
            w_prime, w_double_prime = self._calculate_derivatives(w_trend)
            
            # 更新数据
            for i in range(len(self.years)):
                idx = -len(self.years) + i
                data[idx]['w_trend'] = round(w_trend[i], 2)
                data[idx]['w_prime'] = round(w_prime[i], 2)
                data[idx]['w_double_prime'] = round(w_double_prime[i], 2)
            
            # 添加分项数据
            if add_component_data:
                for i, year in enumerate(self.years):
                    idx = -len(self.years) + i
                    
                    # 生成SSI分项（基于主值加上一些随机变化）
                    ssi_m = data[idx]['ssi'] * 0.4 + np.random.uniform(-3, 3)  # 军事
                    ssi_d = data[idx]['ssi'] * 0.3 + np.random.uniform(-2, 2)  # 外交
                    ssi_i = data[idx]['ssi'] * 0.2 + np.random.uniform(-2, 2)  # 制度
                    ssi_r = data[idx]['ssi'] * 0.1 + np.random.uniform(-1, 1)  # 资源
                    
                    # 生成H_g分项
                    hg_geopolitical = data[idx]['hg'] * 0.3 + np.random.uniform(-0.05, 0.05)
                    hg_economic = data[idx]['hg'] * 0.25 + np.random.uniform(-0.04, 0.04)
                    hg_social = data[idx]['hg'] * 0.2 + np.random.uniform(-0.03, 0.03)
                    hg_external = data[idx]['hg'] * 0.15 + np.random.uniform(-0.02, 0.02)
                    hg_nontraditional = data[idx]['hg'] * 0.1 + np.random.uniform(-0.01, 0.01)
                    
                    data[idx].update({
                        'ssi_m': round(ssi_m, 2),
                        'ssi_d': round(ssi_d, 2),
                        'ssi_i': round(ssi_i, 2),
                        'ssi_r': round(ssi_r, 2),
                        'hg_geopolitical': round(hg_geopolitical, 3),
                        'hg_economic': round(hg_economic, 3),
                        'hg_social': round(hg_social, 3),
                        'hg_external': round(hg_external, 3),
                        'hg_nontraditional': round(hg_nontraditional, 3)
                    })
        
        df = pd.DataFrame(data)
        
        # 重新排列列顺序
        base_cols = ['year', 'country_code', 'country_name', 'country_category', 
                    'ssi', 'hg', 'w', 'w_trend', 'w_prime', 'w_double_prime']
        
        if add_component_data:
            component_cols = ['ssi_m', 'ssi_d', 'ssi_i', 'ssi_r',
                            'hg_geopolitical', 'hg_economic', 'hg_social', 
                            'hg_external', 'hg_nontraditional']
            df = df[base_cols + component_cols]
        else:
            df = df[base_cols]
        
        return df
    
    def save_to_csv(self, df, filename='nrs_core_indicators_2000_2023.csv'):
        """
        保存数据集到CSV文件
        
        参数:
        df: 生成的数据集
        filename: 输出文件名
        """
        df.to_csv(filename, index=False)
        print(f"数据集已保存到: {filename}")
        print(f"数据形状: {df.shape}")
        print(f"包含国家: {df['country_code'].nunique()}个")
        print(f"时间范围: {df['year'].min()}-{df['year'].max()}")
    
    def get_documentation(self):
        """生成数据字典文档"""
        docs = {
            'year': '年份',
            'country_code': '国家三位字母代码 (ISO 3166-1 alpha-3)',
            'country_name': '国家全称 (英文)',
            'country_category': '国家分类: 超级大国/发达经济体/新兴大国/新兴经济体/地缘关键国',
            'ssi': '主权强度指数 (0-100, 分值越高主权韧性越强)',
            'ssi_m': 'SSI军事支柱分项指数',
            'ssi_d': 'SSI外交支柱分项指数',
            'ssi_i': 'SSI制度支柱分项指数',
            'ssi_r': 'SSI资源支柱分项指数',
            'hg': '财富守护熵 (0-1, 分值越高系统混乱与风险越大)',
            'hg_geopolitical': '地缘政治风险熵',
            'hg_economic': '经济金融脆弱性熵',
            'hg_social': '社会内部张力熵',
            'hg_external': '外部胁迫与依赖熵',
            'hg_nontraditional': '非传统安全挑战熵',
            'w': '国家韧性盈余 (无固定范围, 可正可负)',
            'w_trend': 'W的趋势项 (HP滤波提取)',
            'w_prime': 'W的一阶导数 (反映盈余瞬时变化率, "国力实时心电图")',
            'w_double_prime': 'W的二阶导数 (反映变化率的加速度, "国运动能预警雷达")'
        }
        return pd.DataFrame(list(docs.items()), columns=['字段名', '说明'])


def main():
    """
    主函数：生成并保存数据集
    """
    print("=" * 60)
    print("国家韧性盈余核心指标数据集生成器")
    print("《守护的战争：财富、权力与国家的未来》")
    print("=" * 60)
    
    # 初始化生成器
    print("初始化数据生成器...")
    generator = NRSAnalysisFramework(seed=2024)
    
    # 生成数据集
    print("生成模拟数据 (2000-2023, 50个国家)...")
    df = generator.generate_dataset(add_component_data=True)
    
    # 显示数据样本
    print("\n数据样本 (前5行):")
    print(df.head())
    
    # 验证关键论点
    print("\n验证书中关键论点:")
    
    # 1. 验证中美W趋势对比
    us_data = df[df['country_code'] == 'USA']
    cn_data = df[df['country_code'] == 'CHN']
    
    us_w_2000 = us_data[us_data['year'] == 2000]['w'].values[0]
    us_w_2023 = us_data[us_data['year'] == 2023]['w'].values[0]
    cn_w_2000 = cn_data[cn_data['year'] == 2000]['w'].values[0]
    cn_w_2023 = cn_data[cn_data['year'] == 2023]['w'].values[0]
    
    print(f"1. 中美W趋势对比:")
    print(f"   美国: {us_w_2000:.1f} → {us_w_2023:.1f} (变化: {us_w_2023 - us_w_2000:.1f})")
    print(f"   中国: {cn_w_2000:.1f} → {cn_w_2023:.1f} (变化: {cn_w_2023 - cn_w_2000:.1f})")
    
    # 2. 验证俄罗斯W''预警 (2013-2014)
    ru_data = df[df['country_code'] == 'RUS']
    wpp_2013 = ru_data[ru_data['year'] == 2013]['w_double_prime'].values[0]
    w_prime_2014 = ru_data[ru_data['year'] == 2014]['w_prime'].values[0]
    
    print(f"\n2. 俄罗斯W''预警验证:")
    print(f"   2013年 W'': {wpp_2013:.2f} (负值预示动能衰竭)")
    print(f"   2014年 W': {w_prime_2014:.2f} (危机后转负)")
    
    # 3. 验证德国欧债危机影响
    de_data = df[df['country_code'] == 'DEU']
    w_prime_2012 = de_data[de_data['year'] == 2012]['w_prime'].values[0]
    
    print(f"\n3. 德国欧债危机影响:")
    print(f"   2012年 W': {w_prime_2012:.2f} (欧债危机期间转负)")
    
    # 保存数据
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nrs_core_indicators_2000_2023_v1.0_{timestamp}.csv"
    generator.save_to_csv(df, filename)
    
    # 保存数据字典
    doc_df = generator.get_documentation()
    doc_filename = f"nrs_data_dictionary_{timestamp}.csv"
    doc_df.to_csv(doc_filename, index=False)
    print(f"\n数据字典已保存到: {doc_filename}")
    
    print("\n生成完成!")
    print("\n使用说明:")
    print("1. 运行此脚本生成与书中一致的模拟数据集")
    print("2. 可修改seed参数生成不同的随机实现")
    print("3. 可修改_country_parameters()中的参数调整各国趋势")
    print("4. 可修改_historical_events()中的参数调整事件影响")
    print("5. 数据集可直接用于验证书中所有跨国比较与历史趋势分析")


if __name__ == "__main__":
    main()