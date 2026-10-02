# __Krein–Tomita–Takesaki Theory__

## Introduction

The Tomita–Takesaki theorem has three statements. The **modular group**: the family $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ is a one-parameter group of automorphisms of the von Neumann algebra, and it is the only group satisfying the KMS condition for the state defined by the vector. The **modular conjugation**: the map $x\mapsto \jmath x^{*}\jmath$ carries the algebra to its commutant, $\jmath\mathcal{M}\jmath = \mathcal{M}'$, and it reverses the modular operator, $\jmath\Delta\jmath = \Delta^{-1}$. The **flow**: the two together give the "standard form" in which the algebra, its commutant and the vector interact, and the KMS condition picks out the modular group among all groups of automorphisms. The theory is the deepest structural result about von Neumann algebras, and it is the source of the modular theory of states.

**Krein–Tomita–Takesaki theory** is the same three statements for a **Krein–von Neumann algebra** with a modular vector and a self-dual cone. The statements survive; what changes is that the objects carry the fundamental symmetry. The modular group is a group of $J$-automorphisms, the modular conjugation is $J$-unitary, the states whose modular group it is are **$J$-positive** rather than positive, and the KMS condition is taken only on the part of the algebra on which the $J$-positivity is defined. This article states the theorem, the modular group and the modular flow, the $J$-modular automorphism group and the $J$-KMS condition.

The modular data itself — the Tomita operator, the $J$-modular operator and the $J$-modular conjugation — is *The Indefinite Modular Operator*; the algebra and its operator theory are *Krein–von Neumann Algebras* and *J-Self-Adjoint and J-Unitary Operators*; the indefinite representation theory is *The Indefinite GNS Construction* and *Krein Algebras*; the definite case is *The Modular Operator and Tomita-Takesaki Theory* and *The Modular Group and the KMS Condition*. Those are cited. The Krein space is $K$, the algebra $\mathcal{M}$, the fundamental symmetry $J$, the $J$-modular operator $\Delta$ and the $J$-modular conjugation $\jmath$.

## The Modular Group of a Krein–von Neumann Algebra

**Definition.** Let $\mathcal{M}$ be a Krein–von Neumann algebra on $K$ with a modular vector $\xi$, $J$-modular operator $\Delta$ and $J$-modular conjugation $\jmath$, in the sense of *The Indefinite Modular Operator*. The **$J$-modular automorphism group** is

$$
\sigma_t = \mathrm{Ad}\,\Delta^{it} : \mathcal{M}\to\mathcal{M}, \qquad \sigma_t(x) = \Delta^{it}x\Delta^{-it} .
$$

**Theorem ($J$-modular group).** $\sigma$ is a one-parameter group of $J$-automorphisms of $\mathcal{M}$: each $\sigma_t$ is an algebra automorphism of $\mathcal{M}$, is compatible with the indefinite adjoint, $\sigma_t(x^{\dagger}) = \sigma_t(x)^{\dagger}$, and fixes the fundamental symmetry, $\sigma_t(J) = J$; the family is strongly continuous in the definite topology of $J$.

**Proof.** $\Delta^{it}$ is a strongly continuous group of definite-unitary operators commuting with $J$; a $J$-commuting definite-unitary $U$ gives the automorphism $x\mapsto UxU^{-1} = UxU^{\dagger}$ because $U^{\dagger} = U^{-1}$, hence compatible with the indefinite adjoint; the fixedness of $J$ is the commutation.

**Proposition (the group leaves the algebra and its commutant invariant).** $\sigma_t(\mathcal{M}) = \mathcal{M}$ for every $t$, and the same holds for $\mathcal{M}^{c}$.

**Proof.** The first statement is the theorem; the commutant is carried to itself because a unitary implementing an automorphism of $\mathcal{M}$ commutes with $\mathcal{M}^{c}$.

**Proposition (the modular flow).** The map $t\mapsto\sigma_t$ is the **modular flow**: it is the modular group of *The Indefinite Modular Operator*, it preserves the form-based structure of $\mathcal{M}$ through its compatibility with $\dagger$, and its generator, when it exists, is the derivation $x\mapsto i[\log\Delta, x]$.

