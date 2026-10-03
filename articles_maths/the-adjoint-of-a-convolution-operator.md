
# __The Adjoint of a Convolution Operator__

## Introduction

A convolution operator on the group is the operator that sends a function to its convolution with a fixed kernel, and its adjoint with respect to the Haar pairing is convolution with the involuted kernel: the same operator with the kernel carried through the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$. The identity is the analytic heart of the `- * Operator Theory` of the group algebra, and everything else in this group is a specialisation of it: the adjoint of the left and right multiplications, of the sandwich, of the reflection and of the signed left multiplication are the same computation with the parameters carried through the involution and, where a grade involution intervenes, through the composite $\sigma = \alpha\circ\,{}^{*}$. Reading the identity as a statement about the family of convolution operators, it says that the map $f\mapsto C_f$ is an injective `*`-homomorphism of the group algebra into the bounded operators, whose closure is the reduced group $\mathrm{C}^*$-algebra and whose von Neumann closure is the group von Neumann algebra — the involutive algebra structure the convolution operators carry. This article states the adjoint, computes it, and describes the involutive algebra it generates; non-unimodular groups are treated only in the left-handed case, where no modular correction is needed.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra $L^1(G)$, its involution and its completions from *The Convolution Algebra $L^1(G)$* and *The Group Algebra as an Involutive Algebra*; the convolution operators and their composition laws from *Convolution on a Group* and *The Group Algebra as an Algebra of Operators*; the regular representations, their commutation and the von Neumann algebra they generate from *The Left and Right Regular Representation*; the involutive structure of the convolution algebra from *The Involution on the Measure Algebra*; the elementary adjoints and the integrated-form identity from *Hermitian Operators on a Group Algebra* and *Unitary Representations and the Adjoint*; the signed adjoints from *The Signed Adjoint Sandwich on the Group Algebra*, *The Signed Adjoint of the Reflection on the Group Algebra* and *The Signed Adjoint of the Left Multiplication on the Group Algebra*; the graded adjoint action from *The Graded Adjoint Action on a Module over the Group Algebra*, immediately preceding; and the bounded operators, the `*`-algebras, the strong and weak topologies, the group von Neumann algebra and the reduced group $\mathrm{C}^*$-algebra from *Operator Algebras*. The measure case and the algebra of measures are *The Involution on the Measure Algebra*; the Plancherel transform is *The Plancherel Operator*.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and modular function $\Delta$; for a kernel $f\in L^1(G)$ the **convolution operator** is

$$
C_f = L_f, \qquad C_f g = f*g, \qquad (f*g)(x) = \int_G f(y)g(y^{-1}x)\,dy ,
$$

on $L^p(G)$, $1\leq p\leq\infty$, and in particular on $L^2(G)$; the **Haar pairing** is $\langle g,h\rangle = \int_G g\overline{h}\,dx$, and the **adjoint** is with respect to it. The involution is $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$, and the right convolution is $R_fg = g*f$. The **reduced group $\mathrm{C}^*$-algebra** is $C^*_r(G) = \overline{\lambda(L^1(G))}^{\|\cdot\|}$ and the **group von Neumann algebra** is $L(G) = \lambda(L^1(G))''$, with $\lambda(f) = C_f$.

## The Adjoint of a Convolution Operator

**Theorem (the adjoint is convolution by the involution).** For every $f\in L^1(G)$ the convolution operator on $L^2(G)$ has adjoint

$$
\bigl(C_f\bigr)^* = C_{f^*}, \qquad f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1} ,
$$

with respect to the Haar pairing, for every locally compact $G$; in the unimodular case the right convolution has the mirror adjoint $(R_f)^* = R_{f^*}$.

**Proof.** The left regular representation is unitary, so its integrated form satisfies $\lambda(f)^* = \lambda(f^*)$: expanding the integrated form, $\lambda(f)^* = \int\overline{f(x)}\lambda(x)^{-1}dx$, and the substitution $x\to x^{-1}$ with the inversion identity $dx = \Delta(y)^{-1}dy$ at $x = y^{-1}$ gives $\int\overline{f(y^{-1})}\Delta(y)^{-1}\lambda(y)dy = \lambda(f^*) = C_{f^*}$. The right-handed identity is the same computation for the right regular representation, which is unitary exactly in the unimodular case. $\square$

**Corollary (the elementary cases recover the earlier adjoints).** With $f = a$ a general element, the adjoint of the left multiplication is $C_{a^*}$; the sandwich, the reflection and the signed left multiplication have the adjoints $S_{a,b}^* = S_{\alpha(a^*),\alpha(b^*)}$, $\rho_u^* = \rho_{\alpha(u^*)}$ and $\Lambda_a^* = \Lambda_{\alpha(a^*)}$, each obtained from the present identity by composing with the twist and using $\mathrm{A}^* = \mathrm{A}$.

