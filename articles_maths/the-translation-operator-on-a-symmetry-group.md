
# __The Translation Operator on a Symmetry Group__

## Introduction

A symmetry group acts on its space and on itself, and the **translation operator** by $a$ is the operator of the action of $a$ on the group: on a function on the group it is

$$
(T_a f)(x) = f(a^{-1}x),
$$

so that $T_a T_b = T_{ab}$ and the translations are a representation of $G$, the left regular representation restricted to the acting side. The translation operators are the elementary operators from which the left multiplications of *Operators on a Symmetry Group* are made, and their two properties are what the present article isolates: **invariance** — the translations commute with the right translations, so the algebra they generate is the natural invariant operator algebra of the group — and **ergodicity**, which is a property of the translation flow only after a quotient by a lattice has been taken, and which is then a genuine geometric property of the lattice.

The lattice enters because a symmetry group of a space carries discrete subgroups, and the quotient of the group by a lattice is a finite-volume locally symmetric space whose geometry is the orbit structure of the translations. The translation flow on the quotient is the geodesic or the horocycle flow of that space, and its ergodicity — the absence of invariant sets of intermediate measure — is a theorem of Part III, cited and not proved here: the ergodic theory of group actions is *Ergodic Theory of Group Actions* and *Homogeneous Dynamics*, the equidistribution and the classification of the orbit closures of the unipotent flows are *Equidistribution* and *Ratner's Theorems*, and the measure is the Haar measure of *Locally Compact Groups and Haar Measure*. The left and right regular representation is *The Left and Right Regular Representation*, Part III; the lattices and the finite-volume quotients are *Transformation Groups* and *Riemannian Symmetric Spaces and the Involution*; and the locally symmetric space the lattice defines is *Riemannian Symmetric Spaces and the Involution*, "Locally Symmetric Spaces and Holonomy". None of it is re-derived.

The article has five sections: the translation operators and their invariance; the lattice and the quotient; the ergodicity of the translation flow; the examples; and the boundary with the analysis of Part III. Throughout, $G$ is a locally compact group, $dg$ a left Haar measure, $\Gamma \leq G$ a lattice, and $T_a$ the translation operator by $a$.

## The Translation Operators and Their Invariance

### The Operators

**Definition.** The **translation operator** by $a \in G$ acts on the functions on $G$ by

$$
(T_a f)(x) = f(a^{-1}x),
$$

and on the functions on a quotient $G/\Gamma$ by $(T_a f)(x\Gamma) = f(a^{-1}x\Gamma)$; it is the operator of left translation, and $a \mapsto T_a$ is the left regular representation of $G$ on the function space. The **right translation** $S_b f(x) = f(xb)$ is the corresponding operator of the right action.

**Proposition.** The translation operators form a representation, $T_a T_b = T_{ab}$, and the right translations form another, $S_a S_b = S_{ab}$; the two commute, $T_a S_b = S_b T_a$, and the inverse relations $T_a^{-1} = T_{a^{-1}}$, $S_b^{-1} = S_{b^{-1}}$ hold. On $L^2(G)$ the operators $T_a$, $S_b$ are isometries for the left and right Haar measures, and they are unitary for a bi-invariant measure when $G$ is unimodular.

**Proof.** The composition and inverse rules are immediate; the commutation is associativity, $T_a S_b f(x) = f(a^{-1}xb) = S_b T_a f(x)$; the isometry statements are the invariance of the Haar measure under left and right translation, and the unitary case is the definition of unimodularity.

### Invariance and the Commutant

**Definition.** An operator on the functions on $G$ is **translation-invariant** (or **right-invariant** in the usual convention) when it commutes with every left translation, $A T_a = T_a A$ for all $a$; such operators are the operators that the group's own translations cannot tell apart.

**Proposition.** The operators commuting with all left translations are exactly the **right convolutions**: the operator $A$ is translation-invariant if and only if there is a distribution or measure $\mu$ with

$$
A f(x) = \int_G f(xy)\,d\mu(y) = (f * \mu)(x),
$$

so that the algebra of translation-invariant operators is the convolution algebra of measures on $G$, *The Involution on the Measure Algebra* and *Convolution on a Group*. In particular every translation-invariant operator commutes with every right translation and the algebra is commutative exactly when $G$ is abelian.

