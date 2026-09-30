# __The Dirac–Kähler Equation__

## Introduction

The **Dirac–Kähler equation** is the geometric analogue of the Dirac equation. Where the Dirac equation is an equation for a spinor field, the Dirac–Kähler equation is an equation for a field of **differential forms** — equivalently, a multivector field — and it is defined on any pseudo-Riemannian manifold using only the exterior calculus. In four-dimensional flat spacetime it is equivalent to **four copies** of the Dirac equation that transform into each other under the Lorentz group; in curved spacetime the equivalence fails, and the equation becomes a modified Dirac equation that is no longer the square root of the Laplace operator. Because its field is a multivector, it has a natural discretization on a simplicial complex, and that discretization is exactly the **staggered fermion** formulation of lattice field theory. The equation was written down by Ivanenko and Landau in 1928 and rediscovered by Kähler in 1962; it is also called the **Ivanenko–Landau–Kähler equation**.

The article is a self-contained treatment of the equation and its structure. The next section fixes the exterior calculus and the Laplace–de Rham operator. The third introduces the Clifford product on forms that makes the operator a geometric square root. The fourth states the equation and its square. The fifth carries out the decomposition into four Dirac equations through the explicit basis change. The sixth adds minimal coupling. The seventh gives the simplicial discretization and its equivalence to staggered fermions. The eighth treats the zero modes and their index-theoretic meaning. The ninth treats the curved-space failure of the fourfold decomposition. The tenth states the relation to the biquaternion algebra of the companion articles — including the precise reason the Dirac–Kähler field is *not* a biquaternion field in the framework's sense. The closing sections are the summary, the notation table and the literature.

## Differential Forms and the Laplace–de Rham Operator

Let $M$ be a four-dimensional (pseudo-)Riemannian manifold with metric $g$ and local coordinates $x^\mu$, $\mu=1,\dots,4$. A **differential form of degree $h$** is a totally antisymmetric tensor field $\Phi_{\mu_1\dots\mu_h} = \Phi_{[\mu_1\dots\mu_h]}$, and a general form field is a sum over the sixteen ordered index sets $H$,

$$
\Phi = \sum_H \Phi_H(x)\,dx_H,
\qquad
dx_H = dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_h},
\qquad
\mu_1<\cdots<\mu_h .
$$

The field therefore has $2^4 = 16$ scalar components in four dimensions: one scalar, four vectors, six bivectors, four trivectors and one pseudoscalar. The **exterior derivative** $d$ raises the degree by one, $d: \Omega^h \to \Omega^{h+1}$, and satisfies $d^2 = 0$. The **codifferential** $\delta$ lowers the degree by one, $\delta: \Omega^h\to\Omega^{h-1}$, and is defined through the **Hodge star** $\star$ by

$$
\delta = -\star\, d\, \star ,
\qquad
\delta^2 = 0 .
$$

Their sum $d - \delta$ is the **Laplace–de Rham operator**. It is the square root of the Laplacian, in the sense that

$$
(d-\delta)^2 = -(d\delta + \delta d) = \square ,
$$

where $\square$ is the Laplace–de Rham (Laplace–Beltrami) operator; on functions of flat Euclidean space it reduces to $-\sum_\mu\partial_\mu^2$ up to sign, and on functions of Minkowski space to the d'Alembertian. This is the property that motivates the equation: the Dirac operator is also a square root of the Laplacian, and $d-\delta$ is its geometric counterpart.

## The Clifford Product on Forms

To see the operator act like a Clifford multiplication, introduce on the basis forms a new product $\vee$ defined by

$$
dx_\mu \vee dx_\nu = dx_\mu \wedge dx_\nu + \delta_{\mu\nu} .
$$

Because the wedge product is antisymmetric and the added term is symmetric, this product satisfies the Clifford relation

$$
\{dx^\mu, dx^\nu\}_\vee = 2\,\delta^{\mu\nu},
$$

so that the exterior algebra, equipped with $\vee$, is the Clifford algebra of the Euclidean form. With this product the Laplace–de Rham operator on a form field is

$$
(d-\delta)\Phi(x) = dx^\mu \vee \partial_\mu\Phi(x),
$$

which is the familiar form $c(dx^\mu)\partial_\mu$ of a Dirac-type operator, with the forms themselves playing the role of the Clifford generators. In Lorentzian signature the relation acquires a sign from the metric, as in *The Volume Element, Duality and the Hodge Star*; the Euclidean statement above is the one used for the lattice construction, and the Lorentzian version differs only in the signature of the Clifford relation.

