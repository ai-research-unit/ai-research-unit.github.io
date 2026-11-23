# __The Gauge Carrier of the Material Sector: Why the Action Is One-Sided__

## Introduction

The carrier exists, and it is a side. The matter field of this framework is an element of the algebra, and the gauge action on it is left multiplication. That single fact decides everything else: what the carrier is, what the action preserves, and why the sector has a carrier but not a chiral one.

The three results, and where they live. Each is stated in a mathematics article: the left family is multiplicative in its parameter, in [One-Sided Operators on a Clifford Algebra](../articles_maths/one-sided-operators-on-a-clifford-algebra.html); the single operator is not an endomorphism, in [The Signed Left Multiplication on a Ring](../articles_maths/the-signed-left-multiplication-on-a-ring.html); the left action on the spin group is the spin representation on a minimal left ideal, in [The One-Sided Action and the Spin Representation](../articles_maths/the-one-sided-action-and-the-spin-representation.html). A physics reader looking for the carrier of matter will not search the mathematics part, and this article collects the three where that reader will look.

The fourth result. A discrimination by the trace, which separates the two things a unit quaternion can do: rotate an element by conjugation, or carry it by left multiplication. The two are exact opposites in what they preserve, and the trace is the shortest way to see it.

## The Carrier Is a Minimal Left Ideal

Why an ideal and not a subspace. The gauge action is left multiplication, so the carrier must be closed under it. A left ideal is exactly a subspace closed under left multiplication, and a *minimal* left ideal is one with no proper such subspace. The carrier is therefore minimal by the demand that the representation be irreducible.

Its dimension. For $\mathbb{B}\cong M_2(\mathbb{C})$ the minimal left ideals have complex dimension two, so the carrier is $\mathbb{C}^2$ as a complex vector space. This is the spinor module, and the spin representation is what acts on it.

The rotor picture: turning a frame and carrying a module. A unit real quaternion — an element of $SU(2)$, which in this algebra is $\mathrm{SU}(2)=\mathrm{Spin}(3)$, the double cover of the spatial rotations — does two different things and the difference is the whole of this article. It can turn, which is the Hermitian pair $\mathrm{Sd}_{\tilde u}(\vec v)=\tilde u\vec v\tilde u^{*}$ on the vector part — a two-sided map, a similarity, the spatial rotation. Or it can carry, which is left multiplication $L_{\tilde u}$, a one-sided map on a module. A frame is turned; a matter field is carried. So the one-sidedness below is not a deficiency of the construction that a better construction would remove: it is the difference between the two maps, and only the second is available for a module. The names are fixed in [Representation Is a Function of Spin](representation-is-a-function-of-spin.html).

**Why one side and not two.** A right multiplication does not preserve a left ideal: $(\psi a)$ need not lie in $I$ when $\psi$ does. So the action that carries the ideal is one-sided by necessity, and a two-sided action on a minimal ideal is not available. That is the structural reason the framework's matter coupling is a left multiplication and cannot be made symmetric in the two sides.

## First Result: the Left Family Is Multiplicative in Its Parameter

The statement. For elements $a,b$ of the algebra, $L_a\circ L_b=L_{ab}$. The map $a\mapsto L_a$ is therefore multiplicative: it is a representation of the algebra on itself, the regular one.

Why it matters. A gauge transformation must compose as the group composes. Because the parameter multiplies, a product of two gauge transformations is the gauge transformation of the product parameter, and the coupling can be written as a single element multiplying the field. This is what makes $D_{\imath}\tilde\Xi=\partial/\partial R_{\imath}\tilde\Xi+i\kappa\,\mathcal{A}_{\imath}\tilde\Xi$ a covariant derivative rather than a formal symbol.

**What it does not say.** That the left family is multiplicative does not make it an *algebra* endomorphism. The two statements are different, and the difference is the second result.

## Second Result: the Single Operator Is Not an Endomorphism

The statement. $L_a(xy)=a\,xy$, whereas $L_a(x)L_a(y)=a\,x\,a\,y$. The two agree only when $a$ is central. So $L_a$ is a linear map of the algebra to itself, multiplicative in its parameter, and not a homomorphism of the algebra's own product.

Consequence for the group. Restricted to the unit elements, left multiplication gives a group acting on a module. It does not give a group of automorphisms of the algebra. A symmetry in the automorphism sense — one that preserves the algebraic structure, hence both sectors and the star — is conjugation, and conjugation is not what the gauge field does.