**Proof.** $C_a = L_a$ and $L_a^* = L_{a^*}$ is the theorem; the signed formulas are the computations of the three preceding articles, which used exactly this identity for the convolution factor and the self-adjointness of $\mathrm{A}$. $\square$

## The Involutive Algebra of Convolution Operators

**Theorem (the map is an injective `*`-homomorphism).** The assignment $f\mapsto C_f$ is an injective `*`-homomorphism of the Banach `*`-algebra $L^1(G)$ into the `*`-algebra of bounded operators on $L^2(G)$,

$$
C_{f*g} = C_fC_g, \qquad (C_f)^* = C_{f^*}, \qquad \|C_f\|\leq\|f\|_1 ,
$$

whose image is a `*`-subalgebra; the map $f\mapsto C_f$ is the left regular representation $\lambda$, and its injectivity is the faithfulness of $\lambda$.

**Proof.** $C_{f*g}g' = (f*g)*g' = f*(g*g') = C_fC_gg'$ by associativity of convolution, so the map is multiplicative; the adjoint identity is the theorem; the norm bound is Young's inequality, $\|f*g\|_p\leq\|f\|_1\|g\|_p$; injectivity of $\lambda$ is *The Group Algebra as an Involutive Algebra*. $\square$

**Corollary (the two completions).** The closure of the image in the operator norm is the reduced group $\mathrm{C}^*$-algebra $C^*_r(G)$, a `*`-subalgebra of $B(L^2(G))$ closed under the adjoint; the closure in the weak operator topology is the group von Neumann algebra $L(G)$, a von Neumann algebra closed under the adjoint; and the two are the operator completions of the same involutive algebra.

**Proof.** The norm closure of a `*`-subalgebra of $B(L^2(G))$ is a `*`-subalgebra, closed in norm; the weak closure is a von Neumann algebra; the identifications are the definitions of $C^*_r(G)$ and $L(G)$. $\square$

**Theorem (the involution is not the inverse).** The adjoint $C_f^* = C_{f^*}$ is convolution by the involution, not by the inverse; the two agree, $C_f^* = C_{f}^{-1}$, exactly when $f$ is a unitary element of $L^1(G)$, and in the group algebra of a non-discrete group there are no unitary elements, so the identity is the only self-adjoint element with unitary convolution operator.

**Proof.** $C_f^* = C_{f^*}$ and $C_f^{-1} = C_{f^{-1}}$ for a unit $f$; they agree exactly when $f^* = f^{-1}$, which is the definition of a unitary element. The absence of unitary elements on a non-discrete $L^1(G)$ is *The Group Algebra as an Involutive Algebra*. $\square$

## The Measure Case and the $L^p$ Picture

**Theorem (the measure case).** For a bounded Radon measure $\mu\in M(G)$ the operator $\lambda(\mu)$ of left convolution on $L^2(G)$ has adjoint $\lambda(\mu)^* = \lambda(\mu^*)$ with the measure involution $\mu^*(E) = \overline{\mu(E^{-1})}$; since $L^1(G)$ is weak-`*` dense in $M(G)$ and both convolution and the involution are weak-`*` continuous, the identity extends the group-algebra statement to the whole measure algebra.

**Proof.** This is *The Involution on the Measure Algebra*, where the adjoint is computed for measures; the extension from $L^1(G)$ to $M(G)$ uses the density of the absolutely continuous measures. $\square$

**Proposition (the $L^p$ adjoint, qualitatively).** For $1<p<\infty$ and its conjugate exponent $p'$, the adjoint of $C_f$ with respect to the duality pairing between $L^p(G)$ and $L^{p'}(G)$ is the convolution operator with the reflected-conjugate kernel, and on $L^2(G)$ it is $C_{f^*}$; the conjugation of the pairing is what distinguishes the two, exactly as the passage from the bilinear form of the discrete theory to the Haar pairing distinguishes the adjoints $(L_a)^\dagger = L_{a^{-1}}$ and $(L_a)^* = L_{a^*}$.

**Proof.** The duality $(L^p)' = L^{p'}$ is realised by the bilinear integral, while the Haar pairing is conjugate-linear in the second variable; the two pairings differ by the involution $g\mapsto\overline{g}$, which conjugates the kernel and turns the reflected kernel into $f^*$. The case $p = 2$ is the theorem, and the discrete comparison is *The Signed Adjoint of the Left Multiplication on a Topological Group*. $\square$

**Corollary (the $\mathrm{C}^*$-identity).** The convolution operators satisfy $C_{f^*\!*f} = C_f^*C_f$, hence $\|C_{f^*\!*f}\|_{B(L^2)} = \|C_f\|_{B(L^2)}^2$; the norm closure $C^*_r(G)$ therefore carries the $\mathrm{C}^*$-norm, and the involution is isometric on it.