## The Equation

The **Dirac–Kähler equation** is

$$
(d-\delta+m)\,\Phi = 0 .
$$

Applying the operator $d-\delta-m$ on the left and using $(d-\delta)^2 = \square$ gives

$$
\left(\square - m^2\right)\Phi = 0 ,
$$

so that every component of the multivector field satisfies the Klein–Gordon equation of the same mass. This is the same second-order consequence that the Dirac equation has, and it holds for the same reason: the first-order operator squares to the wave operator. The equation is a first-order system of coupled partial differential equations of Dirac type; its principal symbol is the Clifford multiplication, so it is elliptic in the Euclidean signature and hyperbolic in the Lorentzian one.

## Decomposition into Dirac Equations

The equivalence to four Dirac equations is proved by an explicit change of basis. Define the matrix-valued form

$$
Z_{ab} = \sum_H (-1)^{h(h-1)/2}\,(\gamma_H)^T_{ab}\, dx_H ,
$$

in which $(\gamma_H)_{ab}$ are the products of the Dirac matrices indexed by $H$ and $h$ is the degree of $H$. The matrix $Z$ is constructed so that

$$
dx_\mu \vee Z = \gamma_\mu^T Z ,
$$

which decomposes the Clifford product into **four irreducible copies** of the Dirac algebra: in this basis the product only mixes the column indices $a$. Writing the field in the new basis,

$$
\Phi = \sum_{ab}\Psi(x)_{ab}\,Z_{ab},
$$

the Dirac–Kähler equation becomes four Dirac equations, one for each value of the unimpaired index $b$,

$$
\left(\gamma^\mu\partial_\mu + m\right)\Psi(x)_b = 0 .
$$

Thus in flat spacetime the sixteen components of the multivector arrange into four four-component spinors, and the four copies transform into one another under the Lorentz group. The mechanism is an **internal symmetry** $\mathrm{SO}(2,4)$ acting on the multivector; its parameters are tensors rather than scalars, and it does not commute with the Lorentz transformations. Consequently the Lorentz group does not act independently on the four Dirac fields: it mixes components of different degrees, and the "spin-$\tfrac12$" fields are not strict half-integer representations of the Clifford algebra but coherent superpositions of forms of different degree. In $2^{2^n}$ dimensions the equation is equivalent to $2^{2^{n-1}}$ Dirac equations; in particular it is the four-dimensional case $d=4=2^2$ that gives the factor four used above.

## Minimal Coupling

Coupling to a gauge field replaces the ordinary derivative by the covariant one, $dx^\mu\vee\partial_\mu \to dx^\mu\vee D_\mu$, and the equation acquires a source:

$$
(d-\delta+m)\Phi = iA\vee\Phi ,
$$

with the components of $A$ agreeing with the four-potential. In the abelian case $A = eA_\mu dx^\mu$; in the non-abelian case there are additional internal indices. The Dirac–Kähler field then carries those indices, and formally corresponds to sections of the Whitney product of the Atiyah–Kähler bundle of differential forms with the vector bundle of local internal spaces. As in the flat uncharged case, the coupled equation is again equivalent to four copies of the corresponding coupled Dirac equation.

## Discretization and Staggered Fermions

The exterior algebra corresponds to a simplicial complex, and this is what makes the equation naturally discretizable. A lattice is a simplicial complex whose $h$-simplices are the $h$-dimensional hypercubes $C^{(h)}_{x,H}$; an $h$-chain is a formal sum $C^{(h)} = \sum_{x,H}\alpha_{x,H}C^{(h)}_{x,H}$. The chain complex carries a **boundary** operator $\Delta$ lowering the degree and a **coboundary** operator $\nabla$ raising it. The dual objects, $h$-cochains $\Phi^{(h)}(C^{(h)})$, are linear functionals on chains, and the dual boundary and coboundary are defined by

$$
(\hat\Delta\Phi)(C) = \Phi(\Delta C),
\qquad
(\hat\nabla\Phi)(C) = \Phi(\nabla C).
$$

Under the exterior-algebra/simplicial-complex correspondence, differential forms become cochains and the exterior derivative and codifferential become the dual boundary and coboundary. The Dirac–Kähler equation on the lattice is then

