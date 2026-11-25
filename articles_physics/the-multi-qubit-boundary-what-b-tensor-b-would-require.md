# __The Multi-Qubit Boundary: What $\mathbb{B}\otimes\mathbb{B}$ Would Require__

## Introduction

The informational sector carries one qubit, and it carries it exactly: the states are the points of the Bloch ball, the observables are the Hermitian elements, the channels are the $*$-unitary congruences, and the Born weight is one scalar part. The article asks what the same construction gives for two qubits, and the answer is a boundary rather than a generalisation.

The claim. The state of one system is an *element* of the algebra. The state of two systems is not: the composition of two informational sectors requires the tensor product $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$, and that algebra is $M_4(\mathbb{C})$, which is not a biquaternion algebra. So the second system takes the description out of the algebra and into a matrix algebra over a module, and what is lost is exactly the sector reading — the two slices, the one product and the one trace.

Three exact statements support it.

1. The one-system state space has three real parameters, the ball; the two-system state space has fifteen, the trace-one positive cone of $M_4(\mathbb{C})$. The algebra's own Hermitian slice has dimension four, so it cannot hold the fifteen.
2. The tensor product is central simple of degree four. $\mathbb{B}\cong M_2(\mathbb{C})$ as a complex algebra, so $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$, and no relabelling returns it to $M_2$.
3. The star extends to the tensor product, so the *involution* survives; what does not survive is the identification of the fixed space with a four-dimensional slice that carries a product. The two-slice structure becomes an eight-plus-eight splitting of a sixteen-dimensional real space, with no second product on either half.

What follows for the corpus's method. The higher-spin carriers are built as tensor powers of the spinor module, and that is the route that works: the object that composes is the *module*, not the element. The price is stated at the end, and it is the price the corpus already pays wherever it treats a many-body system.

The article uses [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) for the one-system construction, [The Two Sectors: the Hermitian Split and the Four Bridges](the-two-sectors-the-hermitian-split-and-the-four-bridges.html) for the slices, [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) for the module, and [The Biquaternion Universe as an Improvement of the Quaternionic Quantum Theory](the-biquaternion-universe-as-an-improvement-of-the-quaternionic-quantum-theory.html) for the tensor-product obstruction that the corpus already records.

## The One-Qubit State Space

Everything is one element. A state is $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ with $\lvert\vec s_\Psi\rvert<1$: three real parameters. An observable is a Hermitian element $\tilde A$, four real parameters, of which the trace part is a normalisation and the traceless part is three. A channel is a congruence by a $*$-unitary element, a group of four real parameters. And the weight is

$$
\langle\tilde A\rangle_{\tilde{Ϛ}_\Psi}=\mathrm{Sc}\left(\tilde{Ϛ}_\Psi\tilde A\right)=\tfrac12\left(\mathrm{Sc}\,\tilde A+\vec s_\Psi\cdot\vec a\right),
$$

one real number, bilinear in the state and the observable.

The counting matches, and that is why the construction closes. Three state parameters, three observable parameters after the trace is fixed, three channel parameters after the phase is quotiented out: the same three, and the same ball. The algebra is not a convenient notation for a two-level system; on one system it is the system.

**The density operator is an element, not a matrix.** $\tilde{Ϛ}_\Psi$ is an element of $\mathbb{B}_{\Psi}$, and its $2\times2$ image is a representative. The product $\tilde{Ϛ}_\Psi\tilde A$ is an element, and its scalar part is the weight. No column, no tensor index and no basis enters.

## The Tensor Product

What composition requires. Two systems, each with a state, compose to a state on the tensor product of their spaces. In the matrix language the state of two qubits is a positive trace-one operator on $\mathbb{C}^{2}\otimes\mathbb{C}^{2}=\mathbb{C}^{4}$, that is an element of $M_4(\mathbb{C})$'s Hermitian part, of real dimension sixteen with the trace constraint leaving fifteen. In the algebra's language the natural candidate is $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$.

What that algebra is. $\mathbb{B}$ is $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$, a central simple complex algebra of degree two. The tensor product of two central simple algebras of degrees $m$ and $n$ is central simple of degree $mn$, so

$$
\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C}),
$$

of complex dimension sixteen. The isomorphism is not a relabelling of the biquaternion algebra: $M_4(\mathbb{C})$ has no two-dimensional irreducible module, so it is not $M_2$ of anything, and it is not $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$.

**The obstruction is a class, not a convention.** In the Brauer group of $\mathbb{C}$ every central simple algebra is trivial, so the statement is the degree count above and nothing deeper; over $\mathbb{R}$ the same composition is the statement that the quaternion class has order two, so two copies of $\mathbb{H}$ are a matrix algebra over $\mathbb{R}$ and not a quaternion algebra. Either way the class is additive under the tensor product, and the one-system class plus itself is not the one-system class. **A second system doubles the degree, and the algebra of degree two exists only once.**

