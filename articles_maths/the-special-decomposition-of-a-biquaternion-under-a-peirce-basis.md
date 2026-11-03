# __The Special Decomposition of a Biquaternion under a Peirce Basis__

## Introduction

Every biquaternion is the product of two unitaries around a real linear combination of $e_t$ and a pure Hermitian root of $e_t$. For a chosen root $\vec\Xi$, the statement is

$$
\tilde Q=\tilde U\,(r e_t+s\vec\Xi)\,\tilde V^{*},\qquad r\ge s\ge0,
$$

and the middle factor is diagonal in the Peirce basis of $\vec\Xi$, with Peirce coefficients $r+s$ and $r-s$. This is the **special decomposition under a Peirce basis** of the title. It is special in a precise sense: it selects the diagonal Peirce component of one root, and the two coefficients in that component are invariants of the element, not of the root.

The article answers four questions, in this order. What is a root of the algebra, and what Peirce data does it produce? What factorization does every element admit relative to those data? What is determined by the element, and what is a choice of presentation? What is the relation to the eigenbasis of a spectrally regular element?

The theorem is stated for an arbitrary root and proved by transporting a base case from the root that the element itself carries. The Peirce language is used throughout; no matrix representation appears before §*The Matrix Model as a Check*, where it serves as a verification and not as a definition. The article assumes *Algebra and Element Conventions* for the algebra and the conjugations, *Special Element and Peirce Conventions* for the glyphs of the root, the idempotent and the Peirce units, *Peirce Decompositions of the Biquaternion Algebra* and *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra* for the four corners and the basis, and *The Polar Decomposition of a Biquaternion* for the polar form. The eigenbasis is a different construction and is compared, not merged, in §*Relation to the Eigenbasis*.

## Notation

**The algebra.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the complex algebra with unit $e_t$ and three further units $\vec e_x,\vec e_y,\vec e_z$ subject to

$$
\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\quad \vec e_y\vec e_z=\vec e_x,\quad \vec e_z\vec e_x=\vec e_y,
$$

the reversed products being the negatives. The central imaginary is $i$, with $i^{2}=-1$ and $i$ commuting with every unit. An element and its vector part are

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z=Q_te_t+\vec Q,\qquad Q_\mu\in\mathbb{C},
$$

and the product is the associative product of $\mathbb{B}$.

**The involution.** The Hermitian conjugation is

$$
\tilde Q^{*}=\overline{Q_t}e_t-\overline{Q_x}\vec e_x-\overline{Q_y}\vec e_y-\overline{Q_z}\vec e_z.
$$

It is conjugate-linear and involutive, $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}$. The elements fixed by the star are **Hermitian**, those anti-fixed are **anti-Hermitian**. The **unitary group** is

$$
\mathrm{U}(\mathbb{B})=\{\tilde U\in\mathbb{B}:\tilde U^{*}\tilde U=e_t\};
$$

it is compact and isomorphic to $\mathrm{U}(2)$ (*The Unitary Group of the Biquaternion Algebra*).

**Pure elements.** An element is **pure** when its scalar part vanishes. A pure element is written with the arrow, $\vec X$, the arrow replacing the tilde.

**The Hermitian root.** A **Hermitian root of $e_t$** is a pure Hermitian element $\vec\Xi$ with

$$
\vec\Xi^{2}=e_t.
$$

In this article the word **root** is shorthand for a Hermitian root of $e_t$. The general root of *Special Element and Peirce Conventions* is any element with square $e_t$; it need be neither pure nor Hermitian, and it includes the central elements $\pm e_t$. The two extra conditions select the roots that produce a non-trivial Hermitian pair and a non-degenerate Peirce basis. A root is an element of the algebra, not a square root of a number, and the word is reserved for this object throughout.

**Proposition (the Hermitian roots are the imaginary unit vectors).** A pure element $\vec\Xi=\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z$ is a Hermitian root of $e_t$ exactly when $\Xi_k=i n_k$ with $n_k\in\mathbb{R}$ and $n_x^{2}+n_y^{2}+n_z^{2}=1$. The Hermitian roots are therefore exactly the elements $i\vec n$ with $\vec n$ a real unit vector, and they form a two-sphere.

*Proof.* A pure element is Hermitian exactly when each coefficient is fixed by $z\mapsto-\bar z$, that is when $\Xi_k=in_k$ with $n_k$ real. For such an element, $\vec\Xi^{2}=-(\Xi_x^{2}+\Xi_y^{2}+\Xi_z^{2})e_t=(n_x^{2}+n_y^{2}+n_z^{2})e_t$, which equals $e_t$ exactly when $\lvert\vec n\rvert=1$.

**Remark (Hermiticity and purity are restrictions, not consequences).** A pure element with $\vec\Xi^{2}=e_t$ need not be Hermitian: the element $i\sqrt2\,\vec e_x+\vec e_y$ is pure and its square is $e_t$, but its star is $i\sqrt2\,\vec e_x-\vec e_y$, which differs from it. A Hermitian element with $\vec\Xi^{2}=e_t$ need not be pure: the central elements $\pm e_t$ are Hermitian and square to $e_t$, but they give the trivial pair $e_t,0$. The roots used in this article are both pure and Hermitian. Purity excludes the two central elements; Hermiticity is exactly the condition for $\mathbb{C}[\vec\Xi]$ to be a $*$-plane and for $r e_t+s\vec\Xi$ to be Hermitian with spectral values $r\pm s$. The other solutions of $\vec\Xi^{2}=e_t$ do not carry the positive semidefinite middle factor of the theorem.

**The singular values.** The element $\tilde Q^{*}\tilde Q$ is Hermitian positive semidefinite, and its two spectral values are $\sigma_1^{2}$ and $\sigma_2^{2}$ with $\sigma_1\ge\sigma_2\ge0$. The numbers $\sigma_1,\sigma_2$ are the **singular values** of $\tilde Q$; equivalently, they are the spectral values of the Hermitian positive semidefinite element $(\tilde Q^{*}\tilde Q)^{1/2}$ (*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*).

