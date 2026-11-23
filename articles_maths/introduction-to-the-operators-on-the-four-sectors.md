# __Introduction to the Operators on the Four Sectors__

## Introduction

Three operators carry the polar word $\tilde Q=\tilde Q_H\tilde Q_0$ on the algebra: the left multiplication $L_{\tilde Q}$, the right multiplication $R_{\tilde Q}$, and the two-sided operator $\mathrm{Sd}_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q}$. This article states what they have in common: their definitions, their multiplicativity, the doubling rule that passes from the element to the two-sided operator, and the table of the four sectors. It proves nothing about a particular sector. The values of the rank, the spectrum and the Jordan type on each sector belong to the four companion articles, and the reading of the two-sided operator in a frame belongs to the two Model articles.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_k^{2}=-e_t$. The complex unit $i$ is central. The quaternionic norm is $N=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, and the vector form is $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. The Hermitian conjugation is $\tilde X^{*}=\overline{\tilde X^{\natural}}$.

**Forward pointers.** The operator theory of the two-sided operator, with its multiplicativity and its parameter modulo the central phase, is *The Hermitian Pair of Operators Acting on Two Sides*. Its reading in a frame is the congruence $X\mapsto MXM^{\dagger}$ of the entry model, and its operator reading is the composite $R_{\tilde Q^{*}}\circ L_{\tilde Q}$ of the frame-free article; the two readings agree by §*The Four Products $\lambda_i\bar\lambda_j$* of the same article. The six sector articles of this group are in the Further Reading: one one-sided and one two-sided operator article for each of the two values of $N$, four in all, and two exponential articles that read the same operators through the exponential. Inside each of the four, the two values of $B^{2}$ are two sections of one theory and not two theories: $N$ alone fixes the rank, the invertibility and the image, and $B^{2}$ alone fixes the eigenvalue count and the Jordan type.

**The two projectors of the algebra.** Two further operators belong to the same algebra of $\mathbb{C}$-linear endomorphisms, and they are not of the polar family: they are idempotent and they split every element into its centre and its vector part,

$$
P_{0}=\tfrac12\bigl(\mathrm{id}+\natural\bigr),\qquad P_{1}=\tfrac12\bigl(\mathrm{id}-\natural\bigr),\qquad P_{0}^{2}=P_{0},\quad P_{1}^{2}=P_{1},\quad P_{0}P_{1}=0,\quad P_{0}+P_{1}=\mathrm{id}.
$$

The images are the centre $\mathbb{C}e_t$ and the complexified vector part $\mathbb{C}\mathfrak{k}$, and the split is the $n=2$ case of the spin decomposition of $M_n(\mathbb{C})$, $M_n\cong\bigoplus_{k=0}^{n-1}V_k$, namely $M_2\cong V_1\oplus V_0$. It is unlike every operator below in one respect that matters: it is canonical, because it is built from the conjugation alone, with no parameter, no axis and no basis. The operators of the four sectors carry a parameter $\tilde Q$; the two projectors carry none. The decomposition is stated and proved in *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*, and both summands are invariant under $\mathrm{Sd}_{\tilde u}$ for a unit $\tilde u$, since that operator is a conjugation.

## The Three Operators

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad
R_{\tilde Q}(\tilde X)=\tilde X\tilde Q,\qquad
\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

All three are $\mathbb{C}$-linear endomorphisms of $\mathbb{B}$, read as a complex vector space of dimension four. The left multiplication is injective exactly when $\tilde Q$ is invertible: if $\tilde Q\tilde X=0$, then $\tilde X=\tilde Q^{-1}\tilde Q\tilde X=0$. For a zero divisor it has a non-trivial right annihilator, and the same argument on the other side gives the left annihilator. The two-sided operator is the composite

$$
\mathrm{Sd}_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q},
$$

and it is invertible exactly when $\tilde Q$ is invertible, with inverse $\mathrm{Sd}_{\tilde Q^{-1}}$.

The kernel of the two-sided operator is the set of $\tilde X$ with $\tilde Q\tilde X\tilde Q^{*}=0$. It contains the right annihilator $\ker L_{\tilde Q}$ and the left annihilator $\ker R_{\tilde Q^{*}}$, and it is strictly larger than either outside the group of invertibles.

## Multiplicativity

**Proposition.** For all $\tilde Q,\tilde Q'\in\mathbb{B}$,

