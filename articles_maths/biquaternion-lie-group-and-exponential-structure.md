# __Biquaternion Lie Group and Exponential Structure__

## Introduction

The group of units $\mathbb{B}^\times$ is a real Lie group, and its exponential map is the bridge between the group and the Lie algebra *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. This article reads the Lie-group structure: the exponential and its parametrisation of the group, the cases of the exponential, the group law, the failure of surjectivity, and the real forms and subgroups the group carries.

The exponential itself — its series, its closed form, the logarithm and the power functions — is computed in *Biquaternion Elementary Functions*, and only its group-theoretic consequences are used here; the Lie algebra is in Algebra, and the topology of the group is in *The Biquaternion Unit Group as a Topological Group*. 

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Unit Quaternions and Their Complexification

The **unit quaternions** are the elements of $\mathbb{H}_{\mathbb{B}}$ of norm $1$:

$$
S^3 = \{\tilde q \in \mathbb{H}_{\mathbb{B}} : N(\tilde q) = 1\},
$$

a compact, connected, simply connected real Lie group of real dimension $3$. Every such $\tilde q$ is $\cos\theta\, e_0 + \sin\theta\, \hat{n}$ with $\hat{n}$ a real unit vector part, the quaternion exponential.

Complexifying the coefficients turns $N(\tilde q) = 1$ into the same equation over $\mathbb{C}$, giving the **unit-norm subgroup**

$$
\mathbb{B}^\times_1 = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) = 1\},
$$

whose elements need not be real quaternions.

**Dimension.** The level set $N = 1$ has complex dimension $3$ and real dimension $6$, the biquaternion norm being a submersion wherever $N(\tilde{Q}) \neq 0$. The group $\mathbb{B}^\times_1$ is connected, simply connected, and non-compact, and it is the **complexification of the unit quaternions**: the trace-free subalgebra satisfies $\mathrm{B}_0 = \mathrm{K} \otimes_{\mathbb{R}} \mathbb{C}$ for the compact subalgebra $\mathrm{K}$ below, and $\mathbb{B}^\times_1$ complexifies the compact group $S^3$. Its center is

$$
Z(\mathbb{B}^\times_1) = \{\pm e_0\} \cong \mathbb{Z}/2.
$$

## The Subgroups and the Real Forms

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the unit quaternions $S^3$ (real dimension $3$); and the center $\mathbb{C}^\times e_0$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$S^3$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact subalgebra $\mathrm{K}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Trace-Free Subalgebra*. The center $\{\pm e_0\}$ is discrete, so the quotient $\mathbb{B}^\times_1/\{\pm e_0\}$ is a Lie group of real dimension $6$.

## The Unitary Subgroup and the Defining Module

The algebra acts on the defining module $\mathbb{C}^2$ by the defining representation, in which a biquaternion acts as its $2\times2$ matrix $\Phi(\tilde{Q})$ (*Biquaternion 2×2 Matrix Element Representation*). The elements that preserve the standard Hermitian form of $\mathbb{C}^2$ are exactly those with $\tilde{Q}^{*}\tilde{Q}=e_0$, and they form a compact subgroup of the group of units,
$$
U(2)=\{\tilde{Q}\in\mathbb{B}^{\times}:\tilde{Q}^{*}\tilde{Q}=e_0\},
$$
of real dimension $4$. The determinant-one elements inside it are the unit quaternions:
$$
U(2)\cap SL(2,\mathbb{C})=S^3=SU(2),
$$
consistently with the unit quaternions being the unitary part of the norm-one group. Every element of $U(2)$ is the product of a unit quaternion and a unit complex scalar, and the two factors meet in $\{\pm e_0\}$:
$$
U(2)=S^3\cdot U(1)\cong (SU(2)\times U(1))/\{\pm(1,1)\}.
$$