## The Peirce Data of a Root

**The idempotents.** Fix a root $\vec\Xi$ and put

$$
\tilde\Pi_+=\frac{e_t+\vec\Xi}{2},\qquad
\tilde\Pi_-=\frac{e_t-\vec\Xi}{2}.
$$

**Lemma (the two idempotents).** The elements $\tilde\Pi_\pm$ satisfy

$$
\tilde\Pi_\pm^{2}=\tilde\Pi_\pm,\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
$$

and they are Hermitian, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$.

*Proof.* The idempotence is $\tilde\Pi_\pm^{2}=(e_t\pm2\vec\Xi+\vec\Xi^{2})/4=(e_t\pm\vec\Xi)/2$, using $\vec\Xi^{2}=e_t$; the orthogonality is $\tilde\Pi_+\tilde\Pi_-=(e_t-\vec\Xi^{2})/4=0$; the sum and the Hermiticity are immediate from the definitions.

**The Peirce decomposition.** The corners of the pair are

$$
\mathbb{B}_{++}=\tilde\Pi_+\mathbb{B}\tilde\Pi_+,\quad
\mathbb{B}_{+-}=\tilde\Pi_+\mathbb{B}\tilde\Pi_-,\quad
\mathbb{B}_{-+}=\tilde\Pi_-\mathbb{B}\tilde\Pi_+,\quad
\mathbb{B}_{--}=\tilde\Pi_-\mathbb{B}\tilde\Pi_-,
$$

each is a complex line, and

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}
$$

(*Peirce Decompositions of the Biquaternion Algebra*). The multiplication follows the corner rule $\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}$, with $s,t,u,v\in\{+,-\}$.

**Lemma (the diagonal part is the plane of the root).** The two diagonal corners span the plane of the idempotents and of the root,

$$
\mathbb{B}_{++}\oplus\mathbb{B}_{--}
=\mathbb{C}[\vec\Xi]
=\operatorname{span}_{\mathbb{C}}\{e_t,\vec\Xi\}
=\operatorname{span}_{\mathbb{C}}\{\tilde\Pi_+,\tilde\Pi_-\}.
$$

*Proof.* The diagonal corners are $\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_+$ and $\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_-$, so their sum is $\operatorname{span}_{\mathbb{C}}\{\tilde\Pi_+,\tilde\Pi_-\}$. The two idempotents are the invertible linear combinations $e_t\pm\vec\Xi$ divided by two, hence they span the same plane as $e_t$ and $\vec\Xi$.

Within the Peirce data, this is the only place where the root enters as an element of the algebra rather than as the label of a pair of corners.

**Lemma A (transport of roots).** For any two Hermitian roots $\vec\Xi,\vec\Xi'$ there is $\tilde W\in\mathrm{U}(\mathbb{B})$ with

$$
\tilde W\vec\Xi\tilde W^{*}=\vec\Xi',
$$

and consequently $\tilde W\tilde\Pi_\pm\tilde W^{*}=\tilde\Pi'_\pm$ and $\tilde W\mathbb{C}[\vec\Xi]\tilde W^{*}=\mathbb{C}[\vec\Xi']$.

*Proof.* Write $\vec\Xi=i\vec n$ and $\vec\Xi'=i\vec n'$ with $\vec n,\vec n'$ real unit vectors. A rotation of $\mathbb{R}^{3}$ carries $\vec n$ to $\vec n'$; every rotation of the vector part is the conjugation $\vec v\mapsto\tilde w\vec v\tilde w^{*}$ by a unit quaternion $\tilde w\in S^{3}\subset\mathrm{U}(\mathbb{B})$ (*Biquaternion Rotations and Lorentz Transformations*). Taking $\tilde W=\tilde w$ gives the first identity. The two consequences follow by conjugating $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$ and by conjugating the plane spanned by $e_t$ and $\vec\Xi$.

**The Peirce basis.** A **Peirce basis** of the pair is a quadruple

$$
\mathcal{B}(\vec\Xi)=(\tilde\Pi_+,\ \vec\Upsilon_{+-},\ \vec\Upsilon_{-+},\ \tilde\Pi_-),
\qquad
\vec\Upsilon_{+-}\in\mathbb{B}_{+-},\quad \vec\Upsilon_{-+}\in\mathbb{B}_{-+},
$$

with

$$
\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+,\qquad
\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_-.
$$

**Lemma (existence and uniqueness of the partner).** For every nonzero $\vec\Upsilon_{+-}\in\mathbb{B}_{+-}$ there is a unique $\vec\Upsilon_{-+}\in\mathbb{B}_{-+}$ with $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+$, and for it $\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_-$. Consequently every choice of one nonzero mixed element determines a Peirce basis, and the two mixed elements are nilpotents.

*Proof.* Left multiplication by $\vec\Upsilon_{+-}$ is a nonzero linear map from the line $\mathbb{B}_{-+}$ to the line $\mathbb{B}_{++}$; it is nonzero because the product of the two mixed lines is nonzero, and it is therefore an isomorphism of complex lines. Hence there is a unique $\vec\Upsilon_{-+}$ with $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+$. The product $\vec\Upsilon_{-+}\vec\Upsilon_{+-}$ lies in $\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_-$; writing it $\lambda\tilde\Pi_-$ and multiplying the first identity by $\vec\Upsilon_{+-}$ on the right gives $\vec\Upsilon_{+-}=\lambda\vec\Upsilon_{+-}$, so $\lambda=1$. The nilpotence is $\vec\Upsilon_{+-}^{2}\in\mathbb{B}_{++}\mathbb{B}_{+-}=0$, and likewise for the other.