**This is the technical form of the sector's central claim.** A gauge field in a non-central generator acts on matter by an operator that is not an automorphism, so the "internal symmetry" reading fails at the level of the definition and not at the level of the physics. The field is a connection on a module, and the geometric reading follows: a connection in the adjoint of $\mathrm{Spin}(3)$ is the spatial part of a spin connection.

## Third Result: the Left Action Is the Spin Representation

The statement. Restricted from the algebra to the spin group, the left multiplication is the representation that carries the spinors. It is irreducible, because the ideal is simple, and its commutant is a division algebra, because the module is simple.

Why the word "spin" is not decorative. The representation a field carries is fixed by its spin, since the group is the spin group. The carrier is therefore not a choice among representations; it is the module the algebra has for spin half, and [Representation Is a Function of Spin](representation-is-a-function-of-spin.html) states the same fact for the three spins at once.

## The Trace Discriminator

Two actions of one element. A unit quaternion $\tilde Q$ can rotate an element, $\tilde QX\tilde Q^{-1}$, or carry it, $\tilde QX$. Both are linear, both are invertible, and they are not the same operation.

| Property | Conjugation $\tilde QX\tilde Q^{-1}$ | Left product $\tilde QX$ |
|---|---|---|
| multiplicative in the pair | yes, an inner automorphism | no, not an endomorphism |
| preserves the trace | yes | no |
| preserves the star | yes | no |
| preserves Hermiticity | yes | no |

The numbers. Over two thousand random elements and random rotors the trace is preserved by conjugation to a residual of $2\times10^{-15}$, while the left product returns a trace that is generically nonzero — of order one on a normally distributed element. The star is preserved by conjugation for every unitary $\tilde Q$, and never by the left product unless the element is central.

**Why the trace and not something else.** It is the shortest invariant that separates the two, and it separates them exactly: the trace of a commutator vanishes, so any conjugation preserves it, while the left product changes it whenever the multiplier is non-central. The discriminator is therefore a proof and not a numerical accident.

## What the Carrier Supplies and What It Does Not

- Supplied. A carrier for spin-half matter, irreducible and uniquely determined; a gauge action that composes; and the trace criterion that identifies it as a module action rather than an automorphism.
- Imported. Nothing. The three results are computations about the algebra.
- Not supplied. A chiral carrier. Because the action is left multiplication and left multiplication ignores the letter, both chiral values are carried by one module and acted on by one matrix. The carrier is therefore vector-like, and [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) records the consequence.

The one-sentence form. The material sector has a carrier, the carrier is a minimal left ideal, the action is left multiplication, and an action that is one-sided cannot be chiral.

## Where the Alternative Filing Is

The corpus files the three results in `articles_maths/`, and that is correct for the mathematics. It is wrong for the reader: the carrier of matter is a physics object, and a physicist who wants to know what the matter field is carried by should not have to find [The One-Sided Action and the Spin Representation](../articles_maths/the-one-sided-action-and-the-spin-representation.html) by search. This article is the pointer, and it adds nothing that the three do not already contain.

Why a pointer and not a rewrite. Because the mathematics articles state the results with their proofs, and a second proof would be a second thing to keep true. The physics article states the results, names the articles that prove them, and draws the consequence for the sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $I=\mathbb{B}\pi$ | a minimal left ideal, the carrier |
| $\rho_I$ | the one-sided action, $\rho_I(x)\psi=x\psi$ |
| $L_a$, $R_a$ | left and right multiplication by $a$ |
| $\tilde Q$ | a unit real quaternion, an element of the spin group |
| $\tilde QX\tilde Q^{-1}$ | conjugation, the automorphism |
| $\tilde QX$ | the left product, the module action |

## Further Reading

- [The One-Sided Action and the Spin Representation](../articles_maths/the-one-sided-action-and-the-spin-representation.html), for the spin representation on a minimal left ideal.
- [The Signed Left Multiplication on a Ring](../articles_maths/the-signed-left-multiplication-on-a-ring.html), for the twisted homomorphism and the failure of endomorphism.
- [Operators Acting on One Side](../articles_maths/one-sided-operators-on-a-clifford-algebra.html), for the two one-sided families and their overlap in the scalars.
- [Polar Decomposition of Quaternions](../articles_maths/polar-decomposition-of-quaternions.html), for the rotor acting on pure quaternions by the two-sided operator.