**Proof.** $C_{f^*\!*f} = C_{f^*}C_f = C_f^*C_f$ by multiplicativity and the adjoint identity, and the operator norm obeys the $\mathrm{C}^*$-identity $\|T^*T\| = \|T\|^2$; a norm-closed `*`-subalgebra of $B(L^2(G))$ satisfying it is a $\mathrm{C}^*$-algebra, and the involution is isometric there because $\|C_f\|^2 = \|C_f^*C_f\|\leq\|C_f^*\|\|C_f\|$ gives $\|C_f\|\leq\|C_f^*\|$ and, symmetrically, equality. $\square$

## The Degenerate Cases

**Theorem (abelian and discrete groups).** If $G$ is abelian then convolution is commutative, $C_fC_g = C_gC_f$, the `*`-algebra of convolution operators is commutative, and its completion is the algebra of multiplication by the Fourier transform; if $G$ is discrete then $L^1(G) = \ell^1(G)$ has unitary elements, the point masses, $\delta_g^* = \delta_{g^{-1}}$, and $C_{\delta_g}$ is the unitary operator $\lambda(g)$.

**Proof.** For abelian $G$ the commutativity is that of convolution and the completion statement is the Fourier transform of *Harmonic Analysis on Groups*; for discrete $G$ the point masses are unitary and $C_{\delta_g} = \lambda(g)$ by $\lambda(\delta_g) = \lambda(g)$. $\square$

**Remark (what the article does not do).** The measure algebra and its involution are *The Involution on the Measure Algebra*; the Plancherel transform as an operator and the unitary equivalence with the direct integral over the dual are *The Plancherel Operator*; the group von Neumann algebra and the regular representation are *The Left and Right Regular Representation* and *The Group Algebra as an Algebra of Operators*. The exact form of the $L^p$ adjoint is stated only qualitatively above; the conjugation of the pairing and the reflected kernel are its content, and the computation for each $p$ is left to the duality theory of *Harmonic Analysis on Groups*.

## Summary

The convolution operator $C_fg = f*g$ on $L^2(G)$ has adjoint $C_f^* = C_{f^*}$ with respect to the Haar pairing, convolution by the involuted kernel $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$, for every locally compact group; the right convolution has the mirror adjoint in the unimodular case. The identity recovers the adjoints of the left multiplication, of the sandwich, of the reflection and of the signed left multiplication as its specialisations, with the parameters carried through the involution and, where a grade involution intervenes, through the composite $\sigma = \alpha\circ\,{}^{*}$. The assignment $f\mapsto C_f$ is an injective `*`-homomorphism of $L^1(G)$ into the bounded operators, $C_{f*g} = C_fC_g$, $(C_f)^* = C_{f^*}$, $\|C_f\|\leq\|f\|_1$, whose norm closure is the reduced group $\mathrm{C}^*$-algebra and whose weak closure is the group von Neumann algebra — the operator completions of the same involutive algebra. The adjoint is the involution and not the inverse, the two coinciding exactly for a unitary element, which exists only in the discrete or measure-algebra reading; the measure case extends the identity to $M(G)$, and the $L^p$ adjoint is realised by the duality pairing with the reflected-conjugate kernel, agreeing with $C_{f^*}$ on $L^2$. On an abelian group the algebra is commutative and its completion is multiplication by the Fourier transform; on a discrete group the point masses are the unitary operators.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C_fg = f*g$ | The convolution operator, the left regular representation |
| $(f*g)(x) = \int_G f(y)g(y^{-1}x)\,dy$ | Convolution |
| $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ | The involution |
| $\langle g,h\rangle = \int_Gg\overline{h}\,dx$ | The Haar pairing |
| $(C_f)^* = C_{f^*}$ | The adjoint of a convolution operator |
| $C_{f*g} = C_fC_g$ | Multiplicativity of $f\mapsto C_f$ |
| $\lambda(\mu)^* = \lambda(\mu^*)$ | The measure case |
| $C^*_r(G) = \overline{\lambda(L^1(G))}$ | The reduced group $\mathrm{C}^*$-algebra |
| $L(G) = \lambda(L^1(G))''$ | The group von Neumann algebra |
| $(L_a)^\dagger = L_{a^{-1}}$ vs $(L_a)^* = L_{a^*}$ | The bilinear form vs the Haar pairing |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the reduced group $\mathrm{C}^*$-algebra, the `*`-representations and the `*`-homomorphism property.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the group von Neumann algebra, its weak closure and the regular representation.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the convolution algebra $L^1(G)$, Young's inequality and the involution.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the adjoint of a convolution operator, the regular representations and the unimodular case.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the `*`-algebra of operators, the $\mathrm{C}^*$-identity and the topologies.
