# __The Adjoint of the Left Multiplication on a Hilbert Space__

## Introduction

The left multiplication of a Hilbert space is the operator $L_U(T)=UT$ on the Hilbert–Schmidt space, and the form of the category with respect to which its adjoint is taken is the Hilbert–Schmidt inner product $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$. The adjoint of the left multiplication is again a left multiplication,

$$
(L_U)^*=L_{U^*},
$$

so the adjoint stays on the side it started from, and the map $U\mapsto L_U$ is a $*$-representation of the algebra on its own Hilbert–Schmidt space: it is multiplicative, isometric and compatible with the involution. This is the property that the present article computes and explores; it is the operator-theoretic counterpart of the identity $L_x^*=L_{x^{\dagger}}$ of the Hilbert algebra, and it is the reason the left multiplications form a self-adjoint family. The computation is carried by the rank-one operators, on which the left multiplication simply shifts the left vector, and the same computation gives the adjoint of the right multiplication, $R_V^*=R_{V^*}$, and the adjoints of the two-sided sandwich in the signed case, which is flagged below.

This article fixes the Hilbert–Schmidt form, the adjoint of the left multiplication and its explicit value on the rank-one operators, the self-adjointness, normality, unitarity and positivity criteria that the identity produces, the $*$-representation structure and the commutant, and the passage to the signed left multiplication. The two-sided multiplication algebra is *The Left and Right Multiplication Operators on a Hilbert Space*, where the rank-one decomposition and the Hilbert–Schmidt form are established; the bounded operators and their adjoints are *Bounded Operators on a Hilbert Space*; the Hilbert-Schmidt class is *Compact Operators*; the signed left multiplication is *The Signed Left Multiplication on a Hilbert Space*, and its adjoint is *The Signed Adjoint of the Left Multiplication on a Hilbert Space* below; the two-sided signed adjoint is *The Signed Adjoint Sandwich on a Hilbert Space*; the Hilbert-algebra form of the same identity, with the Tomita operator, is *The Adjoint of the Left Multiplication on a Hilbert Algebra* (Part II).

Throughout, $H$ is a Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ with inner product linear in the first argument, $S_2(H)$ is the Hilbert–Schmidt class with the inner product $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$, $B(H)$ acts on $S_2(H)$ by $L_U(T)=UT$ and $R_V(T)=TV$, and the adjoint with respect to $\langle\cdot,\cdot\rangle_{\mathrm{HS}}$ is written with a star. The rank-one operator is $\xi\otimes\bar\eta:\zeta\mapsto\langle\zeta,\eta\rangle\xi$, and the **involution** on the elements is $U\mapsto U^*$.

## The Hilbert–Schmidt Form and the Adjoint

**Definition.** On the Hilbert–Schmidt class $S_2(H)$ the **Hilbert–Schmidt form** is

$$
\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*),
$$

linear in the first argument and conjugate-linear in the second; it is an inner product, and $S_2(H)$ is a Hilbert space in it. The **adjoint** of a bounded operator is taken with respect to this form.

**Theorem (the adjoint of the left multiplication).** For every $U\in B(H)$ the left multiplication $L_U$ is bounded on $S_2(H)$ and

$$
(L_U)^*=L_{U^*},
$$

so the adjoint of a left multiplication is the left multiplication by the adjoint; the same computation gives $R_V^*=R_{V^*}$ for the right multiplication, and each one-sided family is closed under the adjunction.

*Proof.* The adjoint identity follows from the trace identity: $\langle L_UT,S\rangle_{\mathrm{HS}}=\operatorname{tr}(UTS^*)=\operatorname{tr}(T(U^*S)^*)=\langle T,U^*S\rangle_{\mathrm{HS}}=\langle T,L_{U^*}S\rangle_{\mathrm{HS}}$; the right case is $\operatorname{tr}(TVS^*)=\operatorname{tr}(T(SV^*)^*)$; uniqueness of the Hilbert adjoint and the density of $S_2(H)$ in the operators of the form give the identities for all elements.

**Proposition (boundedness and the rank-one expression).** For all $U$ and $\xi,\eta\in H$,

$$
L_U(\xi\otimes\bar\eta)=(U\xi)\otimes\bar\eta,\qquad R_V(\xi\otimes\bar\eta)=\xi\otimes\bar{V^*\eta},
$$

and the adjoint is computed on rank-one operators by transposing the vector:

$$
\langle L_U(\xi\otimes\bar\eta),\zeta\otimes\bar\kappa\rangle_{\mathrm{HS}}
=\langle U\xi,\zeta\rangle\langle\kappa,\eta\rangle
=\langle \xi\otimes\bar\eta,L_{U^*}(\zeta\otimes\bar\kappa)\rangle_{\mathrm{HS}} .
$$