**The gauge.** If $\vec\Upsilon_{+-}$ is replaced by $\mu\vec\Upsilon_{+-}$ with $\mu\in\mathbb{C}^{\times}$, the partner is replaced by $\mu^{-1}\vec\Upsilon_{-+}$, and the products are unchanged. This is the **gauge** of the basis,

$$
\vec\Upsilon_{+-}\longmapsto\mu\,\vec\Upsilon_{+-},\qquad
\vec\Upsilon_{-+}\longmapsto\mu^{-1}\vec\Upsilon_{-+},\qquad \mu\in\mathbb{C}^{\times},
$$

and every two bases of the same pair differ by exactly one gauge transformation. The basis $\mathcal{B}(\vec\Xi)$ is therefore unique up to the gauge, and the diagonal elements are the idempotents themselves and are not a choice. The companion article writes the same gauge with the parameter $t=\mu^{-1}$.

**Peirce coordinates.** Every element has a unique expansion

$$
\tilde Q=Q_{++}\tilde\Pi_++Q_{+-}\vec\Upsilon_{+-}+Q_{-+}\vec\Upsilon_{-+}+Q_{--}\tilde\Pi_-,
\qquad Q_{st}\in\mathbb{C}.
$$

Under the gauge the off-diagonal coordinates transform reciprocally, $Q_{+-}\mapsto\mu^{-1}Q_{+-}$ and $Q_{-+}\mapsto\mu Q_{-+}$, while $Q_{++}$ and $Q_{--}$ are unchanged.

## The Theorem

**Theorem (factorization relative to a root).** Let $\vec\Xi$ be a Hermitian root of $e_t$. For every $\tilde Q\in\mathbb{B}$ there exist $\tilde U,\tilde V\in\mathrm{U}(\mathbb{B})$ and real numbers $r\ge s\ge0$ with

$$
\tilde Q=\tilde U\,(r e_t+s\vec\Xi)\,\tilde V^{*}.
$$

The middle factor lies in $\mathbb{C}[\vec\Xi]$, and its Peirce coordinates in $\mathcal{B}(\vec\Xi)$ are $(r+s,0,0,r-s)$.

**Reading of the statement.** Three points are part of the statement and not consequences of the proof.

- The middle factor is diagonal in the Peirce basis, $r e_t+s\vec\Xi=(r+s)\tilde\Pi_++(r-s)\tilde\Pi_-$, and its two Peirce coefficients are non-negative real numbers.
- The pair $(r,s)$ is determined by $\tilde Q$ alone. The singular values of $\tilde Q$ are $\sigma_1=r+s$ and $\sigma_2=r-s$, so $r=(\sigma_1+\sigma_2)/2$ and $s=(\sigma_1-\sigma_2)/2$. The root changes only the presentation of the middle factor.
- The factorization is not a claim about a preferred root. It holds for every root, and the two numbers $r+s$ and $r-s$ are the same for all roots.

## The Proof

The proof has three steps: a transport of roots, a base case, and a transport of the factorization. The base case is not attached to a fixed root; it is attached to the root that the element itself carries. That is the choice of base case that makes the proof shortest, and it is internal to the proof.

**Lemma A (transport of roots)** is the transitivity lemma of §*The Peirce Data of a Root*: for any two roots $\vec\Xi,\vec\Xi'$ there is $\tilde W\in\mathrm{U}(\mathbb{B})$ with $\tilde W\vec\Xi\tilde W^{*}=\vec\Xi'$, and it carries the idempotents and the plane of one root to those of the other. It is the first step.

**Lemma (extension of a partial isometry).** Let $\tilde Q_0$ be a partial isometry, with initial projection $\tilde\Pi_{\mathrm i}=\tilde Q_0^{*}\tilde Q_0$ and final projection $\tilde\Pi_{\mathrm f}=\tilde Q_0\tilde Q_0^{*}$. Then there is $\tilde U\in\mathrm{U}(\mathbb{B})$ with $\tilde U\tilde\Pi_{\mathrm i}=\tilde Q_0$.

