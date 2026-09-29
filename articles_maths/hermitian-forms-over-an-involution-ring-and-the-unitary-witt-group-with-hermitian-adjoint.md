
# __Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint__

## Introduction

Over a field of characteristic not two, a non-degenerate symmetric bilinear form is classified up to congruence by its dimension, its determinant and its Hasse invariant, and the forms are added by orthogonal sum to build the Witt group. When the field is replaced by a ring with an involution, the correct objects are **Hermitian forms** and the correct group is the **unitary Witt group**, whose classification is harder and whose invariants include the discriminant and, for the forms over a central simple algebra with involution, the **Wall group**. A Clifford algebra is a ring with three involutions, and the Hermitian forms it carries — the forms of *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint* — therefore live in a unitary Witt group rather than in an orthogonal one.

This article sets out the general theory in the amount the Clifford case needs, and then reads the three forms of the algebra in it. The two structural facts are that the three forms are Hermitian over the algebra with respect to their own anti-involutions, hence represent classes in the corresponding unitary Witt groups, and that their **isometry groups** — the unitary slice for the dagger and the Pin group for Clifford conjugation — preserve the Witt classes, so that the slice and Pin act on the Witt groups by isometries of the forms rather than by arbitrary automorphisms. The classification theory of the algebra-valued quadratic forms, the Clifford invariant and the eightfold way belong to *Quadratic Forms over Algebras and Norms*, *The Brauer–Wall Group and the Eightfold Way* and *The Witt Group and the Grothendieck–Witt Ring*; the classical orthogonal theory is *Bilinear Forms* and *Quadratic Forms and Polarisation*; and the extension and cancellation theorems are *Witt's Theorems*.

## Hermitian Forms over a Ring with Involution

**Definition.** Let $R$ be a ring with an anti-involution $c$ and let $\varepsilon \in R$ be central with $c(\varepsilon) = \varepsilon$ and $\varepsilon\bar\varepsilon = 1$, where $\bar\varepsilon$ is the image of $\varepsilon$ under $c$. A **$\varepsilon$-Hermitian form** on a right $R$-module $M$ is a biadditive map $h : M \times M \to R$ with

$$
h(xa, yb) = c(a)\,h(x,y)\,b, \qquad h(y,x) = \varepsilon\,c\bigl(h(x,y)\bigr),
$$

for all $x, y \in M$ and $a, b \in R$. The case $\varepsilon = 1$ is a **Hermitian** form and $\varepsilon = -1$ a **skew-Hermitian** or **symplectic** form.

**Remark (the Clifford forms).** For $R = \mathrm{Cl}(V,q)$ the definition is exactly the structure of *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint*: with $c = {}^{\dagger}$ and $\varepsilon = 1$ one gets $h_{\dagger}(x,y) = x^{\dagger}y$; with $c = \bar\cdot$ one gets $h_{\bar\cdot}(x,y) = \bar xy$; with $c = {}^{r}$ one gets $h_r(x,y) = x^{r}y$. The three forms satisfy their own Hermitian conditions and are therefore $\varepsilon$-Hermitian forms over the algebra with the respective involution.

**Definition.** The **radical** of a Hermitian form is $M^{\perp} = \{x : h(x,y) = 0 \ \forall y\}$, and the form is **non-degenerate** if $M^{\perp} = 0$ and **nonsingular** if moreover the induced map $M \to M^{*}$ is an isomorphism; over a division ring, or over a field, the two conditions coincide. The **discriminant** is the class of $\det H$ in the appropriate quotient of the units, and the **unitary group** is $\mathrm{U}(h) = \{s : h(sx,sy) = h(x,y)\}$.

**Theorem (Dieudonné, extension and cancellation).** Let $h$ be a nonsingular Hermitian form over a division ring with involution, and let $U \subseteq M$ be a subspace with $M = U\oplus U^{\perp}$. Then every isometry $U \to M$ extends to an isometry of $M$; and if $M = U\oplus U^{\perp}$ for another decomposition with $U' \cong U$, then the two orthogonal complements are isometric (**Witt cancellation**). The statements hold with the usual exceptions in characteristic two.

**Corollary (the Clifford groups).** For $h_{\dagger}$ the unitary group is the unitary slice $U$ and for $h_{\bar\cdot}$ it is the Pin group, by the proposition of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint* and the identification of *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint*. So the Clifford and spin structures are exactly the unitary groups of the Hermitian forms of the algebra, and the extension and cancellation theorems apply to them.

## The Witt Group

### Hyperbolic and Metabolic Forms

**Definition.** The **hyperbolic** $\varepsilon$-Hermitian form on $M \oplus M^{*}$ is $h\bigl((x,\phi),(y,\psi)\bigr) = \phi(y) + \varepsilon\,c(\psi(x))$, and a form is **metabolic** if it has a submodule $N$ with $N = N^{\perp}$. The **orthogonal sum** $h_1\perp h_2$ is the form on $M_1\oplus M_2$ vanishing across the summands.