*Proof.* The rank-one action is the computation $UT=U(\xi\otimes\bar\eta)$, and for the right multiplication $(\xi\otimes\bar\eta)V=\xi\otimes\bar\eta\circ V$ gives the transpose formula; the adjoint pairing is the trace of the product of two rank-one operators, $\operatorname{tr}((\xi\otimes\bar\eta)(\zeta\otimes\bar\kappa)^*)=\langle\xi,\zeta\rangle\langle\kappa,\eta\rangle$.

**Corollary (the multiplications are isometric and multiplicative).** The maps $U\mapsto L_U$ and $V\mapsto R_V$ are linear, multiplicative and isometric: $\|L_U\|=\|U\|$, $\|R_V\|=\|V\|$, and the two families commute, $L_UR_V=R_VL_U$.

*Proof.* The norm identity is $\|UT\|_{\mathrm{HS}}\le\|U\|\|T\|_{\mathrm{HS}}$ with equality at a rank-one operator for which the vector is aligned with $U$; multiplicativity is associativity, and the commutativity is $U(TV)=(UT)V$.

## Self-Adjointness, Normality and the Order

**Theorem (criteria for a left multiplication).** For $U\in B(H)$:

(i) $L_U$ is self-adjoint exactly when $U$ is self-adjoint;

(ii) $L_U$ is normal exactly when $U$ is normal;

(iii) $L_U$ is unitary exactly when $U$ is unitary;

(iv) $L_U$ is positive exactly when $U$ is positive;

(v) $L_U$ is an orthogonal projection exactly when $U$ is an orthogonal projection.

*Proof.* (i) $L_U^*=L_{U^*}$ equals $L_U$ iff $U^*=U$, the map being injective. (ii) $L_UL_U^*=L_{UU^*}$ and $L_U^*L_U=L_{U^*U}$ coincide iff $UU^*=U^*U$. (iii) $(L_U)^*L_U=L_{U^*U}$ is the identity iff $U^*U=I$, and $L_UL_U^*=I$ iff $UU^*=I$; the identity of $S_2(H)$ is $L_I$. (iv) $L_U$ is positive iff it is self-adjoint, so $U$ is, and $\langle L_UT,T\rangle_{\mathrm{HS}}=\operatorname{tr}(UTT^*)=\operatorname{tr}(T^*UT)$ is nonnegative for all $T$ iff $U\ge0$. (v) An orthogonal projection is a positive idempotent; $L_U^2=L_{U^2}$ is $L_U$ iff $U^2=U$, and the positivity is (iv).

**Proposition (the adjoint and the involution).** The involution $U\mapsto U^*$ on the elements and the adjunction on the operators agree under the representation:

$$
(L_U)^*=L_{U^*},\qquad (R_V)^*=R_{V^*},
$$

so the two representations are $*$-representations of $B(H)$ (and of its opposite) on $S_2(H)$, and the compatibility of the involution with the multiplications, $(UV)^*=V^*U^*$, is the compatibility of the adjunction with the composition, $(L_UL_V)^*=(L_V)^*(L_U)^*$.

*Proof.* The two identities are the theorem; passing to adjoints reverses the order of a product, $(L_UL_V)^*=L_V^*L_U^*$, which is the operator form of the anti-multiplicativity of the involution.

**Corollary (the commutation theorem for one side).** The commutant of $\{L_U:U\in B(H)\}$ in $B(S_2(H))$ contains the right multiplications $R_V$, and in finite dimension it is exactly the algebra generated by them; consequently $\{L_U:U\in B(H)\}'=\{R_V\}$, and the double commutant is $\{L_U\}$.

*Proof.* The first containment is the commutativity of the two families; in finite dimension the multiplication algebra generated by the two families is the whole of $B(M_n(\mathbb{K}))$ via the identification $M_n\cong\mathbb{K}^n\otimes\mathbb{K}^n$, and the commutant of the left family is the right family by the standard double-commutant computation, which gives the second identity and, applying it twice, the third.

## The Signed Case

**Proposition (the signed left multiplication to be adjointed).** With the same form, the signed left multiplication of the graded Hilbert space, $\ell_U=L_U\circ\alpha$, has adjoint

$$
(\ell_U)^*=\alpha\,L_{U^*}=\ell_{\alpha(U^*)},
$$

because the grade involution is a $*$-automorphism and is self-adjoint for the Hilbert–Schmidt form, $\alpha^*=\alpha$; so the adjoint of a signed left multiplication is again a signed left multiplication, and the explicit computation is *The Signed Adjoint of the Left Multiplication on a Hilbert Space* below.