$$
(\hat\Delta - \hat\nabla + m)\,\Phi(C) = 0 .
$$

The resulting discrete field is equivalent, by an explicit change of basis, to the **staggered fermion** of lattice field theory; hence the continuum Dirac–Kähler field is the formal continuum limit of the staggered fermion. This is the mathematical reason the multivector form is the natural home of the staggered discretization, and it is the fact the companion article *Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form* draws on. The discretization reduces the number of doubler species but does not eliminate them: the Nielsen–Ninomiya obstruction applies to the discretized Dirac–Kähler theory as to any other local, hermitian lattice fermion.

## Zero Modes and Their Index

The Dirac–Kähler operator has a distinctive feature in its zero modes. On a compact manifold, the equations $d\Phi = 0$ and $\delta\Phi = 0$ define the **harmonic forms**, and they exist whenever the relevant **Betti numbers** do not vanish: a nonzero cohomology class always contains a harmonic representative. Consequently the massless Dirac–Kähler operator always has zero modes on any compact manifold with nonzero Betti numbers, in contrast to the Dirac operator, which may have no zero modes at all on a positively curved manifold. The two operators therefore have different index-theoretic behaviour, even though they agree in flat spacetime: the Dirac–Kähler index is a topological datum of the manifold's cohomology, and the Dirac index is the Atiyah–Singer index of a spin Dirac operator. The companion article on fermion doubling records the two index facts that touch the biquaternion framework, the harmonic-form zero modes here and the anomalous Landau level at the Dirac point in graphene.

## Curved Spacetime

In curved spacetime the fourfold decomposition fails. The Dirac–Kähler equation remains a single equation for a multivector field, but it no longer splits into four independent Dirac equations, because the curvature couples the internal $\mathrm{SO}(2,4)$ symmetry to the geometry. What survives is the defining property: the operator is still the square root of the Laplace–de Rham operator, and hence still a **modified** Dirac operator, a property not shared by the ordinary Dirac equation in curved spacetime (whose square acquires the spin-curvature term of the Lichnerowicz formula). Preserving the square-root property in curved space costs Lorentz covariance: the departures are suppressed by powers of the Planck mass, so they are invisible at accessible energies but present in principle. The zero-mode statement also survives: the harmonic forms exist by cohomology, independently of the metric in its cohomology class.

## Relation to the Biquaternion Algebra

The biquaternion algebra of the companion articles is the **even part** of the real Clifford algebra $\mathrm{Cl}_{1,3}$,

$$
\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong \mathrm{Cl}_{1,3}^{+} ,
$$

an eight-real-dimensional algebra whose two minimal left ideals are the framework's left and right Weyl spinors. The Dirac–Kähler field is a **full** multivector of $\mathrm{Cl}_{1,3}$, sixteen complex components, of which the even-grade part — one scalar, six bivectors, one pseudoscalar — is eight complex components and can be read as a pair of biquaternion fields. The relation is therefore one of **containment**, not identity: the biquaternion field is the even part of a Dirac–Kähler multivector, and the Dirac–Kähler field carries the odd part as well.

This containment does not turn the Dirac–Kähler equation into a biquaternion equation. The operator $d-\delta$ is **odd**: the exterior derivative raises the degree and the codifferential lowers it, so $(d-\delta+m)\Phi=0$ couples the even and odd parts of $\Phi$ and does not restrict to either. A biquaternion-valued field alone does not satisfy the Dirac–Kähler equation; one must carry the odd components too. What the containment does give is a natural statement of *why* the framework's equation and the Dirac–Kähler equation are two readings of one geometric object: both are square roots of a Laplacian, and both are built from $\mathrm{Cl}_{1,3}$; the framework takes a minimal left ideal of the even part and calls it the Dirac field, while the Dirac–Kähler construction takes the whole multivector and recovers four Dirac fields from it by the basis change $Z$. The corpus's statement that spinors are minimal left ideals and the Dirac–Kähler decomposition into four copies are the two extremes of the same Clifford structure, and their precise dictionary — which of the four Dirac–Kähler copies corresponds to the framework's field — is not fixed in the corpus and is collected among the open questions.

## Summary

