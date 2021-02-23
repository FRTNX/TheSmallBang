import uuid

# For subatomic physics, todo after atomic
class Photon:
    """iLLUMINATE"""

    def __init__(self):
        self._photon_id = str(uuid.uuid4())

    
class Proton:
    """The One"""

    def __init__(self):
        """Initialise an new Proton instance


        """
        self._proton_id = str(uuid.uuid4())
        self._symbol = 'p+'
        self._charge = 1


class Neutron:
    """The chargeless one"""

    def __def__(self):
        """Initialise an new Neutron instance


        """
        self._neutron_id = str(uuid.uuid4())
        self._symbol = 'n0'
        self._charge = 0


class Electron:
    """Pikachu"""

    def __init__(self):
        """Initialise an new Electron instance


        """
        self._electron_id = str(uuid.uuid4())
        self._symbol = 'e-'
        self._charge = -1


    
class Atom:
    """An atom, duh"""

    def __init__(self, atomic_properties):
        """Create a new Atom instance

        atomic id  the atoms unique identifier
        name       the atoms name
        ...
        """
        self._atomic_id = str(uuid.uuid4())
        self._protons = atomic_properties['protons']
        self._neutrons = atomic_properties['neutrons']
        self._electrons = atomic_properties['electrons']
        self._is_neutral = len(self._electrons) == len(self._protons)
        self._name = atomic_properties['name']
        self._symbol = atomic_properties['symbol']
        self._atomic_number = atomic_properties['atomic_number']
        self._atomic_weight = atomic_properties['atomic_weight']
        self._density = atomic_properties['density']
        self._atomic_radius = atomic_properties['atomic_radius']
        self._melting_point = atomic_properties['melting_point']
        self._boiling_point = atomic_properties['boiling_point']
        self._phase = atomic_properties['phase']
        self._valence = atomic_properties['valence']
        self._period = atomic_properties['period']
        self._group = atomic_properties['group']
        self._atomic_radius = atomic_properties['atomic_radius']
        self._ionisation_potential = atomic_properties['ionisation_potential']
        self._electronic_configuration = atomic_properties['electronic_configuration']

    def __add__(self, atomic_additive):
        return Molecule({ 'atomic_members': [self, atomic_additive] })

    # def __sub__(self) # this would remove electrons, protons, etc

    def __str__(self):
        return self._name

    def __len__(self):
        return self._atomic_radius * 2 # len(Atom) returns atomic diameter

    def get_symbol(self):
        return self._symbol


class Molecule:
   """An atomic cartel"""

    def __init__(self, molecular_properties):
        """Initialise an new Molecule instance


        """
        self.molecular_id = str(uuid.uuid4())
        self._atomic_members = molecular_properties['atomic_members']
        self._empirical_formula = self._calculate_emperical_formula()
        self._atomic_bonds = [
            { 'bond_type': 'covelent', 'members': [] },
            { 'bond_type': 'hydrogen', 'members': [] }
        ]

    # todo: support adding molecules to molecules
    def __add__(self, atomic_additive):
        atomic_members = self._atomic_members + [atomic_additive]
        return Molecule({ 'atomic_members': atomic_members })

    def __sub__(self, atomic_member):
        new_atomic_members = self._atomic_members.remove()  
        # return molecule with ammended memmbers

    def __contains__(self, atomic_member):
        return str(atomic_member) in self.list_atomic_members()

    def __len__(self):
        return len(self._atomic_members)

    def __getitem__(self, index):
        return self._atomic_members[index]

    def list_atomic_members(self):
        return [str(atom) for atom in self._atomic_members]

    def get_empirical_formula(self):
        return self._empirical_formula

    def _calculate_emperical_formula(self):
        counted = []        empirical_formula = ''
        for atom in self._atomic_members:
            print(self._atomic_members)
            if str(atom) not in counted:
                empirical_formula += f'{atom.get_symbol()}{self.list_atomic_members().count(str(atom))}'
                counted.append(str(atom))
        return empirical_formula.replace('1', '')



Hydrogen = Atom({
    'name': 'Hydrogen',
    'symbol': 'H',
    'atomic_number': 1,
    'protons': [ Proton() ],
    'neutrons': [ Neutron() ],
    'electrons': [ Electron() ],
    'atomic_weight': { 'value': 1.0079, 'unit': 'g/mol' },
    'density': { 'value': 0.0000899, 'unit': 'g/cm3' },
    'atomic_radius': { 'value': 53, 'unit': 'pm' },
    'covalent_radius': { 'value': 38, 'unit': 'pm' },
    'van_der_waals_radius': { 'value': 120, 'unit': 'pm' },
    'melting_point': { 'value': -259.1, 'unit': 'celcius' },
    'boiling_point': { 'value': -252.9, 'unit': 'celcius' },
    'phase': 'gas',
    'valence': 1,
    'period': 1,
    'group': 'IA',
    'block': 's-block',
    'ionisation_potential': { 'value': 13.53, 'unit': 'eV' },
    'electronic_configuration': { 'K': 1 }
})

Oxygen = Atom({
    'name': 'Oxygen',
    'symbol': 'O',
    'atomic_number': 8,
    'protons': [ Proton() for i in range(8) ],
    'neutrons': [ Neutron() for i in range(8) ],
    'electrons': [ Electron() for i in range(8) ],
    'atomic_weight': { 'value': 15.9994, 'unit': 'g/mol' },
    'density': { 'value': 0.00142897, 'unit': 'g/cm3' },
    'atomic_radius': { 'value': 48, 'unit': 'pm' },
    'covalent_radius': { 'value': 66, 'unit': 'pm' },
    'van_der_waals_radius': { 'value': 152, 'unit': 'pm' },
    'melting_point': { 'value': -218.4, 'unit': 'celcius' },
    'boiling_point': { 'value': -182.9, 'unit': 'celcius' },
    'phase': 'gas',
    'valence': -2,
    'period': 2,
    'group': 'VIA',
    'block': 'p-block',
    'ionisation_potential': { 'value': 13.56, 'unit': 'eV' },
    'electronic_configuration': { 'K': 1 }
})


class AtomicError(Exception):
    """A generic error occuring at the atomic level"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class MolecularError(Exception):
    """Generic molecular level error""""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    # tests
    print('Atoms rule the world.')

# TODO: Consider how to create molecular intuition, e.g., avoiding rendering C02 as 02C