The star extends and the slices survive as a splitting. With $(\tilde Q\otimes\tilde Q')^{*}=\tilde Q^{*}\otimes\tilde Q'{}^{*}$ the involution is an anti-automorphism: the star of a product reverses the order in both factors and therefore reverses the order of the product. So the thirty-two-dimensional real algebra splits into a sixteen-dimensional Hermitian part and a sixteen-dimensional anti-Hermitian part, and the splitting is canonical. What is *not* canonical is a product on either part: the Hermitian part of $M_4(\mathbb{C})$ is not closed under multiplication, and neither is the anti-Hermitian part. The one-system algebra had a product that will be used; the two-system algebra has only the commutator and the anticommutator, which is the ordinary quantum-mechanical situation the corpus was built to avoid.

What a state would have to be. A state must be a positive element of trace one in the Hermitian part: fifteen parameters, of which the two "marginal" six are the two Bloch vectors and the remaining nine are the correlations. Those nine have no representative in $\mathbb{B}$: an element of the algebra has four, and a pair of elements has eight, and the ninth — the one that entanglement needs — is exactly the part that the tensor product adds and the algebra cannot supply.

## What the Algebra Would Have to Be

Requirement one: a degree-two algebra that is closed under the composition. None exists. The degree is multiplicative under the tensor product and the only degree-two central simple complex algebra is $M_2(\mathbb{C})$, so no composition of two systems stays inside the family. This is a theorem and not a limitation of the construction.

Requirement two: a real structure that selects a biquaternion factor. One can put a real structure on $M_4(\mathbb{C})$ and ask for the fixed algebra of an antilinear involution commuting with the star. The candidates are the real forms $M_4(\mathbb{R})$, $M_2(\mathbb{H})$ and $M_2(\mathbb{C})$ read over $\mathbb{R}$, and none of them is $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$: the first two have no complex scalar, and the third is the algebra of one system, of half the dimension required. A real structure can select *a* biquaternion subalgebra — $\mathbb{B}\otimes e_t$ is one — and that subalgebra acts on one factor only, which is the statement that one system's algebra can be recovered and the second cannot.

Requirement three: a product that the Born weight respects. The weight is the scalar part of a product, and the product must be defined on the state. In $M_4(\mathbb{C})$ the product of two states is a state only if they commute, and the scalar part is not positive on the whole cone. The one-system case works because the trace is the scalar part of a *single* product of two elements of a four-dimensional slice; the two-system case would need a four-dimensional slice whose product reproduces the fifteen-parameter cone, and no four-dimensional subspace of the sixteen does: a four-dimensional real subspace spans at most four of the fifteen generators.

**The three requirements are one statement.** A two-qubit system is not an element of a biquaternion algebra, and the reason is the dimension count of the second requirement read three ways. The corpus's own verdict on the quaternionic quantum theory — that consistency forces a complex structure and the composition objection is decisive — is the same fact at one level down, and it is recorded in the article on that programme.

## What the Corpus Does Instead

It composes modules, not elements. The higher-spin carriers are tensor powers of the spinor module, $S^{\otimes 2s}$, and the corpus already builds them. A two-qubit system is then a state on $S\otimes S=\mathbb{C}^{4}$, described by a density operator in $M_4(\mathbb{C})$, and the algebra enters through its action on the module and through the spin generators it supplies.

What survives that route. The Lorentz action, because it acts on each factor by the same rotor; the spin structure, because the generators are the algebra's; the Born weight, because it is a trace on the module; and the one-product advantage for each subsystem separately.

**What does not survive.** The identification of the state with an element; the reading of the trace as the doubled scalar part of one element; the sector vocabulary — a two-qubit state is not in a sector, because the tensor product's Hermitian part is not a sector of a biquaternion algebra; and the exceptional-point reading of the maximally mixed state, which becomes a property of $M_4$ and not of the algebra.

The price is stated, not hidden. For one system the corpus is not a notation for quantum mechanics; for two it is a notation for the Lorentz action on a many-body module, which is what everyone else has.

## Summary

The informational sector carries one qubit exactly, with three state parameters, four observable parameters and four channel parameters, all read from one product. Two qubits require the tensor product, and $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$: a central simple algebra of degree four, with a canonical eight-plus-eight splitting by the star and no product on either half. The state then has fifteen parameters, nine of which are correlations that no element of the algebra carries. No degree-two algebra is closed under composition, no real structure selects a biquaternion factor of the right size, and no four-dimensional subspace holds the cone. The corpus composes modules and not elements, and the sector reading stops at one system.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}\cong M_2(\mathbb{C})$ | the biquaternion algebra, central simple of degree two |
| $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$ | the two-system algebra, degree four |
| $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ | the one-system state, three parameters |
| $S=\mathbb{C}^{2}$ | the spinor module |
| $S\otimes S=\mathbb{C}^{4}$ | the two-system module |
| $15$ | the real dimension of the two-qubit state space after the trace constraint |
| $8\oplus 8$ | the Hermitian and anti-Hermitian parts of the two-system algebra |

## Further Reading

In this category. [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) is the one-system construction. [The Two Sectors: the Hermitian Split and the Four Bridges](the-two-sectors-the-hermitian-split-and-the-four-bridges.html) fixes the slices. [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) supplies the module and its tensor powers. [The Biquaternion Universe as an Improvement of the Quaternionic Quantum Theory](the-biquaternion-universe-as-an-improvement-of-the-quaternionic-quantum-theory.html) records the composition objection and the corpus's answer to it. [The Fubini–Study Geometry and the Biquaternion Norm](the-fubini-study-geometry-and-the-biquaternion-norm.html) is the one-system geometry that does not generalise by this route.

In the mathematics corpus. [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) supplies the product laws that the tensor product abandons.