$$
L_{\tilde Q\tilde Q'}=L_{\tilde Q}\circ L_{\tilde Q'},\qquad
R_{\tilde Q\tilde Q'}=R_{\tilde Q'}\circ R_{\tilde Q},\qquad
\mathrm{Sd}_{\tilde Q\tilde Q'}=\mathrm{Sd}_{\tilde Q}\circ\mathrm{Sd}_{\tilde Q'}.
$$

*Proof.* Each identity is the associativity of the product read at the three positions: $\tilde Q\tilde Q'\tilde X=\tilde Q(\tilde Q'\tilde X)$, $\tilde X\tilde Q\tilde Q'=(\tilde X\tilde Q)\tilde Q'$, and $\tilde Q\tilde Q'\tilde X(\tilde Q\tilde Q')^{*}=\tilde Q(\tilde Q'\tilde X\tilde Q'{}^{*})\tilde Q^{*}$. The last uses $(\tilde Q\tilde Q')^{*}=\tilde Q'{}^{*}\tilde Q^{*}$.

The order is the only difference between the three laws: the left multiplication is a representation of the multiplicative monoid, the right multiplication is an anti-representation, and the two-sided operator is a representation again because the two reversals cancel.

**Corollary.** The map $\tilde Q\mapsto L_{\tilde Q}$ is a faithful representation of $\mathbb{B}$ on itself, and $\tilde Q\mapsto\mathrm{Sd}_{\tilde Q}$ is a representation that kills the central circle on the group of invertibles. On the invertibles, $\tilde Q\mapsto L_{\tilde Q}$ is injective, with image $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$ of real dimension eight, and $\tilde Q\mapsto\mathrm{Sd}_{\tilde Q}$ has image the conformal group $CO^{+}(1,3)$, of real dimension seven, with kernel the central circle $U(1)$.

## The Doubling Rule

Write the polar word as $\tilde Q=\tilde Q_H\tilde Q_0$, with $\tilde Q_H$ Hermitian positive semidefinite and $\tilde Q_0$ a partial isometry. Multiplicativity gives at once

$$
\boxed{\;\mathrm{Sd}_{\tilde Q}=\mathrm{Sd}_{\tilde Q_H}\circ\mathrm{Sd}_{\tilde Q_0}\;}
$$

The positive factor is the modulus of the operator: $\lvert\mathrm{Sd}_{\tilde Q}\rvert=\mathrm{Sd}_{\tilde Q_H}$. On the null cone the factor $\mathrm{Sd}_{\tilde Q_H}$ acts as the scalar $4a^{2}$ on the image of $\mathrm{Sd}_{\tilde Q_0}$, so the two-sided operator collapses to a scalar times a partial isometry. Off the null cone $\mathrm{Sd}_{\tilde Q_0}$ is invertible, and the collapse occurs exactly when $\tilde Q_H$ is a scalar, that is when the element is a scalar multiple of a $*$-unitary. This is the **scalar collapse**, and its value is the **doubling**: every quantity of the element is squared when it passes to the two-sided operator.

| element | two-sided operator |
|---|---|
| scale $r$ | $r^{2}$ |
| singular value $2a$ | $4a^{2}$ |
| phase $e^{i\theta_{\mathrm{pha}}}$ | $1$ |

The scale and the singular value double. The last row is the cancellation of the central phase: $\mathrm{Sd}_{\omega\tilde Q}=\mathrm{Sd}_{\tilde Q}$ for every central unit $\omega$, because $\omega$ commutes with $\tilde X$ and $\omega\omega^{*}=1$. The doubling of the exponents $\ln r$, $\theta/2$ and $\psi/2$ is in the operator-exponential companions. On the null cone the collapse is exact and reads

$$
\mathrm{Sd}_{\tilde Q}=4a^{2}\,\mathrm{Sd}_{\tilde Q_0},\qquad
\tilde Q=2a\,\tilde Q_0,
$$

with $\tilde Q_0$ a rank-one partial isometry and $2a$ the non-zero singular value of $\tilde Q$.

## The Four Sectors

The sectors are indexed by the two vanishing conditions,

$$
\Sigma_{11}=\{N\neq0,\ B^{2}\neq0\},\quad
\Sigma_{10}=\{N\neq0,\ B^{2}=0\},\quad
\Sigma_{01}=\{N=0,\ B^{2}\neq0\},\quad
\Sigma_{00}=\{N=0,\ B^{2}=0\},
$$

the first index recording $N\neq0$ and the second $B^{2}\neq0$. On $\Sigma_{11}$ the element is invertible and $\lambda_\pm=Q_t\pm iB$ are the eigenvalues of $\tilde Q$, with $B$ a root of $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. On $\Sigma_{01}$ the element is $\tilde Q=c\tilde\Pi_{\mathrm{id}}$ with $c=2Q_t\neq0$ and $\tilde\Pi_{\mathrm{id}}$ a non-trivial idempotent. On $\Sigma_{10}$ it is $\tilde Q=Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}^{2}=0$; the scalar line $\vec\Pi_{\mathrm{nil}}=0$ is written $\Sigma_{10}^{\mathrm{s}}$, the Jordan part $\vec\Pi_{\mathrm{nil}}\neq0$ is $\Sigma_{10}^{\mathrm{J}}$. On $\Sigma_{00}$ it is a non-zero nilpotent $\tilde\pi_{\mathrm{nil}}$, with $\tilde\Pi_{\mathrm{id},\pm}$ the canonical Hermitian idempotents and $\tilde\pi_{\mathrm{nil}}=\tilde\Pi_{\mathrm{id},+}\tilde\pi_{\mathrm{nil}}\tilde\Pi_{\mathrm{id},-}$.