**Proof.** If $A$ is translation-invariant then for each $x$ the functional $f \mapsto (Af)(x)$ is a distribution $\mu_x$ supported at $x$ — the invariance forces $\mu_x = \delta_x * \mu$ to be a translate of a single distribution $\mu$, so $Af = f * \mu$; conversely a right convolution commutes with the left translations by associativity and invariance of the measure. The commutativity in the abelian case is the commutativity of convolution there.

**Remark (the abelian picture).** When $G$ is abelian, the translation operators are simultaneously diagonalised by the characters: on the group algebra, $\hat T_a(\chi) = \chi(a)^{-1}$, and $T_a$ is multiplication by this character in the Fourier basis; the algebra of translation-invariant operators is the algebra of Fourier multipliers, diagonal in the character basis, and its elements are the operators of *Convolution Operators* and *Involutions of the Convolution Operators*. The non-abelian case replaces the characters by the irreducible representations, and the algebra of translation-invariant operators by the Fourier algebra; the representation theory is *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*.

## The Lattice and the Quotient

### Lattices

**Definition.** A **lattice** in a locally compact group $G$ is a discrete subgroup $\Gamma \leq G$ of finite covolume, meaning that the quotient $G/\Gamma$ carries a $G$-invariant measure of finite total mass; the lattice is **cocompact** (or uniform) when $G/\Gamma$ is compact, and nonuniform otherwise. The invariant measure on $G/\Gamma$ is the Haar measure normalised so that the total volume is one, and it is the **normalised invariant measure**.

**Proposition.** The quotient $G/\Gamma$ is a $G$-space for the left translations, the projection $G \to G/\Gamma$ is a covering map when $\Gamma$ is discrete and torsion-free, and the invariant measure of $G/\Gamma$ is the pushforward of the Haar measure under the projection. If $G$ is a Lie group and $\Gamma$ cocompact, $G/\Gamma$ is a compact manifold; if $G$ is semisimple and $\Gamma$ torsion-free, $G/\Gamma$ is the frame bundle of the locally symmetric space $\Gamma\backslash G/K$.

**Proof.** The quotient by a discrete subgroup is a covering of a neighbourhood of the identity coset; the pushforward measure descends because the Haar measure is invariant under right translation by $\Gamma$, and the total mass is finite by the definition of a lattice; the identification of the locally symmetric space is the general quotient theory of *Transformation Groups*.

### The Quotient as a Geometric Space

**Definition.** When $G$ is a semisimple Lie group and $X = G/K$ a symmetric space, the lattice $\Gamma$ acts on $X$ by isometries and the quotient $\Gamma\backslash X = \Gamma\backslash G/K$ is the **locally symmetric space** of *Riemannian Symmetric Spaces and the Involution*: it is complete, of finite volume when $\Gamma$ is a lattice, and its universal cover is the symmetric space $X$.

**Remark.** The geometry is the point of the lattice. The translation operator on $G$ descends to the quotient $G/\Gamma$, and on the bundle $G/\Gamma \to \Gamma\backslash X$ it is a flow over the locally symmetric space: the flow of the one-parameter group $\{a_t\}$ is the geodesic flow when $\{a_t\}$ is the full Cartan subgroup and the horocycle flow when $\{a_t\}$ is unipotent. The locally symmetric space and its finite volume are the geometric data; the translation flow is the operator.

## The Ergodicity of the Translation Flow

### Ergodicity

**Definition.** A measurable action of $G$ on a probability space $(Y, \mu)$ preserving $\mu$ is **ergodic** when every measurable invariant subset has measure $0$ or $1$; equivalently, when the only invariant measurable functions are the constants. It is **mixing** when $\mu(A \cap T_a^{-1}B) \to \mu(A)\mu(B)$ as $a \to \infty$ along a suitable exhaustion, and mixing implies ergodic.

**Proposition.** For the translation action of $G$ on $G/\Gamma$ with the normalised invariant measure, ergodicity is equivalent to the absence of nonzero invariant vectors in the representation of $G$ on the space $L^2_0(G/\Gamma)$ of functions of mean zero; equivalently, every nonzero $f \in L^2(G/\Gamma)$ satisfying $T_a f = f$ for all $a$ is constant.