*Proof.* If $\tilde\Pi_{\mathrm i}=0$ then $\tilde Q_0=0$ and any unitary works; if $\tilde\Pi_{\mathrm i}=e_t$ then $\tilde Q_0$ is unitary. Otherwise $\tilde\Pi_{\mathrm i}$ and $\tilde\Pi_{\mathrm f}$ are Hermitian idempotents that are neither $0$ nor $e_t$, so each is the idempotent of a root. For the initial one, put $\vec\Xi=2\tilde\Pi_{\mathrm i}-e_t$: the element $\vec\Xi$ is Hermitian, and it is pure because the vector part of $\tilde\Pi_{\mathrm i}$ does not vanish, which forces the scalar part of $\tilde\Pi_{\mathrm i}$ to be $1/2$ by $\tilde\Pi_{\mathrm i}^{2}=\tilde\Pi_{\mathrm i}$; then $\vec\Xi^{2}=4\tilde\Pi_{\mathrm i}-4\tilde\Pi_{\mathrm i}+e_t=e_t$. So $\tilde\Pi_{\mathrm i}=(e_t+\vec\Xi)/2$, and likewise $\tilde\Pi_{\mathrm f}=(e_t+\vec\Xi')/2$. By Lemma A there is $\tilde W\in\mathrm{U}(\mathbb{B})$ with $\tilde W\tilde\Pi_{\mathrm i}\tilde W^{*}=\tilde\Pi_{\mathrm f}$. Put

$$
\tilde U=\tilde Q_0+\tilde W(e_t-\tilde\Pi_{\mathrm i}).
$$

The cross terms in $\tilde U^{*}\tilde U$ vanish because $\tilde Q_0=\tilde Q_0\tilde\Pi_{\mathrm i}=\tilde\Pi_{\mathrm f}\tilde Q_0$ and $\tilde W\tilde\Pi_{\mathrm i}=\tilde\Pi_{\mathrm f}\tilde W$, and the two remaining terms are $\tilde\Pi_{\mathrm i}+(e_t-\tilde\Pi_{\mathrm i})=e_t$; hence $\tilde U$ is unitary, and $\tilde U\tilde\Pi_{\mathrm i}=\tilde Q_0$.

**Lemma B (the root carried by the element).** For every $\tilde Q\in\mathbb{B}$ there exist a Hermitian root $\vec\Xi$, a unitary $\tilde U\in\mathrm{U}(\mathbb{B})$ and real numbers $r\ge s\ge0$ with

$$
\tilde Q=\tilde U\,(r e_t+s\vec\Xi).
$$

*Proof.* By the polar form with the Hermitian factor on the right, $\tilde Q=\tilde Q_0\tilde H$ with $\tilde H=(\tilde Q^{*}\tilde Q)^{1/2}$ Hermitian positive semidefinite and $\tilde Q_0=\tilde Q\tilde H^{+}$ a partial isometry. This is the companion's polar form read on the other side: applied to $\tilde Q^{*}$ it gives $\tilde Q^{*}=\tilde H\tilde Q_0^{*}$ with the same $\tilde H$, and transposing back gives the displayed identity (*The Polar Decomposition of a Biquaternion*, §*The Isometry Factor*); the inverse $\tilde H^{+}$ is that of §*The Moore–Penrose Inverse of the Hermitian Factor*, and $\tilde Q_0^{*}\tilde Q_0=\tilde H^{+}\tilde H$ is the projection onto the image of $\tilde H$. Write the Hermitian factor in coordinates,

$$
\tilde H=h_0e_t+i\bigl(h_x\vec e_x+h_y\vec e_y+h_z\vec e_z\bigr)=h_0e_t+i\vec h,
\qquad h_0,h_x,h_y,h_z\in\mathbb{R}.
$$

Positive semidefiniteness is $h_0\ge\lvert\vec h\rvert$ (*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*), and the spectral values of $\tilde H$ are $h_0\pm\lvert\vec h\rvert$. Put $r=h_0$ and $s=\lvert\vec h\rvert$. If $s>0$, put $\vec\Xi=i\vec h/s$; if $s=0$, put $\vec\Xi=i\vec e_z$. In both cases $\vec\Xi$ is a root and $\tilde H=r e_t+s\vec\Xi$, with $r\ge s\ge0$.

It remains to replace the partial isometry $\tilde Q_0$ by a unitary without changing the product. Let $\tilde\Pi_{\mathrm i}=\tilde Q_0^{*}\tilde Q_0$, which is the projection onto the image of $\tilde H$. By the extension lemma there are $\tilde U\in\mathrm{U}(\mathbb{B})$ and $\tilde W\in\mathrm{U}(\mathbb{B})$ with $\tilde U=\tilde Q_0+\tilde W(e_t-\tilde\Pi_{\mathrm i})$ and $\tilde U\tilde\Pi_{\mathrm i}=\tilde Q_0$. Since $(e_t-\tilde\Pi_{\mathrm i})\tilde H=0$, one has

$$
\tilde U\tilde H=\tilde Q_0\tilde H+\tilde W(e_t-\tilde\Pi_{\mathrm i})\tilde H=\tilde Q_0\tilde H=\tilde Q.
$$

Hence $\tilde Q=\tilde U(r e_t+s\vec\Xi)$.

**Lemma C (transport of the factorization).** If the theorem holds for a Hermitian root $\vec\Xi$, then it holds for every Hermitian root $\vec\Xi'$.

*Proof.* Let $\tilde W\in\mathrm{U}(\mathbb{B})$ satisfy $\tilde W\vec\Xi\tilde W^{*}=\vec\Xi'$, by Lemma A, and let $\tilde Q=\tilde U(r e_t+s\vec\Xi)\tilde V^{*}$ be a factorization for $\vec\Xi$. Then

$$
\tilde Q=\tilde U\tilde W^{*}\,\bigl(r e_t+s\vec\Xi'\bigr)\,\bigl(\tilde V\tilde W^{*}\bigr)^{*},
$$

and $\tilde U\tilde W^{*}$ and $\tilde V\tilde W^{*}$ are unitary.

**Conclusion.** Let $\vec\Xi$ be the root fixed in the statement. Lemma B gives the factorization of $\tilde Q$ for the root that $\tilde Q$ carries; Lemma A supplies the unitary $\tilde W$ carrying that root to $\vec\Xi$; Lemma C transports the factorization to $\vec\Xi$. Hence the theorem holds for every root.

**What the proof uses, and what it does not use.** It uses the transitivity of $\mathrm{U}(\mathbb{B})$ on the roots, the polar form and the positivity of $\tilde Q^{*}\tilde Q$ for the base case, and the extension of a partial isometry to a unitary. It does not use a preferred root in the statement, and it does not use a matrix representation at any point.

## Uniqueness

**Theorem (uniqueness).** Let $\tilde Q=\tilde U(r e_t+s\vec\Xi)\tilde V^{*}$ with $r\ge s\ge0$, and let $\tilde Q=\tilde U'(r e_t+s\vec\Xi)\tilde V'^{*}$ be another factorization with the same root and the same pair. Put $\tilde A=\tilde U^{*}\tilde U'$ and $\tilde B=\tilde V^{*}\tilde V'$, so that $\tilde A(r e_t+s\vec\Xi)=(r e_t+s\vec\Xi)\tilde B$. Then:

- if $r>s>0$, there are real $\theta_+,\theta_-$ with $\tilde A=\tilde B=e^{i\theta_+}\tilde\Pi_++e^{i\theta_-}\tilde\Pi_-$; the two unitaries are unique up to the simultaneous right multiplication by a unitary commuting with the middle factor;
- if $r=s>0$, there are real $\theta,\varphi,\psi$ with
$$
\tilde A=e^{i\theta}\tilde\Pi_++e^{i\varphi}\tilde\Pi_-,\qquad
\tilde B=e^{i\theta}\tilde\Pi_++e^{i\psi}\tilde\Pi_-;
$$
the phase of the image line is common and the phase of the kernel line is free on each side;
- if $s=0$ and $r>0$, the middle factor is the scalar $r e_t$ and $\tilde A=\tilde B$ is an arbitrary unitary; if $\tilde Q=0$ the middle factor vanishes and $\tilde A$ and $\tilde B$ are independent arbitrary unitaries.

*Proof.* Write the middle factor in the Peirce basis, $M=r e_t+s\vec\Xi=r_+\tilde\Pi_++r_-\tilde\Pi_-$ with $r_\pm=r\pm s$, and write $\tilde A$ and $\tilde B$ in the same basis, with Peirce coordinates $A_{st}$ and $B_{st}$. The identity $\tilde A M=M\tilde B$ reads, on the four Peirce components,

$$
A_{st}\,r_t=r_s\,B_{st},\qquad s,t\in\{+,-\}.
$$

If $s=0$ and $r>0$, then $r_+=r_-=r$ and the identity is $\tilde A=\tilde B$, with no further condition beyond unitarity; if $r=0$ the identity is void, and $\tilde A$ and $\tilde B$ are free.

If $r>s>0$, then $M$ is invertible and the identity gives $\tilde A=M\tilde B M^{-1}$. Unitarity of $\tilde A$ and $\tilde B$ gives $\tilde B^{*}M^{2}\tilde B=M^{2}$, that is $\tilde B M^{2}=M^{2}\tilde B$. The Hermitian element $M^{2}$ has the two distinct spectral values $r_+^{2}$ and $r_-^{2}$, so the unitary $\tilde B$ commutes with its two spectral projections and is therefore diagonal in the Peirce basis; then the diagonal equations give $\tilde A=\tilde B$. A diagonal element $a\tilde\Pi_++b\tilde\Pi_-$ is unitary exactly when $\lvert a\rvert=\lvert b\rvert=1$, because $\tilde\Pi_\pm$ are Hermitian orthogonal idempotents.

If $r=s>0$, then $r_+=2r$ and $r_-=0$. The equations with $(s,t)=(+,-)$ and $(-,+)$ give $B_{+-}=0$ and $A_{-+}=0$, so both elements have at most three Peirce components. A unitary with $A_{-+}=0$ is diagonal: writing $A=a\tilde\Pi_++b\tilde\Pi_-+c\vec\Upsilon_{+-}$, the product $\tilde A\tilde A^{*}$ carries the mixed terms $a\bar c\,\vec\Upsilon_{-+}$ and $c\bar b\,\vec\Upsilon_{+-}$, which must vanish, so $c=0$ because $\lvert a\rvert=\lvert b\rvert=1$; and likewise for $\tilde B$. Hence $\tilde A=\operatorname{diag}(A_{++},A_{--})$ and $\tilde B=\operatorname{diag}(B_{++},B_{--})$, the equation $(+,+)$ gives $A_{++}=B_{++}$, and unitarity gives $\lvert A_{++}\rvert=\lvert A_{--}\rvert=\lvert B_{--}\rvert=1$.

**Corollary (the residual freedom preserves the middle factor).** In each case of the theorem, $\tilde A M\tilde B^{*}=M$. Hence $\tilde U'(r e_t+s\vec\Xi)\tilde V'^{*}=\tilde U(r e_t+s\vec\Xi)\tilde V^{*}$ with the middle factor unchanged, and the residual freedom is a subgroup of $\mathrm{U}(\mathbb{B})\times\mathrm{U}(\mathbb{B})$ acting on the right of the pair: simultaneously in the generic case, and with the two kernel phases independent in the rank-one case. It is not the gauge of the Peirce basis: the gauge rescales the mixed elements of $\mathcal{B}(\vec\Xi)$ and leaves the unitaries alone, while the residual freedom acts on the unitaries and leaves the basis alone.

## The Peirce-Diagonal Reading

**Proposition (the element becomes Peirce-diagonal).** Let $\tilde Q=\tilde U(r e_t+s\vec\Xi)\tilde V^{*}$ and put

$$
\tilde\Pi_i^{\tilde U}=\tilde U\tilde\Pi_i\tilde U^{*},\qquad
\tilde\Pi_j^{\tilde V}=\tilde V\tilde\Pi_j\tilde V^{*},\qquad i,j\in\{+,-\}.
$$

Then

$$
\tilde\Pi_i^{\tilde U}\,\tilde Q\,\tilde\Pi_j^{\tilde V}
=\delta_{ij}\,r_i\,\tilde U\tilde\Pi_i\tilde V^{*},
\qquad r_+=r+s,\quad r_-=r-s.
$$

*Proof.* By the corner rule, $\tilde\Pi_i^{\tilde U}\tilde Q\tilde\Pi_j^{\tilde V}=\tilde U\tilde\Pi_i(r e_t+s\vec\Xi)\tilde\Pi_j\tilde V^{*}$. The middle factor acts on the idempotents by $\tilde\Pi_i(r e_t+s\vec\Xi)=r_i\tilde\Pi_i$, and $\tilde\Pi_i\tilde\Pi_j=\delta_{ij}\tilde\Pi_i$; the display follows.

**Remark.** The two rotated systems depend on the element, through $\tilde U$ and $\tilde V$, and on the chosen root. The coefficients $r_+$ and $r_-$ do not depend on either. The proposition is the precise sense in which the element is Peirce-diagonal: diagonal relative to the pair of rotated systems, not relative to the pair $\tilde\Pi_\pm$ of the root itself.

## What Is Intrinsic and What Is a Choice

**Proposition (invariance of the coefficients).** Let $\vec\Xi$ and $\vec\Xi'$ be two Hermitian roots, and let $\tilde W\in\mathrm{U}(\mathbb{B})$ satisfy $\tilde W\vec\Xi\tilde W^{*}=\vec\Xi'$. If

$$
\tilde Q=\tilde U\,(r e_t+s\vec\Xi)\,\tilde V^{*},
$$

then

$$
\tilde Q=(\tilde U\tilde W^{*})\,(r e_t+s\vec\Xi')\,(\tilde V\tilde W^{*})^{*},
$$

with the same $r$ and $s$.

*Proof.* Since $r e_t+s\vec\Xi=\tilde W^{*}(r e_t+s\vec\Xi')\tilde W$, the identity is

$$
\tilde Q=\tilde U\tilde W^{*}(r e_t+s\vec\Xi')\tilde W\tilde V^{*},
$$

and $\tilde W\tilde V^{*}=(\tilde V\tilde W^{*})^{*}$.

**Corollary (the numbers are invariants of the element).** The numbers $r$, $s$, $r_+=r+s$ and $r_-=r-s$ are the same for every root. They are determined by $\tilde Q$ alone: $r_+$ and $r_-$ are its singular values, and $r=(r_++r_-)/2$, $s=(r_+-r_-)/2$. The unitary $\tilde W$ depends only on the two roots and not on the element, so the same $\tilde W$ serves every $\tilde Q$. The root, the Peirce basis, the gauge and the unitaries are a presentation; the coefficients are the invariant.

The two columns below separate the two kinds of data.

| Intrinsic to $\tilde Q$ | A choice of presentation |
|---|---|
| The numbers $r\ge s\ge0$ | The root $\vec\Xi$ |
| The Peirce coefficients $r_+=r+s$, $r_-=r-s$, that is the singular values $\sigma_1,\sigma_2$ | The Peirce basis $\mathcal{B}(\vec\Xi)$ |
| The image line and the kernel line of $\tilde Q$, when $r>s>0$ | The gauge $\mu$ of $\mathcal{B}(\vec\Xi)$ |
| | The unitaries $\tilde U,\tilde V$, and the residual freedom between them |
| | The matrix representation used as a check |

## Worked Example

### The Element and Its Singular Values

Take

$$
\tilde Q=\frac{1}{\sqrt2}(e_t+\vec e_x)\left(\frac32e_t+\frac12i\vec e_z\right)
=\frac{3\sqrt2}{4}e_t+\frac{3\sqrt2}{4}\vec e_x-\frac{\sqrt2}{4}i\vec e_y+\frac{\sqrt2}{4}i\vec e_z .
$$

The factor $(e_t+\vec e_x)/\sqrt2$ is a unit quaternion, hence unitary, so

$$
\tilde Q^{*}\tilde Q=\left(\frac32e_t+\frac12i\vec e_z\right)^{2}
=\frac52e_t+\frac32i\vec e_z .
$$

Its spectral values are $5/2\pm3/2$, that is $4$ and $1$. The singular values are therefore $2$ and $1$, and

$$
r=\frac{2+1}{2}=\frac32,\qquad s=\frac{2-1}{2}=\frac12,\qquad r_+=2,\quad r_-=1.
$$

### The Root $i\vec e_z$

Take $\vec\Xi_0=i\vec e_z$. The idempotents and the standard mixed units are

$$
\tilde\Pi_\pm=\frac{e_t\pm i\vec e_z}{2},\qquad
\vec\Upsilon_{+-}=\frac{i\vec e_x-\vec e_y}{2},\qquad
\vec\Upsilon_{-+}=\frac{i\vec e_x+\vec e_y}{2},
$$

with $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+$ and $\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_-$; this is the standard Peirce basis of the literature. The factorization is

$$
\tilde Q=\tilde U_0\left(\frac32e_t+\frac12i\vec e_z\right)\tilde V_0^{*},
\qquad
\tilde U_0=\frac{e_t+\vec e_x}{\sqrt2},\quad \tilde V_0=e_t,
$$

which is the definition of $\tilde Q$ above. The middle factor has Peirce coordinates $(2,0,0,1)$ in $\mathcal{B}(i\vec e_z)$.

### The Root $i\vec e_x$

Take $\vec\Xi_1=i\vec e_x$ and the unitary

$$
\tilde W=\frac{e_t+\vec e_y}{\sqrt2},
$$

so that $\tilde W\vec\Xi_0\tilde W^{*}=\vec\Xi_1$. The transported factorization is

$$
\tilde Q=\tilde U_1\left(\frac32e_t+\frac12i\vec e_x\right)\tilde V_1^{*},
\qquad
\tilde U_1=\tilde U_0\tilde W^{*}=\frac12\bigl(e_t+\vec e_x-\vec e_y-\vec e_z\bigr),
\quad
\tilde V_1=\tilde W^{*}=\frac{e_t-\vec e_y}{\sqrt2}.
$$

The Peirce data of $\vec\Xi_1$ are

$$
\tilde\Pi'_\pm=\frac{e_t\pm i\vec e_x}{2},\qquad
\vec\Upsilon'_{+-}=-\frac{\vec e_y+i\vec e_z}{2},\qquad
\vec\Upsilon'_{-+}=\frac{\vec e_y-i\vec e_z}{2},
$$

the mixed units being the $\tilde W$-conjugates of the standard ones. The middle factor has Peirce coordinates $(2,0,0,1)$ in $\mathcal{B}(i\vec e_x)$ as well, so the two roots give the same coefficients $r_+=2$ and $r_-=1$.

### The Two Presentations Agree

The two factorizations differ by $\tilde W$ exactly as the invariance proposition predicts: $\tilde U_1=\tilde U_0\tilde W^{*}$ and $\tilde V_1=\tilde V_0\tilde W^{*}$, and

$$
\tilde Q=\tilde U_1\left(\frac32e_t+\frac12i\vec e_x\right)\tilde V_1^{*}
=\tilde U_0\left(\frac32e_t+\frac12i\vec e_z\right)\tilde V_0^{*}.
$$

The rotated idempotents of the second presentation are

$$
\tilde\Pi_+^{\tilde U_1}=\tilde U_1\tilde\Pi'_+\tilde U_1^{*}=\frac{e_t-i\vec e_y}{2},
\qquad
\tilde\Pi_-^{\tilde U_1}=\frac{e_t+i\vec e_y}{2},
$$

$$
\tilde\Pi_+^{\tilde V_1}=\tilde V_1\tilde\Pi'_+\tilde V_1^{*}=\tilde\Pi_+,
\qquad
\tilde\Pi_-^{\tilde V_1}=\tilde\Pi_-.
$$

The Peirce-diagonal proposition then gives $\tilde\Pi_i^{\tilde U_1}\tilde Q\tilde\Pi_j^{\tilde V_1}=\delta_{ij}r_i\tilde U_1\tilde\Pi'_i\tilde V_1^{*}$, with $r_+=2$ and $r_-=1$. Relative to the unrotated pair $\tilde\Pi'_\pm$ the element is not diagonal; for instance

$$
\tilde\Pi'_+\tilde Q\tilde\Pi'_-=\frac{\sqrt2}{8}\bigl((1-i)\vec e_y+(1+i)\vec e_z\bigr)\ne0.
$$

This is the point of §*The Peirce-Diagonal Reading*: the idempotent systems must be rotated by the unitaries, and the coefficients are $2$ and $1$ in both presentations.

## The Boundary of the Construction

The Peirce decomposition and the factorization have different boundaries, and they must not be conflated.

**The Peirce side has no boundary.** A root always produces the idempotents $\tilde\Pi_\pm$, the four corners, the Peirce basis and the expansion of any element in it. The decomposition exists for every root and every element, and the basis is unique up to the gauge. Nothing degenerates.

**The factorization always exists and its uniqueness degenerates.** The scalars $r$ and $s$ are always defined, and the unitaries always exist, by the theorem. The ambiguity of the pair $(\tilde U,\tilde V)$ grows on two loci, and the two are different.

- **The scalar locus $s=0$, equivalently $r_+=r_-$.** The middle factor is $r e_t$ and any unitary commutes with it. The pair is unique only up to the diagonal right action of $\mathrm{U}(\mathbb{B})$, $(\tilde U,\tilde V)\mapsto(\tilde U\tilde R,\tilde V\tilde R)$ with arbitrary unitary $\tilde R$. This is the case of two equal singular values.
- **The rank-one locus $r=s>0$, equivalently $r_-=0$.** The middle factor is $2r\tilde\Pi_+$ and has one zero spectral value. The pair is unique only up to $\tilde U'=\tilde U(e^{i\theta}\tilde\Pi_++e^{i\varphi}\tilde\Pi_-)$ and $\tilde V'=\tilde V(e^{i\theta}\tilde\Pi_++e^{i\psi}\tilde\Pi_-)$ with independent real $\varphi$ and $\psi$: the phase of the image line is common, the phase of the kernel line is free on each side. This is the case of a vanishing second singular value.
- **The generic locus $r>s>0$.** The pair is unique up to the simultaneous right multiplication by $e^{i\theta_+}\tilde\Pi_++e^{i\theta_-}\tilde\Pi_-$, a two-torus.

At $\tilde Q=0$ one has $r=s=0$, the middle factor vanishes, and every pair of unitaries is allowed. The two loci are the boundary of the uniqueness of the factorization, not of the Peirce decomposition.

## Relation to the Eigenbasis

The eigenbasis of a spectrally regular biquaternion is a different construction, and it is compared here without being merged with the special decomposition.

The eigenbasis fixes the direction to the vector part of the element itself,

$$
\vec\Xi_{\mathrm{eig}}=-\frac{i\vec Q}{B},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

which is defined only on the spectral-regular locus $B^{2}\ne0$. The element is pure and satisfies $\vec\Xi_{\mathrm{eig}}^{2}=e_t$, but it need not be Hermitian; when it is not, it lies outside the class of roots fixed in this article. Its idempotents $\tilde\Pi_\pm=(e_t\pm\vec\Xi_{\mathrm{eig}})/2$ commute with $\tilde Q$, and the expansion

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,\qquad \lambda_\pm=Q_t\pm iB,
$$

is diagonal with complex coefficients, with no unitaries. The special decomposition fixes no relation between the root and the element, requires no spectral condition, uses Hermitian roots and produces a factorization with two unitaries and real non-negative coefficients.

| Aspect | Eigenbasis | Special decomposition |
|---|---|---|
| Direction | $\vec\Xi_{\mathrm{eig}}=-i\vec Q/B$, depends on $\tilde Q$ | Any Hermitian root, independent of $\tilde Q$ |
| Existence | $B^{2}\ne0$ | Always |
| Unitaries | $\tilde U=\tilde V=e_t$ | General $\tilde U,\tilde V$ |
| Middle factor | $\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ | $r e_t+s\vec\Xi$ |
| Coefficients | $\lambda_\pm=Q_t\pm iB\in\mathbb{C}$ | $r\ge s\ge0$ real |
| Peirce basis | $\mathcal{B}(\vec\Xi_{\mathrm{eig}})$ | $\mathcal{B}(\vec\Xi)$ with an arbitrary Hermitian root |

The two constructions meet on the Hermitian positive semidefinite elements with $B^{2}\ne0$. There the eigenbasis element $\vec\Xi_{\mathrm{eig}}$ is the negative of the root that the element carries, and its two idempotents are those of the special decomposition with the labels exchanged. With that root and with $\tilde U=\tilde V=e_t$ the two statements coincide, the coefficients being real and non-negative in both. Off that locus the eigenbasis keeps the complex eigenvalues and the special decomposition keeps the real singular values, and the two are not the same statement.

## The Matrix Model as a Check

The $2\times2$ Pauli representation is used once, here, as a verification and not as a definition (*$M_2(\mathbb{C})$ Pauli Representation*):

$$
e_t\longmapsto I_2,\qquad
\vec e_x\longmapsto-i\sigma_x,\qquad
\vec e_y\longmapsto-i\sigma_y,\qquad
\vec e_z\longmapsto-i\sigma_z,
$$

with the Pauli matrices $\sigma_x,\sigma_y,\sigma_z$. Under it the star becomes the conjugate transpose, so unitaries become unitary matrices and the theorem becomes a factorization $\mathsf M_2(\tilde Q)=U\,\mathsf M_2(r e_t+s\vec\Xi)\,V^{*}$ with $U,V\in\mathrm{U}(2)$.

For the standard root $\vec\Xi_0=i\vec e_z$ one has $\mathsf M_2(\vec\Xi_0)=\sigma_z$, hence

$$
\mathsf M_2(r e_t+s\vec\Xi_0)=rI_2+s\sigma_z=\begin{pmatrix}r+s&0\\0&r-s\end{pmatrix},
$$

which is diagonal: the reference root reproduces the diagonal middle factor of the ordinary singular value decomposition.

For the root $\vec\Xi_1=i\vec e_x$ one has $\mathsf M_2(\vec\Xi_1)=\sigma_x$, hence

$$
\mathsf M_2(r e_t+s\vec\Xi_1)=rI_2+s\sigma_x=\begin{pmatrix}r&s\\s&r\end{pmatrix},
$$

which is not diagonal in the Pauli frame. It is nonetheless Hermitian with spectral values $r+s$ and $r-s$: it is diagonal in the Peirce frame of $\vec\Xi_1$, not in the matrix frame of the representation. This is the warning of the article. The special decomposition is diagonal in the Peirce sense, not in the matrix sense; the matrix model confirms the coefficients and shows that only the reference root makes the middle factor matrix-diagonal.

## Summary

A root of $e_t$ is a pure Hermitian element $\vec\Xi$ with $\vec\Xi^{2}=e_t$; the roots are exactly $i\vec n$ with $\vec n$ a real unit vector. A root produces the idempotents $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$, the four Peirce lines, the Peirce basis $\mathcal{B}(\vec\Xi)$, unique up to the reciprocal gauge, and the plane $\mathbb{C}[\vec\Xi]=\mathbb{B}_{++}\oplus\mathbb{B}_{--}$.

For every element and every root there are unitaries $\tilde U,\tilde V$ and real $r\ge s\ge0$ with $\tilde Q=\tilde U(r e_t+s\vec\Xi)\tilde V^{*}$. The middle factor is Peirce-diagonal with coefficients $r_+=r+s$ and $r_-=r-s$, and the element is Peirce-diagonal relative to the rotated idempotent systems $\tilde U\tilde\Pi_i\tilde U^{*}$, $\tilde V\tilde\Pi_j\tilde V^{*}$. The proof transports the base case from the root carried by the element to the chosen root. The uniqueness of the pair $(\tilde U,\tilde V)$ degenerates at $s=0$ and at $r=s$, and at neither point does the Peirce decomposition degenerate.

The numbers $r_+$ and $r_-$ are the singular values of the element, and $r=(r_++r_-)/2$, $s=(r_+-r_-)/2$; all four are independent of the root. The root, the basis, the gauge and the unitaries are a choice of presentation. The decomposition is special because it selects the diagonal Peirce component of a chosen root, and the numbers in that component are invariants of the element, not of the root.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vec\Xi$ | A Hermitian root of $e_t$: pure, $\vec\Xi^{2}=e_t$ |
| $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$ | The two idempotents of the root |
| $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ | A Peirce corner, left index first |
| $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ | The mixed units of a Peirce basis |
| $\mathcal{B}(\vec\Xi)$ | The Peirce basis $(\tilde\Pi_+,\vec\Upsilon_{+-},\vec\Upsilon_{-+},\tilde\Pi_-)$ |
| $\mu$ | The gauge parameter, $\vec\Upsilon_{+-}\mapsto\mu\vec\Upsilon_{+-}$, $\vec\Upsilon_{-+}\mapsto\mu^{-1}\vec\Upsilon_{-+}$ |
| $Q_{st}$ | The Peirce coordinates of $\tilde Q$ |
| $r\ge s\ge0$ | The two real coefficients of the middle factor |
| $r_+=r+s$, $r_-=r-s$ | The two Peirce coefficients |
| $\sigma_1\ge\sigma_2$ | The singular values, $\sigma_1=r_+$, $\sigma_2=r_-$ |
| $\tilde U,\tilde V$ | The two unitaries of the factorization |
| $\tilde\Pi_i^{\tilde U},\tilde\Pi_j^{\tilde V}$ | The rotated idempotent systems |
| $\vec\Xi_{\mathrm{eig}}=-i\vec Q/B$ | The element of the eigenbasis, defined for $B^{2}\ne0$ |

## Further Reading

- [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the four corners, the corner rule and the diagonal lines.
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the existence of the mixed partner, the gauge and the torsor of bases.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the Hermitian factor and the partial isometry used in Lemma B.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for $\mathrm{U}(\mathbb{B})\cong\mathrm{U}(2)$ and its action.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the element-dependent root compared in §*Relation to the Eigenbasis*.
- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the matrix check of §*The Matrix Model as a Check*.
- [Idempotents](idempotents.html), for the classification of the idempotents and the halving map from the roots of $e_t$.