The Dirac–Kähler equation $(d-\delta+m)\Phi=0$ is the geometric analogue of the Dirac equation: it is an equation for a multivector field, defined on any pseudo-Riemannian manifold by the exterior calculus alone. The Laplace–de Rham operator $d-\delta$ is a square root of the Laplacian, $(d-\delta)^2=\square$, and the equation therefore implies the Klein–Gordon equation $(\square-m^2)\Phi=0$ componentwise. Equipping the exterior algebra with the Clifford product $dx_\mu\vee dx_\nu = dx_\mu\wedge dx_\nu + \delta_{\mu\nu}$ makes $d-\delta$ the Clifford multiplication $dx^\mu\vee\partial_\mu$.

In four-dimensional flat spacetime the basis change $Z_{ab}=\sum_H(-1)^{h(h-1)/2}(\gamma_H)^T_{ab}dx_H$ turns the equation into four Dirac equations linked by an internal $\mathrm{SO}(2,4)$ symmetry that does not commute with the Lorentz group; the four copies are coherent superpositions of forms of different degree. Minimal coupling adds the gauge field through $dx^\mu\vee D_\mu$, and the coupled equation is again four coupled Dirac equations. The natural discretization on a simplicial complex is equivalent to the staggered fermion, making the continuum Dirac–Kähler field the continuum limit of the staggered lattice fermion; the Nielsen–Ninomiya obstruction still applies. The zero modes are the harmonic forms, guaranteed by cohomology and in contrast to the Dirac operator. In curved spacetime the fourfold split fails, and what survives is the square-root property, at the cost of Lorentz covariance suppressed by powers of the Planck mass. Finally, the biquaternion algebra is the even part of $\mathrm{Cl}_{1,3}$ and is contained in the Dirac–Kähler multivector, but the Dirac–Kähler operator is odd and does not restrict to a biquaternion equation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi=\sum_H\Phi_H dx_H$ | Multivector field; sums over the sixteen ordered index sets |
| $d$, $\delta$ | Exterior derivative and codifferential, $\delta=-\star d\star$ |
| $d-\delta$ | Laplace–de Rham operator, $(d-\delta)^2=\square$ |
| $\square$ | Laplace–de Rham (Laplace–Beltrami) operator |
| $dx_\mu\vee dx_\nu = dx_\mu\wedge dx_\nu+\delta_{\mu\nu}$ | Clifford product on forms |
| $Z_{ab}$ | Basis change to four Dirac copies |
| $\gamma_H$ | Products of Dirac matrices indexed by $H$ |
| $\mathrm{SO}(2,4)$ | Internal symmetry mixing the four copies |
| $A = eA_\mu dx^\mu$ | Abelian gauge potential, minimally coupled |
| $\Delta,\nabla,\hat\Delta,\hat\nabla$ | Boundary, coboundary and their duals |
| $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$ | Biquaternion algebra as the even part |

## Further Reading

- D. Iwanenko and L. Landau, "Zur Theorie des magnetischen Elektrons I," *Zeitschrift für Physik* **48** (1928) 340–348, for the original equation.
- E. Kähler, "Der innere Differentialkalkül," *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **25** (1962) 192–205, for the rediscovery and the inner calculus.
- W. Graf, "Differential forms as spinors," *Annales de l'Institut Henri Poincaré A* **29** (1978) 85–109, for the Clifford module and the bundle structure.
- P. Becher and H. Joos, "The Dirac–Kähler equation and fermions on the lattice," *Zeitschrift für Physik C* **15** (1982) 343–365, for the simplicial discretization and the equivalence to staggered fermions.
- T. Banks, Y. Dothan and D. Horn, "Geometric fermions," *Physics Letters B* **117** (1982) 413–417, for the curved-spacetime behaviour.
- Y. N. Obukhov and S. N. Solodukhin, "Dirac equation and the Ivanenko–Landau–Kähler equation," *International Journal of Theoretical Physics* **33** (1994) 225–245, for the comparison with the Dirac equation.
- S. I. Kruglov, "Dirac–Kähler equation," *International Journal of Theoretical Physics* **41** (2002) 653–687, for a review of the algebraic structure and the Lorentz mixing.
- I. Montvay and G. Münster, *Quantum Fields on a Lattice* (Cambridge University Press, 1994), chapter 4, for the lattice construction in the standard notation.
- The companion articles of this series: *Dirac Differential Operators*, *Geometric Calculus and the Vector Derivative*, *The Volume Element, Duality and the Hodge Star*, *Spinors as Minimal Left Ideals*, and *Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form*.