*Proof.* $(L_U\alpha)^*=\alpha^*L_U^*=\alpha L_{U^*}$, and $\alpha L_{U^*}=\alpha L_{U^*}$ acts by $X\mapsto\alpha(U^*X)=\alpha(U^*)\alpha(X)$, which is $\ell_{\alpha(U^*)}$; the self-adjointness of $\alpha$ is $\langle\alpha X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(\Gamma X\Gamma Y^*)=\operatorname{tr}(X\Gamma Y^*\Gamma)=\langle X,\alpha Y\rangle_{\mathrm{HS}}$.

**Forward reference.** The two-sided adjoint, the sandwich $S_{A,B}=L_A\varrho_B=\ell_AR_{\alpha(B)}$ and its adjoint $S_{\alpha(A^*),\alpha(B^*)}$, the unitarity condition they define, and the reflection case are *The Signed Adjoint Sandwich on a Hilbert Space* and *The Signed Adjoint of the Reflection on a Hilbert Space*, written in parallel; the graded-module adjoint action is *The Graded Adjoint Action on a Module over a Hilbert Space*. Nothing of those is used here.

**Example (the finite-dimensional picture).** For $H=\mathbb{K}^n$ identify $S_2(H)$ with $M_n(\mathbb{K})$ and the Hilbert–Schmidt form with $\langle S,T\rangle=\operatorname{tr}(ST^*)$; then $L_U$ is the operator $T\mapsto UT$, the adjoint is $T\mapsto U^*T$, and the matrix of $L_U$ in the standard basis is $U\otimes I$. The self-adjointness of $L_U$ is the self-adjointness of $U$, and the eigenvalues of $L_U$ are the eigenvalues of $U$ each repeated $n$ times, so the spectral picture of the multiplication is read from the element.

**Example (rank-one vectors and the shift).** On a rank-one operator, $L_U$ shifts only the left vector and keeps the right one, $L_U(\xi\otimes\bar\eta)=(U\xi)\otimes\bar\eta$; the adjoint shifts the same vector back by $U^*$, and iterating gives $L_U^n(\xi\otimes\bar\eta)=(U^n\xi)\otimes\bar\eta$. The rank-one decomposition thus carries the adjoint, the powers and the whole functional calculus of $L_U$ back to the element $U$.

## Summary

With respect to the Hilbert–Schmidt form $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$, the left multiplication $L_U(T)=UT$ has adjoint $(L_U)^*=L_{U^*}$ and the right multiplication $R_V(T)=TV$ has adjoint $R_V^*=R_{V^*}$, so both one-sided families are closed under adjunction and stay on their side. The representation $U\mapsto L_U$ is linear, multiplicative and isometric, it is a $*$-representation in the sense that it carries the involution of the elements, $U\mapsto U^*$, to the adjunction of the operators, and the two families $L(B(H))$ and $R(B(H))$ commute; the commutant of each is the other, and the double commutant is the family itself. Consequently self-adjointness, normality, unitarity, positivity and projectionness of $L_U$ are exactly the corresponding properties of $U$, and the rank-one operators carry the adjoint and the powers to the element by shifting one vector. The signed left multiplication $\ell_U=L_U\alpha$ has adjoint $(\ell_U)^*=\ell_{\alpha(U^*)}$, again on the left, which is the first step of the signed adjoint theory developed in *The Signed Adjoint of the Left Multiplication on a Hilbert Space* and its companions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_2(H)$ | the Hilbert–Schmidt class |
| $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$ | the Hilbert–Schmidt form |
| $L_U(T)=UT$, $R_V(T)=TV$ | the left and right multiplications |
| $(L_U)^*=L_{U^*}$ | adjoint of the left multiplication |
| $R_V^*=R_{V^*}$ | adjoint of the right multiplication |
| $\alpha(T)=\Gamma T\Gamma$, $\alpha^*=\alpha$ | the grade involution, self-adjoint for the form |
| $(\ell_U)^*=\ell_{\alpha(U^*)}$ | adjoint of the signed left multiplication |
| $\xi\otimes\bar\eta$ | the rank-one operator |
| $L_U(\xi\otimes\bar\eta)=(U\xi)\otimes\bar\eta$ | the rank-one action |
| $\{L_U\}'=\{R_V\}$ | the commutation theorem |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the multiplication operators on $B(H)$ and their adjoints.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the Hilbert–Schmidt space and the elementary operators.
- Barry Simon, *Trace Ideals and Their Applications*, Mathematical Surveys and Monographs 120 (American Mathematical Society, 2nd ed. 2005), for the trace form and the rank-one decomposition.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the adjoint of a multiplication and the commutant computations.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the $*$-representations and the commutation theorem of the multiplications.