**Proof.** An invariant measurable set has an indicator, a bounded invariant function; conversely an invariant function has level sets that are invariant, so the two formulations agree, and orthogonality of the invariant functions to the constants is the restriction to mean zero. This is the bilinear form of the mean ergodic theorem, *Ergodic Theory of Group Actions*.

### The Ergodicity Criterion for a Lattice

**Theorem (ergodicity for a lattice).** Let $G$ be a connected semisimple Lie group with finite centre and no compact factors, and let $\Gamma \leq G$ be a lattice. Then the translation action of $G$ on $G/\Gamma$ is ergodic and, when $\Gamma$ is irreducible, mixing. Consequently the translation operators $T_a$ descend to the quotient and their only common invariant functions are the constants.

**Proof sketch.** The proof is the Moore–Mautner phenomenon: a closed subgroup $H \leq G$ that is not contained in a compact subgroup acts ergodically on $G/\Gamma$, and the argument propagates the vanishing of an invariant vector from the subgroup generated by the unipotent radicals of the parabolic subgroups to all of $G$; the mixing is the decay of the matrix coefficients of $G$, the Howe–Moore theorem. Both are Part III, *Ergodic Theory of Group Actions* and *Homogeneous Dynamics*, and are quoted, not proved.

**Corollary (one-parameter flows).** Let $\{a_t\} \subseteq G$ be a one-parameter subgroup. If $\{a_t\}$ is not contained in a compact subgroup of $G$ — in particular if $a_t$ is unipotent, or if $a_t$ is a regular semisimple element generating the Cartan subgroup — then the flow $T_{a_t}$ on $G/\Gamma$ is ergodic; the horocycle flow, the case of a unipotent $\{a_t\}$, is ergodic and uniquely ergodic on a compact quotient.

**Proof.** The criterion is the Moore–Mautner phenomenon applied to the closed subgroup $\{a_t\}$; that a unipotent subgroup is not compact and that the theorem applies is the content of the quoted result, and the unique ergodicity of the horocycle flow is the Hedlund–Furstenberg theorem, in Part III.

**Remark.** Ergodicity is a property of the **lattice**, and the geometry is visible in it. A nonuniform lattice gives a cusp and a continuous spectrum; a uniform lattice gives a compact quotient and a discrete part at the bottom of the spectrum; an arithmetic lattice has the Hecke operators as extra symmetries, and the arithmeticity and the classification of the lattices are *Homogeneous Dynamics* and *Automorphic Forms*. The ergodicity of the flow is the operator expression of the fact that a lattice cannot be decomposed into smaller invariant pieces.

## Worked Cases

**Example (the circle).** Let $G = \mathbb{R}$, $\Gamma = \mathbb{Z}$, and $T_\alpha$ the translation by $\alpha$ on $\mathbb{R}/\mathbb{Z} = S^1$. The translation operators are multiplication by the characters $e^{2\pi i n x}$, and $T_\alpha$ is ergodic exactly when $\alpha$ is irrational: for rational $\alpha$ the first return map has finite orbits and there are invariant sets of intermediate measure, while for irrational $\alpha$ the orbit is dense and the only invariant functions are the constants. This is the classical irrational rotation, and the translation operator is the unitary $T_\alpha f(x) = f(x-\alpha)$.

**Example (the torus).** Let $G = \mathbb{R}^n$, $\Gamma = \mathbb{Z}^n$, and $T_a$ the translation by $a$ on the torus $\mathbb{T}^n$. The flow is ergodic exactly when the entries of $a$ are linearly independent over $\mathbb{Q}$, and the translation operator is diagonal in the character basis with eigenvalues the exponentials of $a$; the finite-order translations have finite orbits and are not ergodic. This is the abelian case of the general criterion, and the operators are the *Convolution Operators* on $\mathbb{T}^n$.

**Example (the hyperbolic surface).** Let $G = PSL(2, \mathbb{R})$, $K = SO(2)$, $\Gamma$ a torsion-free lattice, and $Y = \Gamma\backslash \mathbb{H}^2$ the hyperbolic surface. The translation flow on the unit tangent bundle $G/\Gamma$ is the geodesic flow, and it is ergodic with respect to the invariant measure by the Hopf argument; the horocycle flow is the unipotent flow and is uniquely ergodic on a compact quotient. This is the geometric case that the abstract criterion generalises, and the ergodicity of the geodesic flow is the statement that the lattice is irreducible.