**The one-sided operators.**

| sector | rank | spectrum | Jordan type | image of $L_{\tilde Q}$ | image of $R_{\tilde Q}$ |
|---|---|---|---|---|---|
| $\Sigma_{11}$ | $4$ | $\lambda_+,\lambda_-$, each twice | diagonal, $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\Sigma_{10}^{\mathrm{s}}$ | $4$ | $Q_t$, algebraic multiplicity $4$, geometric $4$ | diagonal, $\operatorname{diag}(Q_t,Q_t,Q_t,Q_t)$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\Sigma_{10}^{\mathrm{J}}$ | $4$ | $Q_t$, algebraic multiplicity $4$, geometric $2$ | $J_2(Q_t)\oplus J_2(Q_t)$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\Sigma_{01}$ | $2$ | $c,0$, multiplicities $2,2$ | diagonal, $\operatorname{diag}(c,c,0,0)$ | the totally isotropic plane $\tilde Q\mathbb{B}$ | the totally isotropic plane $\mathbb{B}\tilde Q$ |
| $\Sigma_{00}$ | $2$ | $0$, algebraic multiplicity $4$, geometric $2$ | $J_2(0)\oplus J_2(0)$ | $\mathbb{C}\tilde\pi_{\mathrm{nil}}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},+}=\ker L_{\tilde\pi_{\mathrm{nil}}}$ | $\mathbb{C}\tilde\pi_{\mathrm{nil}}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},-}=\ker R_{\tilde\pi_{\mathrm{nil}}}$ |

The two image columns differ on the null strata. On $\Sigma_{01}$ the planes $\tilde Q\mathbb{B}$ and $\mathbb{B}\tilde Q$ are distinct and meet in $\mathbb{C}\tilde\Pi_{\mathrm{id}}$; on $\Sigma_{00}$ the two planes are distinct and meet in $\mathbb{C}\tilde\pi_{\mathrm{nil}}$. On $\Sigma_{11}$ and $\Sigma_{10}$ both images are the whole algebra.

**The two-sided operator.**

| sector | rank | spectrum | Jordan type | image |
|---|---|---|---|---|
| $\Sigma_{11}$ | $4$ | $\lambda_i\bar\lambda_j$, $i,j\in\{+,-\}$ | semisimple, eigenvalues $\lambda_i\bar\lambda_j$ | $\mathbb{B}$ |
| $\Sigma_{10}^{\mathrm{s}}$ | $4$ | $\lvert Q_t\rvert^{2}$, algebraic multiplicity $4$, geometric $4$ | diagonal, $\operatorname{diag}(\lvert Q_t\rvert^{2},\lvert Q_t\rvert^{2},\lvert Q_t\rvert^{2},\lvert Q_t\rvert^{2})$ | $\mathbb{B}$ |
| $\Sigma_{10}^{\mathrm{J}}$ | $4$ | $\lvert Q_t\rvert^{2}$, algebraic multiplicity $4$, geometric $2$ | $J_3(\lvert Q_t\rvert^{2})\oplus J_1(\lvert Q_t\rvert^{2})$ | $\mathbb{B}$ |
| $\Sigma_{01}$ | $1$ | $\lvert c\rvert^{2},0$, multiplicities $1,3$ | diagonal, $\operatorname{diag}(\lvert c\rvert^{2},0,0,0)$ | the null line $\mathbb{C}P$, $P=\tilde Q\tilde Q^{*}/(4a^{2})$ |
| $\Sigma_{00}$ | $1$ | $0$, algebraic multiplicity $4$, geometric $3$ | $J_2(0)\oplus0\oplus0$ | the null line $\mathbb{C}\tilde\Pi_{\mathrm{id},+}$ |