**Definition.** The **even Witt group** $W^{\varepsilon}(R,c)$ of a ring with involution is the Grothendieck group of the monoid of nonsingular $\varepsilon$-Hermitian forms under orthogonal sum, modulo the subgroup of metabolic forms; the **Grothendieck–Witt group** $GW^{\varepsilon}(R,c)$ is the corresponding group before the metabolic forms are divided out, so that $GW \to W$ is the quotient by the hyperbolic subgroup. The classical theory is in *The Witt Group and the Grothendieck–Witt Ring*.

**Proposition.** Each of the three Clifford forms has a class in the Witt group of its own involution,

$$
[h_{\dagger}] \in W^{1}\bigl(\mathrm{Cl}(V,q), {}^{\dagger}\bigr), \qquad
[h_{\bar\cdot}] \in W^{1}\bigl(\mathrm{Cl}(V,q), \bar\cdot\bigr), \qquad
[h_{r}] \in W^{1}\bigl(\mathrm{Cl}(V,q), {}^{r}\bigr),
$$

over a field of characteristic not two, since each is non-degenerate by *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint* and nonsingularity follows from non-degeneracy over the algebra when the algebra is a product of matrix algebras over a field.

**Remark (the $\varepsilon = -1$ companion).** The $\varepsilon$-conjugates $h_{\dagger}(x,y) - h_{\dagger}(y,x)$ and the alternating forms on the algebra give classes in $W^{-1}$, the symplectic Witt group; the two Witt groups together are the data of the Grothendieck–Witt ring, and the reader is referred to *The Witt Group and the Grothendieck–Witt Ring* for the ring structure.

### The Clifford Algebra as a Hermitian Form

**Definition.** The **unit form** of the algebra with respect to the anti-involution $c$ is the Hermitian form $h_c(x,y) = c(x)y$ on the algebra regarded as a right module over itself. It is the form whose matrix in an $R$-basis is the identity.

**Proposition (invariance of the class).** The isometry groups of the three forms act on the forms by isometries, hence fix their Witt classes:

$$
s \in U \ \Longrightarrow \ [h_{\dagger}(s\,\cdot\,, s\,\cdot\,)] = [h_{\dagger}], \qquad
s \in \mathrm{Pin}(V,q) \ \Longrightarrow \ [h_{\bar\cdot}(s\,\cdot\,,s\,\cdot\,)] = [h_{\bar\cdot}] ,
$$

and similarly for $h_r$ with the group $\{s : s^{r}s = 1\}$. So the unit form is not merely non-degenerate: it is **fixed as a Witt class** by the whole unitary slice and the whole Pin group, and the orbits of the Clifford groups in the Witt group are trivial on the unit form.

**Proof.** Immediate from the isometry-group proposition of *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint*: an isometry is by definition a substitution under which the form is unchanged, so its class is unchanged.

**Remark (discriminant and signature).** The discriminant of the unit form is the class of $1$, and the scalar reductions of *The Blade Form and the Hilbert Structure with Hermitian Adjoint* give the signature; over $\mathbb{R}$ the signature is the invariant of the form, positive definite exactly for the negative definite quadratic form in the dagger case, and the inertia is the one computed there.

## The Unitary Witt Group of a Clifford Algebra

**Definition.** The **unitary Witt group of a Clifford algebra** with respect to an involution $\sigma$ of the base is the even Witt group $W^{\varepsilon}(\mathrm{Cl}(V,q), {}^{\dagger})$ of the algebra with the dagger; its elements are the Witt classes of nonsingular $\varepsilon$-Hermitian forms over $\mathrm{Cl}(V,q)$ with respect to the dagger.

**Proposition.** The map which sends a Hermitian form over the base to the form on the same module regarded over the Clifford algebra, $g \mapsto g\otimes_{\!A}\mathrm{Cl}(V,q)$ with the diagonal involution, induces a homomorphism of Witt groups

$$
W^{\varepsilon}(A,\sigma) \longrightarrow W^{\varepsilon}\bigl(\mathrm{Cl}(V,q), {}^{\dagger}\bigr),
$$

the **Clifford invariant** or **unitary Clifford map**, and its image is the subgroup of forms that are the scalar extension of a form over the base.

**Proof.** The scalar extension of a nonsingular Hermitian form under a flat base change is nonsingular Hermitian, and the orthogonal sum and the metabolic forms are preserved, so the assignment is a well-defined homomorphism on the Grothendieck groups; the image description is the definition of the image.