**Example (a compact factor).** Let $G = G_1 \times G_2$ with $G_1$ compact and $G_2$ simple, and let $\Gamma = G_1 \times \Gamma_2$. Then the translation action of $G$ on $G/\Gamma = G_1 \times G_2/\Gamma_2$ has the compact factor as an invariant set of intermediate measure, so the action is not ergodic: the presence of a compact factor is exactly what the criterion excludes. The example shows that ergodicity is sensitive to the chosen lattice and the chosen subgroup, and is not a property of $G$ alone.

## Summary

The translation operator by $a$ on a symmetry group is $T_a f(x) = f(a^{-1}x)$, a representation of $G$ commuting with the right translations $S_b f(x) = f(xb)$; the operators commuting with the left translations are exactly the right convolutions $f \mapsto f * \mu$, so the algebra of translation-invariant operators is the measure algebra, commutative exactly for abelian $G$, and on an abelian group the translations are multiplication by the characters. A lattice is a discrete subgroup of finite covolume; its quotient $G/\Gamma$ carries the normalised invariant measure and is the frame bundle of the finite-volume locally symmetric space $\Gamma\backslash X$, and the translation operators descend to flows there, the geodesic flow and the horocycle flow among them. Ergodicity is the absence of invariant sets of intermediate measure, equivalently the absence of nonzero invariant functions on $G/\Gamma$; for a connected semisimple $G$ with no compact factors the translation action is ergodic and mixing by the Moore–Mautner phenomenon and the Howe–Moore theorem, and a one-parameter subgroup generates an ergodic flow exactly when it is not contained in a compact subgroup. The irrational rotation on the circle, the translations on the torus, and the geodesic and horocycle flows on a hyperbolic surface are the classical instances; the presence of a compact factor destroys ergodicity.

The ergodic theorems, the mixing rates and the classification of the orbit closures of the unipotent flows are Part III and are cited; the article's content is the translation operator, its invariance, and the geometric meaning of the ergodicity of its flow on a lattice quotient. The involution on the elements of the symmetry group and the adjoint of an operator are the later groups of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_a$ | translation operator, $T_a f(x) = f(a^{-1}x)$; left regular representation |
| $S_b$ | right translation operator, $S_b f(x) = f(xb)$ |
| $\mu$ | a measure or distribution; the right convolution $f * \mu$ |
| $\Gamma$ | a lattice: discrete subgroup of finite covolume |
| $G/\Gamma$ | the quotient $G$-space with the normalised invariant measure |
| $\Gamma\backslash X$ | the locally symmetric space of the lattice |
| $L^2_0(G/\Gamma)$ | the mean-zero functions; no nonzero invariant vector iff ergodic |
| $T_{a_t}$ | the translation flow of the one-parameter group $\{a_t\}$ |
| ergodic, mixing | no invariant set of intermediate measure; decay of correlations |
| $\hat T_a(\chi) = \chi(a)^{-1}$ | the diagonalisation of the abelian translations |
| horocycle, geodesic flow | the unipotent and Cartan flows on $G/\Gamma$ |

## Further Reading

- Robert J. Zimmer, *Ergodic Theory and Semisimple Groups* (Birkhäuser, 1984), for the Moore–Mautner phenomenon, the ergodicity of the translation action and the mixing of the lattice quotients.
- Grigoriy A. Margulis, *Discrete Subgroups of Semisimple Lie Groups* (Springer, 1991), for lattices, arithmeticity, the finite volume quotients and the ergodic theorems.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the locally symmetric space $\Gamma\backslash G/K$ and the identification of the flows.
- Hopf, "Statistik der geodätischen Linien in Mannigfaltigkeiten negativer Krümmung", *Berichte über die Verhandlungen der Sächsischen Akademie der Wissenschaften zu Leipzig* **91** (1939), 261–304, for the ergodicity of the geodesic flow.
- Marina Ratner, "On Raghunathan's measure conjecture", *Annals of Mathematics* **134** (1991), 545–607, for the classification of the invariant measures of the unipotent flows, cited as Part III.