**Proof.** The content is the theorem; the generator is the derivative at the origin of a strongly continuous one-parameter group of the definite form.

## The Modular Conjugation and the Commutant

**Theorem (conjugation maps the algebra to its commutant).** With the notation above,

$$
\jmath\,\mathcal{M}\,\jmath = \mathcal{M}^{c}, \qquad \jmath\,\Delta\,\jmath = \Delta^{-1}, \qquad \jmath\,J\,\jmath = J .
$$

So the $J$-modular conjugation is an anti-isomorphism of the algebra onto its commutant, it inverts the $J$-modular operator, and it commutes with the fundamental symmetry.

**Proof.** The first identity is the classical conjugation theorem transported by $J$: since the polar decomposition of $\bar S$ is $\jmath\Delta^{1/2}$ and $S$ is defined by the involution, the map $x\mapsto\jmath x\jmath$ reverses products and carries $\mathcal{M}$ to the operators commuting with $\mathcal{M}$; the second identity follows from $S^{2} = \mathrm{id}$ on the dense domain and the uniqueness of the polar decomposition; the third is the $J$-commutation of $\jmath$ established in *The Indefinite Modular Operator*.

**Corollary (the standard form).** In the triple $(\mathcal{M}, K, \xi)$ the algebra acts on $K$, the commutant is its $J$-modular image, and the vector is $J$-cyclic for both; this is the indefinite **standard form** of the algebra.

**Proof.** Cyclicity for $\mathcal{M}$ and for $\mathcal{M}^{c}$ is the modular hypothesis, and the image statement is the theorem.

**Remark (the asymmetry introduced by $J$).** In the definite case the modular conjugation is determined by the algebra and the vector. In the indefinite case the conjugation is $J$-unitary and commutes with $J$, so it is an anti-isomorphism of the pair $(\mathcal{M},J)$ onto the pair $(\mathcal{M}^{c},J)$: the modular theory of a Krein–von Neumann algebra is the modular theory of the pair, not of the algebra alone, and two algebras differing only in the choice of $J$ have different modular data.

## The $J$-KMS Condition

**Definition.** Let $\omega$ be a $J$-positive linear functional on $\mathcal{M}$ and $\sigma$ a strongly continuous group of $J$-automorphisms. The functional is **$J$-KMS at $\beta\in\mathbb{R}$** with respect to $\sigma$ when for every $x, y\in\mathcal{M}$ there is a function $F$ bounded and continuous on the closed strip $\{z : 0\leq\mathrm{Im}\,z\leq\beta\}$ and holomorphic in its interior with

$$
F(t) = \omega\big(x\,\sigma_t(y)\big), \qquad F(t+i\beta) = \omega\big(\sigma_t(y)\,x\big)
$$

for all real $t$.

**Theorem ($J$-KMS characterisation).** For a $J$-positive faithful weight $\omega$ with $J$-modular group $\sigma$, the functional $\omega$ is $J$-KMS at $\beta$ with respect to $\sigma$; conversely, a strongly continuous group of $J$-automorphisms of $\mathcal{M}$ satisfying the $J$-KMS condition for $\omega$ coincides with the $J$-modular group of $\omega$.

**Proof.** The direct statement is the classical KMS computation for $\omega(x) = [\pi(x)\xi,\xi]$, read with the indefinite adjoint: the analytic continuation of $t\mapsto[\pi(x\sigma_t(y))\xi,\xi]$ to the strip is the content of the modular relation, and $J$-positivity replaces positivity so that the boundary values used are the $J$-positive ones. The converse is the uniqueness of the modular group, which is the second half of the classical theorem and is transported by $J$ as in the proof of the $J$-modular group.

**Proposition (the definite case).** For $J = \mathrm{id}$ the $J$-KMS condition is the KMS condition of *The Modular Group and the KMS Condition*, the theorem is the Tomita–Takesaki theorem of *The Modular Operator and Tomita-Takesaki Theory*, and the modular conjugation is the classical conjugation with $\jmath\mathcal{M}\jmath = \mathcal{M}'$.

**Proof.** Every statement reduces to its classical form at $J = \mathrm{id}$.

