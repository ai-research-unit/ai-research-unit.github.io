
# __Hermitian Operators on a Group Algebra__

## Introduction

An operator on the group algebra is a rule on its elements, and the first invariant of such a rule is its adjoint: the operator that makes the Haar pairing symmetric. The group algebra then splits into operators equal to their adjoints and operators opposite to them, the Hermitian and skew-Hermitian, and an element of the algebra is carried to a Hermitian operator exactly when the element is Hermitian in the involution. So the Hermitian operators on the group algebra are the operator image of the Hermitian elements, the positive operators are the operator image of the positive cone, and the positive functionals are the operator traces that the construction produces. This article fixes the adjoint on the group algebra, computes the adjoints of the elementary operators, and describes the Hermitian cone, the positive operators and the positive functionals with the correspondences among them.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra $L^1(G)$, its involution and its completions from *The Convolution Algebra $L^1(G)$* and *The Group Algebra as an Involutive Algebra*; the convolution operators, the sandwiches and the left regular representation from *Convolution on a Group*, *The Group Algebra as an Algebra of Operators* and *The Left and Right Regular Representation*; the involution, the Hermitian elements, the positive cone and the positive functionals from *The Group Algebra as an Involutive Algebra*; the Hermitian forms and the forms of the positive functionals from *Hermitian Forms and the Group Algebra*; the measure algebra and its involution from *The Involution on the Measure Algebra*; the bounded operators, the adjoint, the spectrum, the positive operators, the trace and the `*`-algebras from *Operator Algebras* and *Adjoints in a Banach Algebra*. The signed operators and their adjoints are *The Signed Adjoint Sandwich on the Group Algebra* and its companions, later in this group; the adjoint of a convolution operator on its own terms is *The Adjoint of a Convolution Operator*, the last article of the group; the Hermitian operators on the group algebra as a Hilbert algebra are also treated in *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*, where the signed form appears.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and modular function $\Delta$, and $\mathcal{A} = L^1(G)\subseteq L^2(G)$ carries the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the **Haar pairing**

$$
\langle f,h\rangle = \int_G f(x)\,\overline{h(x)}\,dx ,
$$

the $L^2(G)$ inner product restricted to $\mathcal{A}\cap L^2(G)$; when $G$ is **unimodular** one has $\Delta\equiv1$ and $f^*(x) = \overline{f(x^{-1})}$. The **adjoint** $T^*$ of a bounded operator $T$ on $L^2(G)$ is defined by $\langle Tf,h\rangle = \langle f,T^*h\rangle$, the left and right convolutions are $L_af = a*f$ and $R_bf = f*b$, and $\mathrm{A}f = \alpha(f)$ is the operator of the grade involution.

## The Adjoint on the Group Algebra

**Theorem (the elementary adjoints).** With respect to the Haar pairing the left convolution has adjoint

$$
(L_a)^* = L_{a^*} \qquad \text{for every } a\in\mathcal{A},
$$

and in the unimodular case the right convolution and the grade-involution operator satisfy

$$
(R_b)^* = R_{b^*}, \qquad \mathrm{A}^* = \mathrm{A} ;
$$

the adjoint operation is an anti-linear involution on the bounded operators,

$$
(T^*)^* = T, \qquad (ST)^* = T^*S^*, \qquad (\lambda T + \mu S)^* = \bar\lambda T^* + \bar\mu S^* .
$$

**Proof.** The left identity follows from the unitary representation $\lambda$ and the integrated form: $\lambda(a)^* = \bigl(\int a(x)\lambda(x)dx\bigr)^* = \int\overline{a(x)}\lambda(x)^{-1}dx$, and the substitution $x\to x^{-1}$ with the inversion identity $dx = \Delta(y)^{-1}dy$ at $x = y^{-1}$ turns this into $\int\overline{a(y^{-1})}\Delta(y)^{-1}\lambda(y)dy = \lambda(a^*) = L_{a^*}$; this is the general form of the computation of *Unitary Representations and the Adjoint*. For the right-hand identity in the unimodular case, $R_b$ is the integrated form of the right regular representation, which is unitary exactly then, and the same computation gives $(R_b)^* = R_{b^*}$; on a non-unimodular group $R_b$ is bounded but $\rho$ is unitary only for the weighted inner product. Finally $\mathrm{A}$ is multiplication by the real involution of the twist (the sign character) or the inverse-transpose of a measure-preserving automorphism, self-adjoint in either case. The operator identities are the general anti-linearity and anti-multiplicativity of the adjoint with respect to an inner product. $\square$

