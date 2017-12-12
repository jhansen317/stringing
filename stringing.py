#!/usr/bin/env python

import sys
import math
import argparse

# These constants come from the stringing book...
IRON_DENSITY_FACTOR = 2436
YELLOW_BRASS_DENSITY_FACTOR = 2639
RED_BRASS_DENSITY_FACTOR = 2780

DENSITY_MAP = {'iron' : IRON_DENSITY_FACTOR, 'yellow brass' : YELLOW_BRASS_DENSITY_FACTOR, 'red brass' : RED_BRASS_DENSITY_FACTOR}

class String(object):
    def __init__(self, **kwargs):
        self.param_labels = ['tension', 'frequency', 'length', 'diameter', 'density']
        self.param_values = [kwargs.pop(label, None) for label in self.param_labels]
        self.param_funcs = [self.calc_tension, self.calc_frequency, self.calc_length, self.calc_diameter, self.calc_density]

    def calc_tension(self): 
        """
        Calculate string tension in kg as per stringing book. Arguments are:
            density factor of material (as density*pi/g, where density appears to be SI units, kg/cubic meter)
            frequency in Hz
            length in meters
            diameter in meters
        get_frequency, get_length, get_diameter, and get_density are just derived from this relation
        """
        if self.param_values[0] == None:
            self.param_values[0] = self.density * (self.frequency * self.length * self.diameter)**2

    @property
    def tension(self):
        return self.param_values[0]

    def calc_frequency(self):
        if self.param_values[1] == None:
            self.param_values[1] = math.sqrt(float(self.tension) / self.density) * 1.0 / (self.length * self.diameter)

    @property
    def frequency(self):
        return self.param_values[1]

    def calc_length(self):
        if self.param_values[2] == None:
            self.param_values[2] = math.sqrt(float(self.tension) / self.density) * 1.0 / (self.frequency * self.diameter)

    @property
    def length(self):
        return self.param_values[2]

    def calc_diameter(self):
        if self.param_values[3] == None:
            self.param_values[3] = math.sqrt(float(self.tension) / self.density) * 1.0 / (self.frequency * self.length)

    @property
    def diameter(self):
        return self.param_values[3]

    def calc_density(self):
        if self.param_values[4] == None:
            self.param_values[4] = float(self.tension) / (self.frequency * self.length * self.diameter)**2

    @property
    def density(self):
        return self.param_values[4]

    def get_missing_term(self):
        try:
            self.n_index = self.param_values.index(None)
        except ValueError:
            self.n_index = None
            print 'No missing term'
        else:
            print 'Missing term is %s...' % self.param_labels[self.n_index]
            try:
                self.param_funcs[self.n_index]()
            except Exception:
                print 'Need at least 4 out of 5 terms!'

    def print_info(self):
        for i in range(len(self.param_values)):
            print '%s: %s' % (self.param_labels[i], self.param_values[i])

def main():
    density_factor, tension, frequency, length, diameter = None, None, None, None, None
    
    parser = argparse.ArgumentParser(description='CLI tool for working with keyboard stringing')
    parser.add_argument('-m', '--material', type=str, help='String material', choices=['iron', 'yellow brass', 'red brass'])
    parser.add_argument('-t', '--tension', type=float, help='Tension in kg.')
    parser.add_argument('-f', '--frequency', type=float, help='Frequency in Hz.')
    parser.add_argument('-l', '--length', type=float, help='String length in meters.')
    parser.add_argument('-d', '--diameter', type=float, help='String diameter in meters.')
    parser.add_argument('-p', '--density', type=float, help='String density factor (density*pi/g)')

    args = parser.parse_args()
    if args.material:
        density_factor = DENSITY_MAP[args.material.lower()]
    if args.tension:
        tension = args.tension
    if args.frequency:
        frequency = args.frequency
    if args.length:
        length = args.length
    if args.diameter:
        diameter = args.diameter
    if args.density:
        density_factor = args.density

    s = String(tension=tension, frequency=frequency, length=length, diameter=diameter, density=density_factor)
    s.get_missing_term()
    s.print_info()

if __name__ == '__main__':
    main()