**Remark (the role of $J$-positivity).** The KMS condition uses the functional and its positivity to obtain the analytic continuation. In the indefinite case the functional is only $J$-positive, so the condition is imposed on the $J$-positive part of the algebra and the fundamental symmetry is the parameter that decides which part that is. The $J$-KMS condition is therefore not a weakening of the KMS condition but a version of it indexed by $J$: the flow and the states that describe it are the modular data of the pair $(\mathcal{M},J)$.

## Worked Cases

### The Abelian Algebra

Let $K = L^{2}$-type Hilbert space of *The Modular Operator and Tomita-Takesaki Theory* with $\mathcal{M}$ its algebra of multiplications and $J = \mathrm{id}$: the modular group is the one of the classical theory and the $J$-KMS condition is the KMS condition.

### A Pontryagin Algebra

Let $K = \mathbb{C}^{1,1}$ with $\mathcal{M}$ the diagonal matrices, $J = \mathrm{diag}(1,-1)$ and $\xi = e_1+e_2$. The $J$-modular operator is the identity, the $J$-modular group is trivial, and the $J$-modular conjugation is the antilinear coordinate exchange, which carries $\mathcal{M}$ to $\mathcal{M}^{c} = \mathcal{M}$ and commutes with $J$; the $J$-KMS condition is satisfied by every $J$-positive functional at every $\beta$, since the flow is trivial.

### The Definite Case

At $J = \mathrm{id}$ every statement above is the corresponding statement of *The Modular Operator and Tomita-Takesaki Theory* and *The Modular Group and the KMS Condition*, so the theory is a strict extension of the classical one.

## Summary

**Krein–Tomita–Takesaki theory** is the Tomita–Takesaki theorem for a **Krein–von Neumann algebra** with a modular vector and a self-dual cone. The **$J$-modular automorphism group** $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ is a strongly continuous one-parameter group of $J$-automorphisms of the algebra: each $\sigma_t$ is an algebra automorphism compatible with the indefinite adjoint and fixing $J$, and it is the **modular flow**. The **$J$-modular conjugation** satisfies $\jmath\mathcal{M}\jmath = \mathcal{M}^{c}$, $\jmath\Delta\jmath = \Delta^{-1}$ and $\jmath J\jmath = J$, so it is an anti-isomorphism of the pair $(\mathcal{M},J)$ onto $(\mathcal{M}^{c},J)$ and the standard form is a form of the pair and not of the algebra alone. The **$J$-KMS condition** is the analytic continuation condition $\omega(x\sigma_t(y))\rightsquigarrow\omega(\sigma_t(y)x)$ across the strip, imposed on the $J$-positive functionals and characterising the modular group among the groups of $J$-automorphisms, and it reduces to the classical KMS condition at $J = \mathrm{id}$. The modular data is built in *The Indefinite Modular Operator*, the algebra is *Krein–von Neumann Algebras*, and the definite case is *The Modular Operator and Tomita-Takesaki Theory* with *The Modular Group and the KMS Condition*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Delta$, $\jmath$ | $J$-modular operator and $J$-modular conjugation |
| $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ | $J$-modular automorphism group, the modular flow |
| $\sigma_t(x^{\dagger}) = \sigma_t(x)^{\dagger}$, $\sigma_t(J) = J$ | $J$-automorphism property |
| $\jmath\mathcal{M}\jmath = \mathcal{M}^{c}$, $\jmath\Delta\jmath = \Delta^{-1}$ | Conjugation to the commutant |
| $\jmath J\jmath = J$ | The conjugation is $J$-unitary |
| $\omega$ $J$-positive | The functionals on which the flow is defined |
| $J$-KMS at $\beta$ | Analytic continuation across the strip |
| $J = \mathrm{id}$ | The classical Tomita–Takesaki theory |

## Further Reading

- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular theory in its original form.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the KMS condition and the modular group.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular conjugation and the standard form.
- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the self-dual cones on which the indefinite theory rests.
- Konrad Schmüdgen, *Unbounded Operator Algebras and Representation Theory* (Akademie-Verlag, 1990), for the indefinite adjoint and the modular objects attached to it.