**Corollary (the left regular representation is a `*`-representation).** For the unitary operators of the group, $(L_{\delta_x})^* = L_{\delta_{x^{-1}}}$, so $\lambda(x)^* = \lambda(x)^{-1}$; more generally $\lambda(f)^* = \lambda(f^*)$, and the closure of $\lambda(\mathcal{A})$ is a `*`-subalgebra of $B(L^2(G))$.

**Proof.** $\delta_x^* = \delta_{x^{-1}}$ for a unimodular group, and $\lambda(f) = L_f$; the theorem gives $\lambda(f)^* = \lambda(f^*)$, and closure under the adjoint is its stability under the involution. $\square$

**Remark (the adjoint is not the inverse).** The adjoint of $L_a$ is left convolution by $a^*$, not left convolution by $a^{-1}$; the two agree exactly when $a^* = a^{-1}$, that is when $a$ is unitary. The distinction is the analytic content of the passage from the discrete natural form of *The Adjoint of the Left Multiplication on a Topological Group*, where $(L_a)^\dagger = L_{a^{-1}}$, to the complex Haar pairing of Part III, where the conjugation of the inner product intervenes; the two are reconciled by the involution $a\mapsto a^*$.

## The Haar Pairing and the Two Adjoints

**Definition.** The **bilinear pairing** on the group algebra is $\langle\!\langle f,h\rangle\!\rangle = \int_G fh\,dx$, the Haar pairing read without the conjugation; writing $Jf = \overline{f}$ for the pointwise complex conjugation and $f^\vee(x) = f(x^{-1})$ for the reflection, the two pairings are related by

$$
\langle\!\langle f,h\rangle\!\rangle = \langle f,Jh\rangle, \qquad J = \,{}^{*}\circ\vee,
$$

so on a unimodular group the missing conjugation is recovered by the complex conjugate, $J = \,{}^{*}\circ\vee$, the involution composed with the reflection; in the general case the modular factor enters $J$ through the involution.

**Proposition (the two adjoints are conjugate by $J$).** If $T^\dagger$ denotes the adjoint with respect to the bilinear pairing, then

$$
T^* = J\,T^\dagger\,J ,
$$

so the Haar-pairing adjoint is the bilinear-pairing adjoint conjugated by the complex conjugation $J$; for the elementary operators this is the passage $(L_a)^\dagger = L_{a^{-1}}$ to $(L_a)^* = L_{a^*}$, since $J L_{a^{-1}} J = L_{\overline{a^{-1}}} = L_{a^*}$ on a unimodular group.

**Proof.** For the general identity, $\langle f,JT^\dagger Jh\rangle = \int f\,\overline{JT^\dagger Jh} = \int f\,T^\dagger(\overline h) = \langle\!\langle f, T^\dagger(\overline h)\rangle\!\rangle = \langle\!\langle Tf,\overline h\rangle\!\rangle = \int Tf\,\overline h = \langle Tf,h\rangle$, using $J^2 = \mathrm{id}$ and $\overline{\overline{T^\dagger(\overline h)}} = T^\dagger(\overline h)$. The elementary case follows from $(L_a)^\dagger = L_{a^{-1}}$ and $JL_{a^{-1}}J = L_{\overline{a^{-1}}}$, with $\overline{a^{-1}}(x) = \overline{a(x^{-1})} = a^*(x)$ on a unimodular group. $\square$

**Corollary (which adjoint the discrete articles use).** The discrete `- Operator Theory` articles of Parts I and II work with the bilinear natural and signed forms and obtain $(L_a)^\dagger = L_{a^{-1}}$; the present group works with the Haar pairing and obtains $(L_a)^* = L_{a^*}$; the two computations are reconciled in every case by the conjugation $T\mapsto JTJ$ of the proposition, the involution entering through $J = \,{}^{*}\circ\vee$.

**Proof.** The discrete adjoints are computed from the bilinear forms of *The Adjoint of the Left Multiplication on a Topological Group*; the present adjoints are the proposition's conjugation of them, and the formula $J = \,{}^{*}\circ\vee$ identifies $a^{-1}$ with $a^*$ under the conjugation. $\square$