**Proof.** If $\tilde{Q}\in U(2)$ then $|\det\Phi(\tilde{Q})|=1$, so $P=\tilde{Q}\,(\det\Phi(\tilde{Q}))^{-1/2}\in U(2)$ has determinant one, hence lies in $S^3$ by the identification of the determinant-one unitary elements with the unit quaternions; the scalar $(\det\Phi(\tilde{Q}))^{1/2}$ is a unit complex number. The intersection $\{\pm e_0\}$ is the set of scalars $\lambda e_0$ of determinant $\lambda^2=1$, and the kernel of $S^3\times U(1)\to U(2)$, $(\tilde q,\lambda)\mapsto\lambda\tilde q$, is $\{\pm(1,1)\}$.

**Remark.** The norm-one group $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$ is strictly larger: it acts on the defining module too, but it does not preserve the Hermitian form, and unlike $U(2)$ it is non-compact.

## The Enlarged Carrier and the Closed Forms for SU(3) and SU(4)

The groups the algebra reaches directly are $SU(2)=S^3$ and the compact $U(2)$ above, and the ceiling recorded in the physics article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* is the statement that no octet of generators with an $\mathfrak{su}(3)$ bracket sits **inside** $\mathbb{B}$. Classical closed forms for $SU(3)$ and $SU(4)$ in terms of biquaternions nevertheless exist, and they cost exactly one enlargement of the carrier: not the algebra but the matrices over the algebra.

**Definition (matrices over the algebra).** Let $M_n(\mathbb{B})$ be the $\mathbb{C}$-algebra of $n\times n$ matrices with entries in $\mathbb{B}$, acting on $\mathbb{B}^n$. The identification $\mathbb{B}\cong M_2(\mathbb{C})$ extends entrywise, so

$$
M_n(\mathbb{B})\cong M_n(M_2(\mathbb{C}))\cong M_{2n}(\mathbb{C}),\qquad
\dim_{\mathbb{C}}M_n(\mathbb{B})=4n^2 .
$$

In particular $M_3(\mathbb{B})\cong M_6(\mathbb{C})$ contains $\mathfrak{u}(3)$ and hence $\mathfrak{su}(3)$, with its eight generators written as $3\times3$ matrices of biquaternions. This realises the ceiling's answer: the octet is not in $\mathbb{B}$, and it *is* in $M_3(\mathbb{B})$, for the price of enlarging the carrier by the factor $2$ in each matrix direction. Since $\mathbb{B}\hookrightarrow M_3(\mathbb{B})$ by the scalar matrices, the chain is $\mathfrak{su}(2)=\mathfrak{k}\subset\mathfrak{su}(3)\subset\mathfrak{u}(3)\subset M_3(\mathbb{B})$.

The closed forms use the Conway operator calculus of *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Conway Operator Basis*: $a[\,]b$ is the linear function $\tilde{Q}\mapsto a\tilde{Q}b$, $\odot$ is composition, $D\{d_1,d_2,d_3\}=\frac12\sum_kd_ke_k[\,]e_k$, and for a unit vector $\mathbf b$ each of the generators $b[\,]b$ and $e_k[\,]e_k$ has square the identity, $(b[\,]b)^2=(e_k[\,]e_k)^2=[\,]$, so their exponentials are trigonometric.

**Proposition (the three exponentials).** $\mathrm{EXP}$ denoting the exponential series of a linear function, for real $\alpha$, $\beta$ and $\delta_k$,

$$
\mathrm{EXP}\Bigl(\tfrac{\alpha}{2}\bigl(a[\,]-[\,]a\bigr)\Bigr)=\exp\bigl(\tfrac{\alpha}{2}a\bigr)[\,]\exp\bigl(-\tfrac{\alpha}{2}a\bigr),
$$

$$
\mathrm{EXP}\bigl(iD\{\delta_1,\delta_2,\delta_3\}\bigr)
=\underset{k=1}{\overset{3}{\odot}}\exp\Bigl(\delta_k\tfrac{i}{2}e_k[\,]e_k\Bigr),
\qquad
\mathrm{EXP}\Bigl(\tfrac{i\beta}{2}\,b[\,]b\Bigr)=\cos\tfrac{\beta}{2}\,[\,]+i\sin\tfrac{\beta}{2}\,b[\,]b .
$$