**Remark (the two invariants of the theory).** The homomorphism above is the entry point of the classification: the cokernel of the Clifford map measures the forms that are genuinely over the algebra and not over the base, and it is the Clifford algebra side of the invariants computed in *Quadratic Forms over Algebras and Norms*. The Clifford groups act on the cokernel as well, and the two-invariant description of the orthogonal case is replaced in the unitary case by the discriminant together with the **Wall group** of the algebra with involution, which is the home of the obstruction and is treated in *Quadratic Forms over Algebras and Norms* and *The Brauer–Wall Group and the Eightfold Way*. Over a local ring with involution the Wall group is computable and reduces to the classical invariants; over a general base it does not, and this is the difference between the orthogonal and the unitary classification.

**Proposition (the two named classes).** Over $\mathbb{R}$ with $\sigma = \mathrm{id}$ the unitary Witt group of $\mathrm{Cl}_{0,n}$ with the dagger is the Witt group of $\mathbb{R}$-valued Hermitian forms on the spinor module, of dimension $2^{m}$, and the class of $h_{\dagger}$ is the class of the positive definite form; it is the class of $1$ in $W(\mathbb{R}) \cong \mathbb{Z}$, so the Clifford Hermitian form is **Witt-trivial** in the definite case and its invariant is carried by the signature alone.

**Proof.** In the definite case the form $\mathrm{Sc}(x^{\dagger}y)$ has diagonal $+1$ on the blades, so it is isometric to the standard hyperbolic-free form of dimension $2^{m}$ over $\mathbb{R}$, whose Witt class is $1 \in \mathbb{Z}$; a positive definite form over $\mathbb{R}$ has signature equal to its dimension and represents the positive generator.

## Summary

Over a ring with an anti-involution $c$ the correct forms are the **$\varepsilon$-Hermitian forms** $h(xa,yb) = c(a)h(x,y)b$, $h(y,x) = \varepsilon c(h(x,y))$, and the correct groups are the even Witt group $W^{\varepsilon}(R,c)$ and the Grothendieck–Witt group $GW^{\varepsilon}(R,c)$, obtained from the monoid of nonsingular forms by dividing out the metabolic forms; the classical extension and cancellation theorems of Dieudonné hold over a division ring with the usual characteristic-two exceptions. The three forms of a Clifford algebra — $h_{\dagger}(x,y) = x^{\dagger}y$, $h_{\bar\cdot}(x,y) = \bar xy$ and $h_r(x,y) = x^{r}y$ — are Hermitian over the algebra with respect to their own involutions and are non-degenerate, hence represent classes in the three Witt groups; the **unit form** $h_c(x,y) = c(x)y$ has the identity matrix, discriminant $1$, and its Witt class is fixed by the isometry group, so the unitary slice and Pin act trivially on the class. The **unitary Witt group of a Clifford algebra** is $W^{\varepsilon}(\mathrm{Cl}(V,q),{}^{\dagger})$, and the scalar extension homomorphism $W^{\varepsilon}(A,\sigma) \to W^{\varepsilon}(\mathrm{Cl}(V,q),{}^{\dagger})$ is the Clifford invariant of the unitary theory; its cokernel contains the forms genuinely over the algebra, whose obstruction is measured by the Wall group rather than by the discriminant alone. Over $\mathbb{R}$ with the identity involution the form $h_{\dagger}$ is positive definite, so its class is the positive generator and the Clifford Hermitian form is Witt-trivial, the invariant being the signature.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varepsilon$-Hermitian form | $h(y,x)=\varepsilon c(h(x,y))$, $h(xa,yb)=c(a)h(x,y)b$ |
| $M^{\perp}$ | Radical, $M^{\perp}=\{x:h(x,y)=0\ \forall y\}$ |
| $\mathrm{U}(h)$ | Unitary group of $h$ |
| $h_1\perp h_2$ | Orthogonal sum |
| $W^{\varepsilon}(R,c)$, $GW^{\varepsilon}(R,c)$ | Witt and Grothendieck–Witt groups |
| $[h]$ | Witt class of a form |
| $h_c(x,y) = c(x)y$ | Unit form of the algebra |
| $W^{\varepsilon}(\mathrm{Cl}(V,q),{}^{\dagger})$ | Unitary Witt group of the Clifford algebra |
| Clifford map | Scalar extension $W^{\varepsilon}(A,\sigma) \to W^{\varepsilon}(\mathrm{Cl}(V,q),{}^{\dagger})$ |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for $\varepsilon$-Hermitian forms over rings with involution, the Witt and Grothendieck–Witt groups and the Wall group.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the classical Witt theory and the extension and cancellation theorems.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution, Hermitian forms over them and the unitary invariants.
- C. T. C. Wall, "On the Classification of Hermitian Forms", *Inventiones Mathematicae* 18 (1972), 119–141, for the Wall group of a ring with involution.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the comparison between the bilinear, quadratic and Hermitian settings.