## Hermitian and Positive Elements

**Definition.** An operator $T$ on $L^2(G)$ is **Hermitian** (self-adjoint) when $T^* = T$, **skew-Hermitian** when $T^* = -T$, **unitary** when $T^*T = TT^* = 1$, and **positive** when $T = S^*S$ for a bounded $S$; an element $f\in\mathcal{A}$ is **Hermitian** when $f^* = f$ and **positive** when $f = g^*\!*g$.

**Theorem (the operator image of the Hermitian elements).** The map $f\mapsto\lambda(f)$ carries the Hermitian elements onto the Hermitian operators in $\lambda(\mathcal{A})$ and the positive cone into the positive operators,

$$
f^* = f \iff \lambda(f)^* = \lambda(f), \qquad f\in\mathcal{A}^+ \implies \lambda(f)\geq0 ,
$$

and it is a `*`-homomorphism; the Hermitian elements of $\mathcal{A}$ form the real subspace $\mathcal{A}_h$, the positive cone $\mathcal{A}^+$ is convex and proper, and $\lambda$ is an order-preserving isomorphism of the ordered `*`-algebra $\mathcal{A}$ onto its image.

**Proof.** By the corollary, $\lambda(f)^* = \lambda(f^*)$, so $\lambda(f)$ is Hermitian exactly when $\lambda(f) = \lambda(f^*)$, which is equivalent to $f = f^*$ because $\lambda$ is injective. If $f = g^*\!*g$ then $\lambda(f) = \lambda(g)^*\lambda(g)\geq0$. The statements about $\mathcal{A}_h$ and $\mathcal{A}^+$ are those of *The Group Algebra as an Involutive Algebra*; multiplicativity and injectivity of $\lambda$ give the isomorphism onto its image. $\square$

**Corollary (the Hermitian decomposition of the operators).** Every operator in $\lambda(\mathcal{A})$ is uniquely $\lambda(f) = \lambda(u) + i\lambda(v)$ with $\lambda(u),\lambda(v)$ Hermitian, and the Hermitian part of $\lambda(\mathcal{A})$ is the image of the Hermitian elements; the skew-Hermitian operators are $i$ times the Hermitian ones.

**Proof.** The decomposition is the image of $f = \mathrm{Re}\,f + i\,\mathrm{Im}\,f$ under the real-linear injection $\lambda$, and the skew statement is the definition. $\square$

## Positive Functionals and the Trace

**Definition.** A **positive functional** on $\mathcal{A}$ is a linear $\omega$ with $\omega(f^*\!*f)\geq0$ for all $f$; a **state** is a positive functional with $\omega$ of norm one; the **trace** of the group von Neumann algebra $L(G) = \lambda(G)''$ is $\tau(T) = \langle T\delta_e,\delta_e\rangle$ on a discrete group, extended to the finite algebra.

**Theorem (the three faces of a positive functional).** A functional $\omega$ on $\mathcal{A}$ is positive if and only if its form $B_\omega(f,g) = \omega(g^*\!*f)$ is positive semidefinite if and only if $\omega = \omega_\phi$ for a positive definite function $\phi$; the corresponding Hermitian operator is the compression $\lambda(\omega)$ acting as $\langle\lambda(f)\xi_\omega,\xi_\omega\rangle = \omega(f)$ on the GNS space, and every vector state $T\mapsto\langle T\xi,\xi\rangle$ restricts to a positive functional on $\lambda(\mathcal{A})$.

**Proof.** The three characterisations are *Hermitian Forms and the Group Algebra* and *Positive Definite Functions and the Gelfand–Raikov Theorem*; the operator description is the GNS construction, in which the cyclic vector $\xi_\omega$ realises $\omega$ as a vector state, and the restriction of a vector state is positive because $\langle\lambda(f^*\!*f)\xi,\xi\rangle = \|\lambda(f)\xi\|^2\geq0$. $\square$

**Corollary (positivity is preserved by the involution).** For a positive functional $\omega$ one has $\omega(f^*) = \overline{\omega(f)}$, and on a Hermitian element $\omega$ is real; the states on $\mathcal{A}$ are exactly the restrictions of the states of the `*`-algebra $C^*(G)$ in which $\mathcal{A}$ is dense, and the positive functionals of norm one are the states of the group.