*Proof.* The first is the Olinde–Rodrigues formula, verified residual $5.8\times10^{-16}$; for the second and third the squares of the generators are the identity, $(b[\,]b)^2=[\,]$ and $(e_k[\,]e_k)^2=[\,]$, so the series collapses to cosine and sine, verified residuals $1.7\times10^{-15}$ and $1.0\times10^{-15}$. The signs of the imaginary units are the ones that make the results compact for real parameters: $D$ carries $i$ and $b[\,]b$ carries $i$, while the antisymmetric function carries none.

**Theorem (Lie-type forms for $\mathrm{SU}(3)$, $\mathrm{SL}(3,\mathbb{R})$ and $\mathrm{SL}(3,\mathbb{C})$).** For real $\alpha,\beta,\delta_1,\delta_2$, with $\mathbf a$ and $\mathbf b$ unit vectors and $\delta_1+\delta_2+\delta_3=0$, every element of $\mathrm{SU}(3)$ is

$$
G=\exp\Bigl(\tfrac{\beta}{2}i\,b[\,]b\Bigr)\odot\exp\Bigl(\tfrac{\alpha}{2}\bigl(a[\,]-[\,]a\bigr)\Bigr)
\odot\exp\Bigl(iD\{\delta_1-\beta b_1^2,\ \delta_2-\beta b_2^2,\ \delta_3-\beta b_3^2\}\Bigr),
$$

with the eight independent parameters $\alpha,\beta,\delta_1,\delta_2$ and the four angles in the two unit vectors. Suppressing the imaginary units gives the same formula for $\mathrm{SL}(3,\mathbb{R})$ when all parameters are real, and for $\mathrm{SL}(3,\mathbb{C})$ when they are complex. Verified: for $100$ random parameter sets the $4\times4$ matrix of $G$ is unitary with $|\det G-1|<4\times10^{-15}$.

**Theorem (Euler-angles forms).** With unit vectors $\mathbf a,\mathbf b,\mathbf c,\mathbf d,\mathbf u,\mathbf v,\mathbf w$ and real angles,

$$
U_{\mathrm{SU}(3)}=\exp\bigl(\tfrac{\alpha}{2}a\bigr)[\,]\exp\bigl(-\tfrac{\alpha}{2}a\bigr)
\odot\exp\bigl(iD\{\beta,\gamma,-\beta-\gamma\}\bigr)
\odot\exp\bigl(\tfrac{\delta}{2}b\bigr)[\,]\exp\bigl(-\tfrac{\delta}{2}b\bigr),
$$

$$
U_{\mathrm{SU}(4)}=\exp\bigl(\tfrac{\alpha}{2}a\bigr)[\,]\exp\bigl(-\tfrac{\beta}{2}b\bigr)
\odot\exp\bigl(iD\{\gamma,\delta,\epsilon\}\bigr)
\odot\exp\bigl(\tfrac{\psi}{2}c\bigr)[\,]\exp\bigl(-\tfrac{\eta}{2}d\bigr),
$$

and, in the degenerate case in which the outer unit vectors coincide, an $\mathrm{SU}(2)$ element,

$$
U_{\mathrm{SU}(2)}=\exp\bigl(\tfrac{\alpha}{2}w\bigr)[\,]\exp\bigl(-\tfrac{\alpha}{2}w\bigr)
\odot\exp\Bigl(\tfrac{i\beta}{2}\bigl(u[\,]u-v[\,]v\bigr)\Bigr)
\odot\exp\bigl(\tfrac{\gamma}{2}w\bigr)[\,]\exp\bigl(-\tfrac{\gamma}{2}w\bigr).
$$

