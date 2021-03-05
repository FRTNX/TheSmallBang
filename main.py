import uuid

# Note: Using slots for subatomic namespaces for better memorey efficiency
class Photon:
    """iLLUMINATE"""

    __slots__ = '_photon_id',

    def __init__(self):
        """Initialise a new Photon instance


        """
        self._photon_id = str(uuid.uuid4())

    
class Proton:
    """The One"""

    __slots__ = '_proton_id', '_symbol', '_charge'

    def __init__(self):
        """Initialise a new Proton instance


        """
        self._proton_id = str(uuid.uuid4())
        self._symbol = 'p+'
        self._charge = 1


class Neutron:
    """The chargeless one"""

    __slots__ = '_neutron_id', '_symbol', '_charge'

    def __def__(self):
        """Initialise a new Neutron instance


        """
        self._neutron_id = str(uuid.uuid4())
        self._symbol = 'n0'
        self._charge = 0


class Electron:
    """Pikachu"""

    __slots__ = '_electron_id', '_symbol', '_charge', '_associated_atoms'

    def __init__(self):
        """Initialise a new Electron instance


        """
        self._electron_id = str(uuid.uuid4())
        self._symbol = 'e-'
        self._charge = -1
        self._associated_atoms = []

    def associate_atom(self, atom):
        self._associated_atoms.append(atom)

    def get_associated_atoms(self):
        return self._associated_atoms

    
class Atom:
    """An Atom"""

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
        self._phase = atomic_properties['phase'] # consider calculating from density
        self._electron_configuration = self._configure_electrons()
        self._valence = self._calculate_valence()
        self._period = atomic_properties['period']
        self._group = atomic_properties['group']
        self._atomic_radius = atomic_properties['atomic_radius']
        self._ionisation_potential = atomic_properties['ionisation_potential']
        self.accept_electrons(atomic_properties['electrons'])

    def __add__(self, atomic_additive):
        if self.is_octate() or atomic_additive.is_octate():
            raise AtomicError('Cannot bond with noble atom')

        # associate electrons to atoms
        # associate atoms to electrons

        self.share_electron(atomic_additive)
            
        return Molecule({ 'atomic_members': [self, atomic_additive] })

    # def __sub__(self) # this would remove electrons, protons, etc

    def __str__(self):
        return self._name

    def get_symbol(self):
        return self._symbol

    def get_electrons(self):
        return self._electron_configuration['configuration']

    def is_octate(self):
        return self._electron_configuration['is_octate_state']

    def share_electron(self, other_atom):
        sharable_electron = self._find_sharable_electron()
        if not sharable_electron:
            raise AtomicError('No sharable electrons found')

        return other_atom.accept_electrons([sharable_electron], True)

    # def donate_electron(self, atom)

    def accept_electrons(self, electrons, share=False):
        if self._electron_configuration['is_octate_state']:
            raise AtomicError('Cannot accept electrons when atom is noble')
            
        for electron in electrons:
            electron.associate_atom(self)

            if share:
                self._electrons.append(electron)
    
        self._electron_configuration = self._configure_electrons()

        return electrons
   
    def _find_sharable_electron(self):
        outermost_electrons = self._electron_configuration['configuration'][self._electron_configuration['outermost_shell']]
        for electron in outermost_electrons:
            if len(electron.get_associated_atoms()) == 1:
                return electron
        return None

    def _calculate_valence(self):
        # This will break when an atom has no electrons, TODO: some robustness here
        number_outermost_electrons = self._electron_configuration['format'][-1]
        if (self._electron_configuration['outermost_shell'] != 'K'):
            number_missing_electrons = 8 - number_outermost_electrons
            if number_missing_electrons > 4:
                return -(8 - number_missing_electrons)
            return number_missing_electrons

        return (2 - number_outermost_electrons)

    def _configure_electrons(self):
        electron_config = {
            'is_octate_state': None,
            'outermost_shell': None,
            'format': [],
            'configuration': {
                'K': [],
                'L': [],
                'M': [],
                'N': [],
                'O': [],
                'P': [],
                'Q': [],
                'R': []
            }
        }
         
        for electron in self._electrons:
            if len(electron_config['configuration']['K']) < 2:
                electron_config['configuration']['K'].append(electron)
                continue

            if len(electron_config['configuration']['L']) < 8:# This will break when an atom has no electrons, TODO: some robustness here
                electron_config['configuration']['L'].append(electron)
                continue

            if len(electron_config['configuration']['M']) < 8:
                electron_config['configuration']['M'].append(electron)
                continue

            if len(electron_config['configuration']['N']) < 8:
                electron_config['configuration']['N'].append(electron)
                continue

            if len(electron_config['configuration']['O']) < 8:
                electron_config['configuration']['O'].append(electron)
                continue

            if len(electron_config['configuration']['P']) < 8:
                electron_config['configuration']['P'].append(electron)
                continue

            if len(electron_config['configuration']['Q']) < 8:
                electron_config['configuration']['Q'].append(electron)
                continue

            if len(electron_config['configuration']['R']) < 8:
                electron_config['configuration']['R'].append(electron)
                continue

        for electron_shell in list(electron_config['configuration']):
            electron_count = len(electron_config['configuration'][electron_shell])
            if electron_count > 0:
                electron_config['format'].append(electron_count)

        # TODO: Test on atom with no electrons
        electron_config['outermost_shell'] = list(electron_config['configuration'])[len(electron_config['format']) -1]

        electron_config['is_octate_state'] = True if electron_config['format'][-1] in [2, 8] else False
        
        # TODO: Some serious code reduction here
        return electron_config


class Molecule:
    """An atomic cartel"""

    def __init__(self, molecular_properties):
        """Initialise a new Molecule instance


        """
        self._molecular_id = str(uuid.uuid4())
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
        counted = []
        empirical_formula = ''
        for atom in self._atomic_members:
            # print(self._atomic_members)
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
    'period': 1,
    'group': 'IA',
    'block': 's-block',
    'ionisation_potential': { 'value': 13.53, 'unit': 'eV' },
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
    'period': 2,
    'group': 'VIA',
    'block': 'p-block',
    'ionisation_potential': { 'value': 13.56, 'unit': 'eV' },
})


class AtomicError(Exception):
    """A generic error occuring at the atomic level"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class MolecularError(Exception):
    """Generic molecular level error"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    print('Atoms rule the world.')

# TODO: Consider how to create molecular intuition, e.g., avoiding rendering C02 as 02C