The two tables are the whole sector theory in one page. Along each row the rank drops when $N=0$, and the Jordan type leaves the semisimple case when $B^{2}=0$; on the scalar line $\Sigma_{10}^{\mathrm{s}}$ the element is central and the operator is a scalar multiple of the identity, so the defective types belong to the Jordan part alone. Along each column the two-sided operator replaces the one-sided eigenvalue $\lambda_i$ by the product $\lambda_i\bar\lambda_j$, so it loses one factor of the spectrum.

## Summary

The polar word carries three operators on the algebra: the left multiplication $L_{\tilde Q}$, the right multiplication $R_{\tilde Q}$, and the two-sided operator $\mathrm{Sd}_{\tilde Q}=R_{\tilde Q^{*}}L_{\tilde Q}$. All three are $\mathbb{C}$-linear; the one-sided maps are injective exactly on the invertibles, the two-sided operator is invertible exactly on the invertibles, and its kernel is the set of $\tilde X$ with $\tilde Q\tilde X\tilde Q^{*}=0$. The three are multiplicative, with the order reversed on the right and restored on the two-sided operator; the two-sided operator kills the central phase and squares the scale and the singular value. The four sectors, indexed by $N$ and $B^{2}$, give the rank, the spectrum and the Jordan type of the three operators; the two-sided operator spectrum is the four products $\lambda_i\bar\lambda_j$. The operator theory of the two-sided operator, with its multiplicativity and its parameter modulo the central phase, is *The Hermitian Pair of Operators Acting on Two Sides*; its readings in a frame are the two Model articles; the six sector articles are the four operator articles and the two exponential articles in the Further Reading.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde Q},R_{\tilde Q}$ | left and right multiplication by $\tilde Q$ |
| $\mathrm{Sd}_{\tilde Q}$ | the two-sided operator $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ |
| $N=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, $Q_t^{2}+B^{2}$ |
| $B^{2}$ | the vector form $Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $\Sigma_{\varepsilon\eta}$ | $\varepsilon=1$ if $N\neq0$, $\eta=1$ if $B^{2}\neq0$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues of $\tilde Q$ on $\Sigma_{11}$ |
| $\tilde Q=c\tilde\Pi_{\mathrm{id}}$ | the form of the element on $\Sigma_{01}$ |
| $\tilde Q=Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ | the form of the element on $\Sigma_{10}$, $\vec\Pi_{\mathrm{nil}}^{2}=0$ |
| $\Sigma_{10}^{\mathrm{s}}$, $\Sigma_{10}^{\mathrm{J}}$ | the scalar line $\vec\Pi_{\mathrm{nil}}=0$ and the Jordan part $\vec\Pi_{\mathrm{nil}}\neq0$ of $\Sigma_{10}$ |
| $a$ | the half singular value, $\tilde Q=2a\tilde Q_0$ on the null cone |

## Further Reading

- [One-Sided Operators on the N-Regular Sector](one-sided-operators-on-the-n-regular-sector.html) and [Two-Sided Operators on the N-Regular Sector](two-sided-operators-on-the-n-regular-sector.html), for the unit case: the four factors, the half-spin, the doubling rule, the conformal image, and the wall $B^{2}=0$ with the Jordan types $2+2$ and $3+1$.
- [One-Sided Operators on the N-Regular Sector](one-sided-operators-on-the-n-regular-sector.html) and [Two-Sided Operators on the N-Regular Sector](two-sided-operators-on-the-n-regular-sector.html), §*The Exponential of the One-Sided Operator* and §*The Exponential of the Two-Sided Operator*, for the one-parameter groups, the doubling of the exponents, and the shear and the null rotation at the wall.
- [One-Sided Operators on the N-Degenerate Sector](one-sided-operators-on-the-n-degenerate-sector.html) and [Two-Sided Operators on the N-Degenerate Sector](two-sided-operators-on-the-n-degenerate-sector.html), for the null cone: the rank-one polar pair, the oblique projection on $\Sigma_{01}$ and the single chain on $\Sigma_{00}$.
- [Operators Acting on One Side](operators-acting-on-one-side.html), for $L$ and $R$ frame-free, the two laws, the rank trichotomy $4,2,0$ and the commutant.
- [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html), for the two-sided operator as an operator, its multiplicativity, its norm and its parameter modulo the central phase.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the polar word itself.