Each **outer** factor is a conjugation of the argument by a single unit vector, $e^{\theta}[\,]e^{-\theta}$; the $\mathrm{SU}(3)$ form has two of them, with unit vectors $\mathbf a$ and $\mathbf b$ and the four angles they carry, and its middle factor is a traceless diagonal $D\{\beta,\gamma,-\beta-\gamma\}$. The $\mathrm{SU}(4)$ form pairs **different** vectors in each outer factor, $\exp(\tfrac\alpha2a)[\,]\exp(-\tfrac\beta2b)$ and $\exp(\tfrac\psi2c)[\,]\exp(-\tfrac\eta2d)$, and its middle factor carries three diagonal parameters $\gamma,\delta,\epsilon$ with no trace condition: that is $7$ scalar parameters and $8$ angles, the fifteen parameters of $\mathrm{SU}(4)$. Verified: unitary with unit determinant in all three cases, residuals below $4\times10^{-15}$ over $100$ random parameter sets.

**Remark (the inverse).** The inverse of any of these elements is obtained by reversing the order of the factors and changing the signs of the exponents, and it equals the biconjugate of the function,
$$G^{-1}=G^{+\approx}=G^{\dagger},$$
the source's rule, which is the statement of *Association and the Transpose on the Biquaternion Algebra*: for an operator that fixes $e_0$ and preserves the span of $e_1,e_2,e_3$ — as every element here does — the conjugation by the Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ of the scalar form is invisible, and association followed by conjugation of the coefficients is the Hermitian adjoint. For a general linear function the two involutions differ, and the corpus keeps them apart.

**Remark (the elements are block-diagonal).** Every element above fixes $e_0$ and preserves the span of $e_1,e_2,e_3$: in the coordinate order $(e_1,e_2,e_3,e_0)$ its matrix is $\operatorname{diag}(U_3,1)$ with $U_3\in\mathrm{SU}(3)$ the $3\times3$ block. Verified: the entries mixing the scalar slot with the vector slots vanish exactly, and the $3\times3$ block has determinant one on the nose. This is the structural reason the enlargement is needed and the ceiling is honest: the octet acts on a three-dimensional **complex** space, whereas the algebra's own action on $\mathbb{B}$ is four-dimensional over $\mathbb{C}$ with the scalar direction inert, so the eight generators have no home in $\mathbb{B}$ itself.

**Remark (where the method ends).** The construction does not generalise directly to $n>4$: the diagonal and antisymmetric functions have bounded room, and the source records that the quaternion expression of the general diagonal-less symmetric matrix of the required size becomes cumbersome and loses its use, which is the same observation as the *Limit of the Method* remark of the enveloping-algebra article. The endpoint is the pair $3,4$, which is also the endpoint of the physics programme's need.

## Surjectivity and Its Failure for the Subgroups

The exponential of the full unit group is surjective (*Biquaternion Elementary Functions*, §*The Logarithm*), but the two distinguished subgroups behave differently.

**The compact subgroup: surjective.** Every unit quaternion is $\cos\theta\, e_0 + \sin\theta\,\hat{n} = \exp(\theta\hat{n})$, so $\exp : \mathrm{K} \to S^3$ is surjective; this is the general fact that a connected compact Lie group has a surjective exponential map.

**The full group: not surjective.** The exponential $\exp : \mathrm{B}_0 \to \mathbb{B}^\times_1$ is **not** surjective: $\mathbb{B}^\times_1$ is not exponential. The element of $\mathbb{B}^\times_1$ with scalar part $-1$ and non-semi-simple behaviour, corresponding to the non-diagonalizable norm-one element with the repeated eigenvalue $-1$, is