**Proof.** $\omega(f^*) = \omega(f^*\!*1) = \overline{\omega(1^*\!*f)} = \overline{\omega(f)}$ under the Hermitian symmetry of the positive form $B_\omega$; density and the extension of a positive functional give the state correspondence. $\square$

**Remark (Hermitian operators that are not in $\lambda(\mathcal{A})$).** The Hermitian operators of the von Neumann algebra $L(G)$ are the self-adjoint elements of the weak closure of $\lambda(\mathcal{A})$; they include operators that are not of the form $\lambda(f)$ for an integrable $f$, and they are the self-adjoint operators affiliated with the group von Neumann algebra. Their spectral theory is *Operator Algebras*; the group-algebraic part, the image of $\mathcal{A}_h$, is what this article has computed.

**Remark (what the article does not do).** The adjoint of a convolution operator on its own terms, its explicit expression and the involutive algebra structure it gives are *The Adjoint of a Convolution Operator*, the last article of this group; the adjoint of a representation operator and the unitarity condition are *Unitary Representations and the Adjoint*; the adjoints of the signed operators are *The Signed Adjoint Sandwich on the Group Algebra* and its companions; the measure algebra and its involution are *The Involution on the Measure Algebra*. The left-handed adjoint $(L_a)^* = L_{a^*}$ holds for every $G$; the right-handed adjoint is stated in the unimodular case, the general right-handed picture being carried by the weighted inner product of *The Left and Right Regular Representation*.

## Summary

On a locally compact group the Haar pairing $\langle f,h\rangle = \int_Gf\overline{h}\,dx$ gives the adjoint $(L_a)^* = L_{a^*}$ of the left convolution for every $a$, and in the unimodular case the adjoints $(R_b)^* = R_{b^*}$ and $\mathrm{A}^* = \mathrm{A}$ of the right convolution and the grade-involution operator, with the adjoint an anti-linear involution $(ST)^* = T^*S^*$ on the bounded operators; the adjoint of left convolution is left convolution by the involution, not by the inverse, the two agreeing exactly for unitary elements. The map $f\mapsto\lambda(f)$ is a `*`-isomorphism of the ordered involutive algebra $\mathcal{A}$ onto its image, carrying Hermitian elements to Hermitian operators and the positive cone into the positive operators, and the Hermitian operators of $\mathcal{A}$ are the images of the Hermitian elements with the real decomposition $f = \mathrm{Re}\,f + i\,\mathrm{Im}\,f$. The positive functionals, the positive semidefinite compatible forms and the positive definite functions are the same object in three guises, each realised as a vector state on the GNS space; the states on the group algebra are the restrictions of the states of $C^*(G)$, and the Hermitian operators of the von Neumann algebra $L(G)$ extend the operator picture beyond the image of $\mathcal{A}$. The adjoints of the convolution and of the representation operators are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle f,h\rangle = \int_Gf\overline{h}\,dx$ | The Haar pairing, the $L^2(G)$ inner product |
| $T^*$ | The adjoint, $\langle Tf,h\rangle = \langle f,T^*h\rangle$ |
| $(L_a)^* = L_{a^*}$ | The adjoint of the left convolution |
| $(R_b)^* = R_{b^*}$ | The adjoint of the right convolution |
| $\mathrm{A}^* = \mathrm{A}$ | The grade-involution operator is self-adjoint |
| $\lambda(f)^* = \lambda(f^*)$ | The left regular representation is a `*`-representation |
| $f^* = f\iff\lambda(f)$ Hermitian | The operator image of the Hermitian elements |
| $\mathcal{A}^+$, $\lambda(f)\geq0$ | The positive cone and the positive operators |
| $\omega(f^*\!*f)\geq0$ | A positive functional |
| $\tau(T) = \langle T\delta_e,\delta_e\rangle$ | The trace of the group von Neumann algebra, discrete case |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for Hermitian and positive operators on a Hilbert space, the Hermitian cone and the group von Neumann algebra.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the `*`-representation $\lambda$, the positive functionals and their vector states.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint operation, the positive cone and the states of a `*`-algebra.
- Sterling K. Berberian, *Baer ${}^*$-Rings* (Springer, 1972), for Hermitian elements, their decomposition and the positive cone of an involutive algebra.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for the positive functionals on $L^1(G)$ and the positive definite functions they define.