$$
\tilde{Q} = -e_0 + \frac{i}{2}e_1 - \frac{1}{2}e_2, \qquad N(\tilde{Q}) = 1 + \left(\frac{i}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 = 1.
$$

Its scalar part is $Q_0 = -1$ and its vector part has $B = 0$, so the element is non-semi-simple with the repeated eigenvalue $-1$. If $\tilde{Q} = \exp(\tilde{R})$ with $\tilde{R} \in \mathrm{B}_0$, then $R_0 = 0$, and $\tilde{R} = \mu e_0 + \tilde{N}$ with $\tilde{N}$ nilpotent and $e^\mu = -1$, hence $\mu \in i\pi(2\mathbb{Z}+1)$ and $\mathrm{Tr}(\tilde{R}) = 2\mu \neq 0$, a contradiction. The same obstruction makes $\exp$ non-surjective on the real group $SL(2,\mathbb{R})$.

**Generation versus surjectivity.** Failure of surjectivity does not mean the exponentials fail to generate: since $\mathbb{B}^\times_1$ is connected and $\exp$ is a local diffeomorphism at $0$, the image $\exp(\mathrm{B}_0)$ contains a neighbourhood of the identity and generates the group, while remaining a proper subset. Nor does simple connectivity force surjectivity: $\mathbb{B}^\times_1$ is simply connected, yet $\exp$ is not onto. The classical criteria (connected compact, connected nilpotent, or $GL(n,\mathbb{C})$) are sufficient, not necessary.

---

The group of units is an open subset of $\mathbb{B}$, hence a smooth real manifold of dimension $8$, but its topology is far from that of a general open set in $\mathbb{R}^8$: it has the homotopy type of a compact group. The polar decomposition exhibits the maximal compact subgroup as a strong deformation retract, and with it determines the homotopy groups and the universal cover. Everything in this part is a statement about $\mathbb{B}^\times$ as a topological group; the topology of the ambient space is in *Topology in the Space of Biquaternions* and that of the null cone in *The Topology of the Zero-Divisor Cone*.

## The Correspondence with the Lie Algebra

The exponential is the correspondence between the group and the algebra. Its differential at the identity is the identity, so it is a local diffeomorphism onto a neighbourhood of $e_0$, and the inverse function theorem makes it a chart of $\mathbb{B}^\times$ near the identity; the tangent space at the identity is the whole algebra, since $\mathbb{B}^\times$ is open, with the commutator as bracket (*The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The Baker–Campbell–Hausdorff series of the algebra converges near the origin and reproduces the group law there, and the group law $\exp(\tilde A)\exp(\tilde C)$ against $\exp(\tilde A+\tilde C)$ of *Biquaternion Elementary Functions* is its first two terms. The subgroups correspond to the subalgebras: the compact subalgebra $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ to $S^3$, the trace-free part $\mathrm{B}_0$ to the norm-one group $\mathbb{B}^\times_1$, and the centre $\mathbb{C}e_0$ to $\mathbb{C}^\times e_0$.

## Summary

The group of units $\mathbb{B}^\times$ is a real Lie group of real dimension $8$, and the exponential map is its link with the Lie algebra: it is a local diffeomorphism at the identity, but it is not surjective onto the group. The unit quaternions $S^3=\{\tilde q\in\mathbb{H}_{\mathbb{B}}:N(\tilde q)=1\}$ form a compact connected simply connected subgroup of real dimension $3$, whose complexification is the norm-one group $\mathbb{B}^\times_1$ of real dimension $6$ and centre $\{\pm e_0\}$.

The subgroups are $\mathbb{B}^\times$, $\mathbb{B}^\times_1$, the unit quaternions $S^3$ and the centre $\mathbb{C}^\times e_0$; the maximal compact subgroup of $\mathbb{B}^\times_1$ is $S^3$, and the quotient by the centre $\mathbb{B}^\times_1/\{\pm e_0\}$ is a Lie group of real dimension $6$. Over the reals these are the real forms of the group, and the correspondence with the Lie algebra attaches each subgroup to its subalgebra: $S^3$ to $\mathrm{K}$, $\mathbb{B}^\times_1$ to $\mathrm{B}_0$, and $\mathbb{C}^\times e_0$ to the centre.

Surjectivity is not uniform. The exponential is surjective onto $S^3$, a connected compact group, and not surjective onto $\mathbb{B}^\times_1$: the norm-one group is not exponential, the obstruction a non-semi-simple element with the repeated eigenvalue $-1$, and the same obstruction occurs in $SL(2,\mathbb{R})$. The image still contains a neighbourhood of the identity and generates the connected group, so failure of surjectivity is not failure of generation.

The larger unitary groups are reached by enlarging the carrier and not the algebra. The matrices over the algebra satisfy $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$, so $M_3(\mathbb{B})\cong M_6(\mathbb{C})$ contains $\mathfrak{su}(3)$ with its eight generators, and the closed forms for $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ — a Lie-type form and Euler-angles forms, built from the antisymmetric, diagonal and diagonal-less symmetric linear functions of the enveloping-algebra article — are the explicit elements of those groups written with $3\times3$ matrices of biquaternions. They do not put an octet inside $\mathbb{B}$: each element fixes $e_0$ and acts on the vector part, so the matrix is $\operatorname{diag}(U_3,1)$ and the group is an $\mathrm{SU}(3)$ block on a three-dimensional complex space, while the algebra's own action on $\mathbb{B}$ is four-dimensional over $\mathbb{C}$ with the scalar direction inert. The ceiling is thus untouched and the price of the embedding is the factor $2$ in each matrix direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times$ | Group of units; real Lie group of real dimension $8$ |
| $\exp$ | Exponential map; closed form in *Biquaternion Elementary Functions* |
| $S^3=\{\tilde q\in\mathbb{H}_{\mathbb{B}}:N(\tilde q)=1\}$ | Unit quaternions; compact subgroup of real dimension $3$ |
| $\mathbb{B}^\times_1=\{N=1\}$ | Norm-one group; complexification of $S^3$; real dimension $6$ |
| $\{\pm e_0\}$ | Centre of $\mathbb{B}^\times_1$; the quotient is a Lie group of real dimension $6$ |
| $\mathrm{B}_0$ | Lie algebra of $\mathbb{B}^\times_1$; trace-free part |
| $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Lie algebra of $S^3$; compact subalgebra |
| $\mathbb{C}^\times e_0$ | Centre of $\mathbb{B}^\times$; Lie algebra $\mathbb{C}e_0$ |
| $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$ | Matrices over the algebra; the enlarged carrier |
| $a[\,]b$, $\odot$, $D\{\delta\}$ | Conway operator $\tilde{Q}\mapsto a\tilde{Q}b$, its composition, and the diagonal function |
| $G^{-1}=G^{+\approx}=G^{\dagger}$ | The inverse of a group element; association with conjugation |

## Further Reading

- A. Gsponer, "Explicit closed-form parametrization of SU(3) and SU(4) in terms of complex quaternions and elementary functions," arXiv:math-ph/0211056v2, 2002, for the closed forms of *The Enlarged Carrier*, the non-canonical SU(3) representation (25) with its inverse (27)–(28), the three elementary exponentials (18), (19) and (21) that make its factorisation work, the Euler-angles forms (31)–(33), and the parametrisations (34)–(38) in the Gell-Mann-type basis; the paper's Table 1, which offers a dictionary between its functions and the Gell-Mann parameters, is inconsistent as printed and is not transcribed here or in the companion $\mathrm{SU}(3)$ article.
- A. W. Conway, "Quaternions and matrices," *Proceedings of the Royal Irish Academy* **A 50** (1945) 98–130, and J. L. Synge, "Quaternions, Lorentz transformations, and the Conway–Dirac–Eddington matrices," *Communications of the Dublin Institute for Advanced Studies* **A 21** (1972), for the Conway operator calculus used by the closed forms.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- Companion articles: *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure* (the Conway operator basis) and *Association and the Transpose on the Biquaternion Algebra* (function association); *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* (the ceiling the enlarged carrier answers); *The Gluon: An Octet Outside the Biquaternion Algebra*.
