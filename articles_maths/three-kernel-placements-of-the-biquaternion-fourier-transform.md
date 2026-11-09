# __The Three Kernel Placements of the Biquaternion Fourier Transform__

## Introduction

**This article proves that the three ways of placing the biquaternion Fourier kernel against a value give three different operators, and that the distance between them is measured by a commutator whose size is the distance of the value from a four-plane.** The three placements are the left, the right and the two-sided, and the last of them carries a second root and a choice of sign that no one-sided placement has.

**The setting.** Let $\tilde{Ζ}$ be the **Hermitian** root of $1$ of *Biquaternion Continuous Harmonic Analysis*, so that $\tilde{Ζ}^{2}=e_t$ and $\tilde{Ζ}^{*}=\tilde{Ζ}$, and let $R=i\tilde{Ζ}$. Then $R^{2}=-e_t$ and $R^{*}=-R$, so $\lVert R\rVert_E=1$; when the root is not central, $R$ is a real unit vector of the pure part. The kernel is

$$
W(t,\omega)=\exp(-2\pi i\tilde{Ζ}\omega t)=\exp(-2\pi R\omega t),
$$

a time $t$, a real frequency $\omega$. Let $\tilde{Ζ}'$ be a second Hermitian root of $1$, with $R'=i\tilde{Ζ}'$ and $W'(t,\omega)=\exp(2\pi R'\omega t)$, which is $W(t,\omega)^{-1}$ exactly when $R'=R$. The three transforms of an integrable $f:\mathbb{R}\to\mathbb{B}$ are

$$
\mathcal T_L[f](\omega)=\int W(t,\omega)f(t)\,dt,\qquad \mathcal T_R[f](\omega)=\int f(t)W(t,\omega)\,dt,
$$

and

$$
\mathcal T_T[f](\omega)=\int W(t,\omega)f(t)W'(t,\omega)\,dt .
$$

**The order is fixed once, in the displays above, and kept to the end**: the left placement multiplies on the left, the right placement on the right, the two-sided placement multiplies by $W$ on the left and by $W'$ on the right. A reader who reverses one of the three mid-article produces the transposed formula, with an error of the size of the transverse plane.

**Why the root is written as a root of one.** The exponent satisfies $\tilde{Ζ}^{2}=e_t$ and the central scalar $i$ carries the sign, which is the convention of *Biquaternion Continuous Harmonic Analysis*. **The letters $R$ and $\tilde{Ζ}$ move no product**, because they differ by a central scalar; they differ only in the sign of the exponent, and that sign is the subject of §*The Two Signs That Fix a Part*.

**Four properties of the root, and which sections need the fourth.** The structural results use three: $R^{2}=-e_t$, $R$ pure, and a transverse element anticommutes with it. The metric results use a fourth, $R^{*}=-R$, which is the same as $\lVert R\rVert_E=1$, and which for a pure $R$ with $R^{2}=-e_t$ says that $R$ has real coordinates. **It holds for exactly the Hermitian roots**: the central pair, which is not pure, and the pure real unit vectors, by the proposition on the Hermitian roots of *Biquaternion Continuous Harmonic Analysis*. **It is not a consequence of the first three.** The element $R=ie_x-\sqrt2\,e_y$ is pure with $R^{2}=-e_t$ and $N(R)=1$, while $R^{*}=ie_x+\sqrt2\,e_y$ and $\lVert R\rVert_E^{2}=3$; §*The Closed Form* shows what such a root does to the metric statements. It is also the root a normal element supplies.

**What is proved, and what is quoted.** That the kernel has algebraic norm one, and Euclidean norm one for the Hermitian root, so that multiplication by it on either side is a Euclidean isometry (§*The Closed Form*); that its commutant is the plane of the root and that it rotates the complementary plane through $4\pi\omega t$ (§*The Commutant and the Complement*); that each one-sided placement is linear over the algebra on exactly one side (§*The One-Sided Placements*); that the two signs of the second root fix complementary halves and forget their frequency (§*What Each Sign Forgets*); that the surviving half is carried at twice the frequency (§*The Doubled Frequency*); and that the two placements differ by the integral of a commutator bounded by $2\lVert P_\perp A\rVert$ (§*The Invariance Groups and Their Intersection*). **The inversion theorem and the uniqueness theorem for the complex transform are quoted** from *Biquaternion Continuous Harmonic Analysis* and are not reproved.

**The sentence that must not be written.** The two-sided kernel is not a one-sided kernel applied twice, and the three transforms are never equal except on the zero function (§*The Invariance Groups and Their Intersection*). What is true is narrower: **on the commutant of $R$ the kernel acts as the identity**, and precisely for that reason the frequency content of that part is destroyed rather than kept. The placement matters most exactly where the three look most alike.

**Boundaries.** The transform, its inversion and its factorization into complex transforms are *Biquaternion Continuous Harmonic Analysis*; the symbol, its zero set and the rank on the null set are *The Fourier Transform and the Symbol of a Differential Operator*; the reciprocal and its poles are *Inversion of the Biquaternion Fourier Transform: Poles, Tails and the Degenerate Set*; the two forms on the algebra are *Norm and Unitary Conventions*; the discrete case, whose kernel order is the model for this article, is *Biquaternion Discrete Harmonic Analysis*.

## The Kernel and the Second Root

### The Closed Form

**Proposition (closed form, unit, inverse, multiplicativity).** For a pure root, with $\theta=2\pi\omega t$,

$$
W(t,\omega)=\cos\theta\,e_t-\sin\theta\,R ,
$$

and the following hold: $N(W(t,\omega))=1$; $\lVert W(t,\omega)\rVert_E=1$ for the Hermitian root; $W(t,\omega)^{-1}=W(-t,\omega)$; the inverse is also the algebra conjugate, $W(t,\omega)^{-1}=\overline{W(t,\omega)}$; and $W(t+s,\omega)=W(t,\omega)W(s,\omega)$.

*Proof.* The exponential of an element with no scalar part splits into the even and the odd parts of its series, which are $\cos\theta\,e_t$ and $-\sin\theta\,R$, because $R^{2}=-e_t$. On the plane the algebraic norm is read off directly: $(a\,e_t+bR)(a\,e_t-bR)=a^{2}-b^{2}R^{2}=a^{2}+b^{2}$, so $N(a\,e_t+bR)=a^{2}+b^{2}$, and $N(W)=\cos^{2}\theta+\sin^{2}\theta=1$ with no hypothesis on the coordinates. The Euclidean norm is $\lVert W\rVert_E^{2}=\cos^{2}\theta+\lVert R\rVert_E^{2}\sin^{2}\theta$, because $e_t$ and $R$ are orthogonal for the form, and it is one exactly when $\lVert R\rVert_E=1$, which is the Hermitian root. The inverse is the same series at $-\theta$, and the conjugate is the same series with $\overline{R}=-R$, which leaves the cosine and reverses the sine. Multiplicativity is the addition formula in a commutative plane.

**Corollary (multiplication by the kernel is a Euclidean isometry, for the Hermitian root).** Let $R^{*}=-R$. Then for every $X\in\mathbb{B}$,

$$
\lVert W(t,\omega)X\rVert_E=\lVert XW(t,\omega)\rVert_E=\lVert X\rVert_E .
$$

*Proof.* Write the form as $\langle X,Y\rangle_E=\operatorname{Sc}(XY^{*})$, whose diagonal is $\lVert X\rVert_E^{2}=\sum_k\lvert X_k\rvert^{2}$, the sum of the eight real numbers $\lvert X_k\rvert^{2}$. The star is the conjugate transpose in the matrix model of *The Fourier Transform and the Symbol of a Differential Operator*, hence an anti-automorphism, and $\operatorname{Sc}(UV)=\operatorname{Sc}(VU)$ for every pair. For the Hermitian root $W^{*}=\cos\theta\,e_t+\sin\theta\,R=W^{-1}$ by the proposition, so $W^{*}W=e_t$ and

$$
\lVert WX\rVert_E^{2}=\operatorname{Sc}\bigl(WXX^{*}W^{*}\bigr)=\operatorname{Sc}\bigl(XX^{*}W^{*}W\bigr)=\lVert X\rVert_E^{2} .
$$

The right-hand case is the same with $WW^{*}=e_t$.

**Remark (a non-Hermitian pure root is not an isometry).** Take $R=ie_x-\sqrt2\,e_y$, whose attached root is $\tilde{Ζ}=e_x+i\sqrt2\,e_y$ with $\tilde{Ζ}^{2}=e_t$. Then $R^{2}=-e_t$, $R$ is pure, $N(R)=1$, and the closed form, the inverse and the multiplicativity of the proposition all hold. But $R^{*}=ie_x+\sqrt2\,e_y\ne-R$, so $W^{*}\ne W^{-1}$, and $\lVert R\rVert_E^{2}=3$ gives $\lVert W\rVert_E^{2}=\cos^{2}\theta+3\sin^{2}\theta\in[1,3]$. Over random $X$ and $\theta$ the ratio $\lVert WX\rVert_E/\lVert X\rVert_E$ is measured between $0.59$ and $2.35$. **Left multiplication by $W$ is then neither an isometry nor a similarity**, and the metric statements below hold for it only in the general forms that §*The Commutant and the Complement* and §*The Commutator Defect* attach to the constants. The same root refutes the shortcut $2\lVert X\rVert_E^{2}=\operatorname{tr}(X\overline{X})$: that trace is $2N(X)$, which is complex, and the trace that gives the Euclidean norm is $\operatorname{tr}(X^{*}X)$, with the factor $\tfrac12$.

**Remark (the central root is the degenerate member of the family).** For $R=\pm i$, that is for $\tilde{Ζ}=\pm e_t$, the kernel is the complex scalar $\cos\theta\mp i\sin\theta$, which commutes with everything. **The two one-sided placements are then the same operator and the two-sided placement is the identity on values.** The article assumes the Hermitian root from here on; the central pair belongs to it, and the placements collapse there as described. **The assumption is a restriction, and it is stated**: a regular biquaternion supplies a pure root, which is Hermitian exactly when the element is normal, as *Biquaternion Continuous Harmonic Analysis* proves in its treatment of the non-Hermitian roots; for the other roots the transform is invertible and not an isometry.

### The Two Roots and the Four Kernels

**Definition (the four kernels).** With $R'$ a second root of $-e_t$, pure and of unit Euclidean length, the four kernels of the family are

$$
Wf,\qquad fW,\qquad WfW^{-1},\qquad WfW ,
$$

the first two the one-sided placements and the last two the two-sided placement with $R'=R$ and with $R'=-R$.

**Remark (why there are four and not more).** The two-sided kernel is $WfW'$ with $W'=\exp(2\pi R'\omega t)$. **The two signs of the second root are the only two that fix a part of the algebra**, which is the proposition of §*The Two Signs That Fix a Part*, and a third root leaves a residue in every summand.

## The Three Placements

**Definition (the three placements).** Let $f:\mathbb{R}\to\mathbb{B}$ be integrable. The left, right and two-sided transforms are the three integrals of the Introduction, each taken over $\mathbb{R}$ in $t$ and evaluated at the real frequency $\omega$.

**Remark (one integral, three products).** All three integrate the same kernel against the same value; what changes is the side on which the kernel meets it. **The distinction is invisible for a scalar-valued function and visible only for a non-commutative algebra**, which is why the complex theory needs one name and this one needs three.

## The Commutant and the Complement

### The Plane of the Root

**Proposition (the commutant of a pure root is the plane of the root).** Let $R$ be pure with $R^{2}=-e_t$, and let $a\in\mathbb{B}$. Then $aR=Ra$ if and only if $a$ lies in $\mathrm{span}_{\mathbb{C}}\{e_t,R\}$, a real subspace of dimension four.

*Proof.* Write $a=a_t+\vec a$ with $\vec a$ the vector part and $R$ read as its vector part. The product rule for vector parts gives $aR-Ra=2\,\vec a\times R$, the cross product being the quaternion one. It vanishes exactly when the two vectors are proportional over $\mathbb{C}$, so $a=a_t+a_RR$ with $a_R$ complex; the four real parameters are the real and imaginary parts of $a_t$ and $a_R$.

**Definition (the plane and its complement).** Write $C(R)=\mathrm{span}_{\mathbb{C}}\{e_t,R\}$ for the plane of the root, a commutative subalgebra of real dimension four, and $V_\perp$ for its complementary subspace with respect to the Euclidean form, also of real dimension four.

**Corollary (conjugation fixes the plane).** For $A\in C(R)$ and all $t,\omega$, $W(t,\omega)A\,W(t,\omega)^{-1}=A$.

*Proof.* Both factors lie in $C(R)$, which is commutative, so they cancel.

### The Two Projections

**Proposition (the projections onto the plane and the complement).** Let $R$ be the Hermitian root. The two elements

$$
P_\parallel A=\tfrac12\bigl(A+RAR^{-1}\bigr),\qquad P_\perp A=\tfrac12\bigl(A-RAR^{-1}\bigr)
$$

satisfy $P_\parallel A+P_\perp A=A$; $P_\parallel A$ lies in $C(R)$ for every $A$; $P_\perp A$ lies in $V_\perp$ for every $A$; and **both are the orthogonal projections for the Euclidean form**.

*Proof.* Since $R^{-1}=-R$ the two expressions add to $A$. For $A\in C(R)$ one has $RAR^{-1}=A$, so $P_\parallel A=A$ and $P_\perp A=0$. For $A=\nu$ in a transverse frame, $R\nu R^{-1}=-\nu$, so $P_\perp\nu=\nu$ and $P_\parallel\nu=0$, and the same holds for $\eta$; the two subspaces span the algebra, so the identities extend by linearity. For the orthogonality, note that the map $\sigma(A)=RAR^{-1}$ is an involution, because $R^{2}=-e_t$ is central, so $P_\parallel$ and $P_\perp$ are the projections onto the eigenspaces of $\sigma$ for the eigenvalues $+1$ and $-1$; and $\sigma$ preserves the Euclidean form, being conjugation by the unitary $R$ of §*The Closed Form*, so the two eigenspaces are orthogonal. **Idempotence together with $P_\parallel P_\perp=0$ would not give this**, which is why the argument is made on $\sigma$.

**Remark (without the Hermitian root the projections are oblique).** For $R=ie_x-\sqrt2\,e_y$ the two maps are still idempotent and still add to the identity, as the first line of the proof shows, but conjugation by $R$ is not a Euclidean isometry, so the two images are complementary subspaces and not perpendicular ones: for one random $A$ the pairing $\langle P_\parallel A,P_\perp A\rangle_E$ is measured at $-6.76$, against $0$ for the Hermitian root. **The word "orthogonal" in the name $P_\perp$ is then no longer earned**, and the commutator estimate of §*The Commutator Defect*, which uses the orthogonal splitting, does not follow.

**Definition (a transverse frame).** Let $\nu,\eta$ be pure with $\nu^{2}=\eta^{2}=-e_t$, orthogonal to each other and to $R$, oriented so that $R\nu=\eta$, $\nu R=-\eta$, $\eta R=\nu$ and $R\eta=-\nu$; then $V_\perp=\mathrm{span}_{\mathbb{R}}\{\nu,\eta\}$.

**Remark (the decomposition is of vector spaces, not of algebras):** the complement is not closed under products, because $\nu\eta=R$ lies in the plane, so the projections are used only as linear maps.

### The Rotation

**Lemma (conjugation rotates the complement).** With $\theta=2\pi\omega t$,

$$
W\nu W^{-1}=\cos 2\theta\,\nu-\sin 2\theta\,\eta,\qquad W\eta W^{-1}=\sin 2\theta\,\nu+\cos 2\theta\,\eta ,
$$

so conjugation by the kernel is the identity on $C(R)$ and a rotation through the angle $4\pi\omega t$ on $V_\perp$.

*Proof.* Multiply out with $W=\cos\theta\,e_t-\sin\theta\,R$ and $W^{-1}=\cos\theta\,e_t+\sin\theta\,R$. For the first, $W\nu=\cos\theta\,\nu-\sin\theta\,\eta$, and the four products with $W^{-1}$ give $\cos^{2}\theta\,\nu-\sin\theta\cos\theta\,\eta-\sin\theta\cos\theta\,\eta-\sin^{2}\theta\,\nu$, using $\nu R=-\eta$ and $\eta R=\nu$; the double-angle formulas give the claim. The second is the same computation with $\nu$ and $\eta$ exchanged.


## The One-Sided Placements

### The Left Placement

**Theorem (the left transform is right-linear and not left-linear).** For integrable $f$ and constant $a\in\mathbb{B}$, $\mathcal T_L[fa]=\mathcal T_L[f]a$. For the left side, $\mathcal T_L[af]=a\mathcal T_L[f]$ for every integrable $f$ if and only if $a\in C(R)$; with $\nu$ in the transverse frame the identity fails, $\mathcal T_L[\nu f]\neq\nu\mathcal T_L[f]$.

*Proof.* The constant on the right passes through the integral because right multiplication is continuous and linear; that is the first claim. For the second, $W\nu=\cos\theta\,\nu-\sin\theta\,\eta$ while $\nu W=\cos\theta\,\nu+\sin\theta\,\eta$, so the two integrands differ by $-2\sin\theta\,\eta$, which is not zero on any interval of $t$ at which $\sin\theta\neq0$; the exactness statement is the corollary of §*The Plane of the Root*.

### The Right Placement

**Theorem (the right transform is left-linear and not right-linear).** For integrable $f$ and constant $a\in\mathbb{B}$, $\mathcal T_R[af]=a\mathcal T_R[f]$. On the right, $\mathcal T_R[fa]=\mathcal T_R[f]a$ for every integrable $f$ if and only if $a\in C(R)$.

*Proof.* The first claim is the argument of the previous theorem with the sides exchanged. For the second, the two integrands differ by $f(\nu W-W\nu)=2\sin\theta\,f\eta$, which does not vanish identically unless $f$ is plane-valued; the exactness statement is again the corollary of §*The Plane of the Root*.

**Proposition (boundedness, for the Hermitian root).** For integrable $f$ and every $\omega$, $\lVert\mathcal T_L[f](\omega)\rVert_E\le\int\lVert f(t)\rVert_E\,dt$, and the same bound holds for $\mathcal T_R$.

*Proof.* The corollary of §*The Closed Form* gives $\lVert Wf\rVert_E=\lVert f\rVert_E$ and $\lVert fW\rVert_E=\lVert f\rVert_E$ pointwise; the triangle inequality for the integral of a norm-valued function gives the bound. **For a general pure root the constant is $\max(1,\lVert R\rVert_E)$**, which is the bound on $\lVert W\rVert_E$, applied to $\lVert WX\rVert_E\le\lVert W\rVert_E\lVert X\rVert_E$.

### The Conjugate Relation

**Theorem (the conjugate of the left transform is the right transform of the conjugate).** For integrable $f$,

$$
\overline{\mathcal T_L[f]}(\omega)=\mathcal T_R[\bar f](-\omega),
$$

the bar being the algebra conjugate.

*Proof.* Conjugation is an antiautomorphism, so $\overline{Wf}=\bar f\,\overline{W}$, and the conjugate of an integral is the integral of the conjugate. For a pure root $\overline{W}=W^{-1}=W(-\cdot,\omega)$ by the proposition of §*The Closed Form*. Hence the left side is $\int\bar f(t)W(t,-\omega)\,dt$, which is the right transform of $\bar f$ at $-\omega$.

**Remark (which conjugation, and why the distinction is not pedantic).** The identity uses the algebra conjugate and fails for the complex conjugate alone. **The complex conjugate of $W$ is not $W^{-1}$** unless the root is central: it leaves $R$ unchanged instead of reversing it, so the two sides differ by an element of the transverse plane. A statement written with the complex conjugate is false, and the error is of the size of the transverse part, which is the whole content of the kernel.

**Remark (inversion).** The left placement is inverted by the conjugate kernel on the left and the right placement by the conjugate on the right,

$$
f(t)=\int\overline{W(t,\omega)}\,\mathcal T_L[f](\omega)\,d\omega,\qquad f(t)=\int\mathcal T_R[f](\omega)\overline{W(t,\omega)}\,d\omega ,
$$

under the hypotheses of the inversion theorem of *Biquaternion Continuous Harmonic Analysis*, which is quoted and not proved here. **What this article adds is that the placement does not change the linearity on the side of the constant**, so the theorem transfers to either side without alteration.

## The Two-Sided Placement and the Two Signs

**Definition (the two-sided transform).** For a second Hermitian root $\tilde{Ζ}'$ of $1$, with $R'=i\tilde{Ζ}'$ and $W'(t,\omega)=\exp(2\pi R'\omega t)$, the two-sided transform is

$$
\mathcal T_T[f](\omega)=\int W(t,\omega)f(t)W'(t,\omega)\,dt .
$$

**Proposition (boundedness, for the Hermitian root).** For integrable $f$ and every $\omega$, $\lVert\mathcal T_T[f](\omega)\rVert_E\le\int\lVert f(t)\rVert_E\,dt$.

*Proof.* For Hermitian roots $W$ and $W'$ are both unitary, and multiplication on either side by a unitary is an isometry by the same computation as the corollary of §*The Closed Form*; so $\lVert WfW'\rVert_E=\lVert f\rVert_E$ pointwise and the triangle inequality applies. For general pure roots the constant becomes $\max(1,\lVert R\rVert_E)\max(1,\lVert R'\rVert_E)$, one factor per kernel.

### The Two Signs That Fix a Part

**Proposition (the two signs that fix a part).** If $R'=R$ then $W'=W^{-1}$ and the two-sided kernel is the conjugation by $W$, which fixes the plane of the root pointwise. If $R'=-R$ then $W'=W$ and the two-sided kernel is $W(\cdot)W$, which fixes the transverse plane pointwise and multiplies the plane of the root by $W^{2}$.

*Proof.* For the first sign, $W'=\exp(2\pi R\omega t)=W(-t,\omega)=W^{-1}$, and conjugation fixes $C(R)$ by the corollary of §*The Plane of the Root*. For the second, $W'=W$, and multiplying out with $W=\cos\theta\,e_t-\sin\theta\,R$ gives

$$
W\nu W=(c^{2}+s^{2})\nu+(cs-sc)\eta=\nu,\qquad W\eta W=(c^{2}+s^{2})\eta+(sc-cs)\nu=\eta ,
$$

with $c=\cos\theta$ and $s=\sin\theta$, using $\nu R=-\eta$ and $\eta R=\nu$; on the plane both factors commute with the value and give $AW^{2}$, and $W^{2}=W(t,2\omega)$ by multiplicativity.

**Proposition (no other sign fixes a part).** Let $R'=\nu$, a pure root of $-e_t$ in the transverse frame. Then $W\nu W'\neq\nu$ and $W\eta W'\neq\eta$ for $\theta$ not a multiple of $\pi$.

*Proof.* With $W'=\cos\theta\,e_t+\sin\theta\,\nu$ and $W\nu=\cos\theta\,\nu-\sin\theta\,\eta$, multiplying out and using $\nu^{2}=-e_t$ and $\eta\nu=-R$ gives

$$
W\nu W'=\cos^{2}\theta\,\nu-\sin\theta\cos\theta\,e_t-\sin\theta\cos\theta\,\eta+\sin^{2}\theta\,R ,
$$

which differs from $\nu$ in the scalar, the transverse and the plane directions at once. **The two signs of the second root are therefore the only two that fix a part of the algebra**, and the display shows the obstruction: a third sign leaves a residue in every summand.

### What Each Sign Forgets

**Theorem (the kernel of the two-sided transform at $R'=R$).** For integrable $f$, $\mathcal T_T[f]$ vanishes at every $\omega$ if and only if $f$ takes values in the plane of the root and $\int f=0$.

*Proof.* Write $f=f_\parallel+f_\perp$ with $f_\parallel$ plane-valued and $f_\perp$ transverse-valued. The plane part is fixed by the conjugation and contributes $\int f_\parallel$, independent of $\omega$. The transverse part is rotated by $4\pi\omega t$, so it contributes an element of $V_\perp$ whose two coefficients are the cosine and sine transforms of the coefficients of $f_\perp$ at frequency $2\omega$; those vanish for all $\omega$ only if $f_\perp=0$, by the inversion theorem for the two real transforms, quoted with the hypothesis that the coefficients be integrable. Hence the transform vanishes everywhere exactly when $\int f_\parallel=0$ and $f_\perp=0$.

**Corollary (the two-sided transform at $R'=R$ is not injective).** It is not injective, and its kernel contains every plane-valued function of zero total integral; for instance $f(t)=t\exp(-t^{2})(e_t+cR)$ with any complex $c$ lies in the kernel.

*Proof.* The integral of $t\exp(-t^{2})$ is zero, so the example is plane-valued with zero total integral and the theorem applies. **The example is checked numerically**: its two-sided transform is zero at three frequencies, to the accuracy of the quadrature.

**Theorem (the kernel at $R'=-R$).** For integrable $f$, $\mathcal T_T[f]$ vanishes at every $\omega$ if and only if $f$ takes values in $V_\perp$ and $\int f=0$.

*Proof.* By the proposition of §*The Two Signs That Fix a Part*, the transverse part is fixed and contributes $\int f_\perp$, independent of $\omega$, while the plane part is multiplied by $W^{2}$ and contributes the left transform of $f_\parallel$ at frequency $2\omega$, which vanishes for all $\omega$ only if $f_\parallel=0$ by the inversion theorem. The conclusion follows.

**Remark (neither sign reduces the two-sided placement to a one-sided one).** The two signs forget complementary halves: **the first forgets the frequency of the plane part, the second the frequency of the transverse part**, and in both cases the forgotten half survives only through its total integral, one element of the algebra and not a function. A one-sided transform forgets nothing, because its kernel never cancels; **so the two-sided transform reduces to a one-sided one on no function except zero.**

### The Doubled Frequency

**Proposition (the surviving half is carried at twice the frequency).** Let $f=f_\parallel+f_\perp$ be integrable with $f_\perp=A_1\nu+A_2\eta$.

- At $R'=R$ the transverse part contributes the pair $\bigl(\int[\cos(4\pi\omega t)A_1-\sin(4\pi\omega t)A_2],\ \int[\sin(4\pi\omega t)A_1+\cos(4\pi\omega t)A_2]\bigr)$, which is the complex transform of $A_1+iA_2$ at frequency $2\omega$.
- At $R'=-R$ the plane part contributes $\mathcal T_L[f_\parallel](2\omega)$, the left transform of the plane part at twice the frequency.

*Proof.* The first is the rotation lemma of §*The Rotation* integrated against the coefficients. The second is the identity $AW^{2}=AW(t,2\omega)$ for $A\in C(R)$, which is multiplicativity of the kernel in the time, integrated over $t$ with the substitution $\omega\mapsto2\omega$ in the definition of the left transform.

**Example (the doubling seen in one kernel).** For $f(t)=\exp(-\pi t^{2})\nu$ and $R'=R$ the two-sided transform is, at every real frequency,

$$
\mathcal T_T[f](\omega)=\exp(-4\pi\omega^{2})\nu .
$$

*Proof.* The transverse coefficient is rotated through $4\pi\omega t$, and only the cosine term survives because $f$ is even and the sine term is odd; the Gaussian identity $\int\exp(-\pi t^{2})\cos(2\pi at)\,dt=\exp(-\pi a^{2})$ at $a=2\omega$ gives the decay rate $4\pi\omega^{2}$. **The transform of a Gaussian is a Gaussian whose exponent is four times the exponent of the one-sided transform**, which is the doubling of the frequency written as a doubling of the constant.

**Proposition (the inversion carries the factor two).** At $R'=R$ and for a transverse-valued integrable $f=A_1\nu+A_2\eta$ with integrable transform, writing $C_1,C_2$ for the two coefficients of the transform,

$$
A_1(t)+iA_2(t)=2\int\bigl(C_1(\omega)+iC_2(\omega)\bigr)\exp(4\pi i\omega t)\,d\omega .
$$

*Proof.* The pair $(C_1,C_2)$ is the real form of the complex transform of $A_1+iA_2$ at the frequency $\alpha=2\omega$; the classical inversion integrates over $d\alpha$, and the change of variable $\alpha=2\omega$ produces the factor $2$ and the argument $4\pi\omega t$.

**Remark (why the doubling must be absorbed).** An inversion written with $d\omega$ and no factor is wrong in the argument, and the error is invisible on a single exponential, which is why it survives review. **The two-sided transform is a one-sided transform of half the function at twice the frequency**, and the inverse carries the factor two in $d(2\omega)$.

| Sign of the second root | Part fixed by the kernel | Part carried at doubled frequency | Part whose frequency is lost |
|---|---|---|---|
| $R'=R$ | the plane of the root | the transverse plane | the plane of the root |
| $R'=-R$ | the transverse plane | the plane of the root | the transverse plane |

## The Invariance Groups and Their Intersection

### The Groups

**Definition (the two invariance groups).** For a placement $\mathcal T$ let

$$
G_L(\mathcal T)=\{a\in\mathbb{B}:\mathcal T[af]=a\mathcal T[f]\ \text{for all integrable }f\},\qquad G_R(\mathcal T)=\{a:\mathcal T[fa]=\mathcal T[f]a\ \text{for all }f\} .
$$

**Theorem (the groups of the three placements).** With $C(R)$ the plane of the root and $C(R')$ the plane of the second root, the groups are as follows.

| Placement | $G_L$ | $G_R$ |
|---|---|---|
| $\mathcal T_L$ | $C(R)$ | $\mathbb{B}$ |
| $\mathcal T_R$ | $\mathbb{B}$ | $C(R)$ |
| $\mathcal T_T$ | $C(R)$ | $C(R')$ |

*Proof.* Each entry restates a computation made above. A constant passes through the left of $\mathcal T_L$ exactly when it commutes with $W(t,\omega)$ for almost every $t$ and $\omega$, which is the condition of §*The Plane of the Root*, and through the right always; the row of $\mathcal T_R$ exchanges the sides. For $\mathcal T_T$ the value separates the two factors, so a constant on the left must commute with $W$ and one on the right with $W'$.

**Corollary (the two-sided placement keeps, on each side, exactly what the corresponding one-sided placement keeps).** $G_L(\mathcal T_T)=G_L(\mathcal T_L)$ and $G_R(\mathcal T_T)=G_R(\mathcal T_R)$. The set of constants over which a placement is bilinear on both sides at once is

$$
G_L(\mathcal T)\cap G_R(\mathcal T);
$$

it is the plane $C(R)$ for each of the three placements when $R'=\pm R$, and the scalars $\mathbb{C}e_t$ for $\mathcal T_T$ when $R'\notin C(R)$. **So the two-sided placement is the only one of the three whose bilinearity can be narrower than a plane**, and that is what the second root does.

*Proof.* The two equalities are read from the table: the effective constraint on the left is always commutation with $W$, and on the right always commutation with $W'$. The intersection for $\mathcal T_T$ is $C(R)\cap C(R')$, which is $C(R)$ when $R'=\pm R$ and $\mathbb{C}e_t$ otherwise, since two planes spanned by distinct pure roots meet only in the scalars; for the one-sided placements it is $C(R)$, one of the two groups being the whole algebra.

**Remark (what "intersection" can and cannot mean).** The two-sided placement is the intersection of the two one-sided ones **in the sense of invariance groups**: it keeps the left action that the left transform keeps and the right action that the right transform keeps. It is not the intersection in the sense of images or kernels, and no statement of that kind is true. **An intersection of images would make the two-sided transform a common part of the other two**, which it is not.

**Proposition (no placement is bilinear over the whole algebra).** For none of the three is $G_L=G_R=\mathbb{B}$.

*Proof.* The algebra is not commutative: $\nu\eta=R$ while $\eta\nu=-R$. A placement bilinear over $\mathbb{B}$ on both sides would have both groups equal to $\mathbb{B}$, and the table gives each placement at least one proper subgroup.

### The Commutator Defect

**Theorem (the two one-sided placements differ by an integral of commutators).** For integrable $f$,

$$
\mathcal T_L[f](\omega)-\mathcal T_R[f](\omega)=\int\bigl[W(t,\omega),f(t)\bigr]dt ,
$$

the difference vanishing identically for every plane-valued $f$ and not vanishing identically for a constant transverse value. Moreover, for the Hermitian root and every $A\in\mathbb{B}$ and every $t,\omega$,

$$
\lVert[W(t,\omega),A]\rVert_E\le 2\lVert P_\perp A\rVert_E ,
$$

and the constant $2$ is attained.

*Proof.* The integrands differ by $Wf-fW$, and the integral of the difference is the difference of the integrals; that is the identity. It vanishes for plane-valued $f$, because $W$ then lies in the commutative plane with the value; and for $f=\nu\chi$ with integrable $\chi$ it is $2\eta\int\chi(t)\sin\theta\,dt$, which is not identically zero in $\omega$ unless $\chi$ vanishes. For the bound, write $A=A_\parallel+A_\perp$ with $A_\parallel=P_\parallel A$ and $A_\perp=P_\perp A$. The kernel commutes with $A_\parallel$, because both lie in $C(R)$, so

$$
[W,A]=[W,A_\perp] ,
$$

and then $\lVert[W,A]\rVert_E\le\lVert WA_\perp\rVert_E+\lVert A_\perp W\rVert_E=2\lVert A_\perp\rVert_E$ by the corollary of §*The Closed Form*, which says that for the Hermitian root multiplication by $W$ on either side is an isometry; if that hypothesis is dropped the estimate becomes $2\lVert W\rVert_E\lVert A_\perp\rVert_E$, which is the next remark. For the sharpness, take $\theta=\pi/2$, that is $W=-R$, and $A=\nu$; then $[W,\nu]=-R\nu+\nu R=-\eta-\eta=-2\eta$, of Euclidean norm $2$, while $\lVert P_\perp\nu\rVert_E=1$.

**Remark (what the bound costs without the Hermitian root).** Without $R^{*}=-R$ the isometry is gone, and only

$$
\lVert[W,A]\rVert_E\le2\lVert W\rVert_E\lVert P_\perp A\rVert_E\le2\max(1,\lVert R\rVert_E)\lVert P_\perp A\rVert_E
$$

survives, by submultiplicativity of the Euclidean norm. For $R=ie_x-\sqrt2\,e_y$ the ratio $\lVert[W,A]\rVert_E/(2\lVert P_\perp A\rVert_E)$ reaches $1.68$ over two thousand sampled pairs $(A,\theta)$, so the constant $2$ is false there and $2\sqrt3$ is what the proof gives. **The example at $\theta=\pi/2$ survives for any root** — $[-R,\nu]=-2\eta$ uses only the frame relations — but its Euclidean norm is $2$ only when the frame has Euclidean norm one, which is the Hermitian case.

**Remark (what the bound says).** The trivial bound $\lVert[W,A]\rVert_E\le2\lVert A\rVert_E$ is also true and says nothing, because it does not vanish where the two placements agree. **The sharper bound vanishes exactly on the plane of the root**, which is the set on which the two transforms coincide, so it is the quantitative form of the corollary above; and since it is attained on a transverse value, the defect is never a small effect to be discarded.

### The Relations Between the Three

**Theorem (factorisation through the one-sided placements).** For integrable $f$ and every root $R'$,

$$
\mathcal T_T[f]=\mathcal T_L\bigl[fW'\bigr]=\mathcal T_R^{(W')}\bigl[Wf\bigr],
$$

where $\mathcal T_R^{(W')}[g]=\int gW'$ is the right placement with kernel $W'$. **The two-sided placement therefore needs no separate inversion theory**: it is a one-sided placement applied to a pointwise multiple, and what it needs instead is the description of §*What Each Sign Forgets*.

*Proof.* Both equalities are associativity of the product inside the integral: $\int WfW'=\int W(fW')=\int(Wf)W'$. Nothing beyond the integrability that makes each integral exist is used.

**Theorem (no two of the three agree on a non-zero function).** For integrable $f$, $\mathcal T_L[f]=\mathcal T_R[f]$ for all $\omega$ exactly when $f$ takes values in $C(R)$, and on such a function $\mathcal T_T[f]=\int f$ when $R'=R$. Consequently the three transforms agree on $f$ only when $f=0$.

*Proof.* The two integrands are equal pointwise exactly when the value commutes with $R$, which gives the first statement. The second is the corollary of §*The Plane of the Root*: a plane-valued function is fixed by the conjugation. For the third, a plane-valued $f$ with $\mathcal T_L[f]=\mathcal T_T[f]$ has $\int Wf=\int f$ for every $\omega$, so the transform of $Wf$ is constant in $\omega$; by the uniqueness theorem for the complex transform, quoted with the hypothesis that $Wf$ be integrable, a function whose transform is constant is supported at the origin, hence $f=0$.

## Summary

The kernel has algebraic norm one, with closed form $\cos(2\pi\omega t)e_t-\sin(2\pi\omega t)R$ for the root $R=i\tilde{Ζ}$ attached to a root $\tilde{Ζ}$ of $1$, with inverse equal to the algebra conjugate and with multiplicativity in the time. **For the Hermitian root it has Euclidean norm one**, and multiplication by it on either side is then an isometry of the eight real coordinates, so every placement is bounded by the integral of the Euclidean norm of the value; for a non-Hermitian pure root neither the isometry nor that bound with constant one holds, and the constant becomes $\max(1,\lVert R\rVert_E)$. Its commutant is the plane of the root, a commutative subalgebra of real dimension four; on that plane conjugation by the kernel is the identity, and on the complementary plane it is a rotation through $4\pi\omega t$.

The left placement is linear on the right over the whole algebra and on the left only over the plane; the right placement is the reverse; and the algebra conjugate of the left transform is the right transform of the conjugate at the opposite frequency, an identity that needs the algebra conjugate and fails for the complex one. Each one-sided placement is inverted by the conjugate kernel on its own side. The two one-sided placements differ by the integral of a commutator, bounded by twice the transverse part of the value and equal to that bound when the kernel has turned a quarter of its period.

The two-sided placement depends on the sign of the second root, and the two signs fix complementary halves. At $R'=R$ the kernel is a conjugation, the plane part is fixed and its frequency content is lost, and the transform is not injective, its kernel being the plane-valued functions of zero total integral. At $R'=-R$ the kernel fixes the transverse plane, the transverse part loses its frequency, and the plane part is carried at twice the frequency. In both signs the surviving half appears at frequency $2\omega$, and the inverse must carry the factor two. **Neither sign turns the two-sided placement into a one-sided one**, and no two of the three agree on a non-zero function. The two-sided placement keeps on each side exactly what the corresponding one-sided placement keeps, so it is the intersection of the two invariance groups; it is the only placement whose bilinearity can be narrower than a plane, and that is what the second root does.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, of real dimension $8$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The units, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | The central scalar imaginary |
| $\tilde{Ζ},\tilde{Ζ}'$ | Roots of $1$, with $\tilde{Ζ}^{2}=\tilde{Ζ}'^{2}=e_t$; $\tilde{Ζ}$ is the Hermitian root, $\tilde{Ζ}^{*}=\tilde{Ζ}$ |
| $R,R'$ | The attached roots of $-e_t$, $R=i\tilde{Ζ}$ and $R'=i\tilde{Ζ}'$, pure with $R^{2}=-e_t$; $R$ is a real unit vector, $R^{*}=-R$ |
| $W,W'$ | The kernels $W(t,\omega)=\exp(-2\pi R\omega t)$ and $W'(t,\omega)=\exp(2\pi R'\omega t)$ |
| $t$ | The time, the variable of integration |
| $\omega$ | The frequency, a real number |
| $\theta$ | The phase $2\pi\omega t$ |
| $c,s$ | The abbreviations $\cos\theta$ and $\sin\theta$ |
| $N(A)$ | The norm $A_t^{2}+A_x^{2}+A_y^{2}+A_z^{2}$, central and complex-valued; **not** the Euclidean norm |
| $\operatorname{Sc}$ | The scalar part, the coefficient of $e_t$ |
| $A^{*}$ | The Euclidean adjoint, the conjugate transpose in the matrix model |
| $\overline{A}$ | The algebra conjugate, which reverses the vector part |
| $\lVert A\rVert_E$ | The Euclidean norm on the eight real coordinates, $\lVert A\rVert_E^{2}=\operatorname{Sc}(AA^{*})=\sum_k\lvert A_k\rvert^{2}$ |
| $A$, $X$, $a$ | Generic elements of the algebra; $a$ is the constant in the linearity statements |
| $\bar f$ | The conjugate-valued function $t\mapsto\overline{f(t)}$ |
| $\mathbb{B}=C(R)\oplus V_\perp$ | The split of the algebra into the plane of the root and its complement |
| $C(R)$ | The plane of the root, $\mathrm{span}_{\mathbb{C}}\{e_t,R\}$, of real dimension four |
| $C(R')$ | The plane of the second root |
| $V_\perp$ | The complementary subspace, $\mathrm{span}_{\mathbb{R}}\{\nu,\eta\}$ |
| $\nu,\eta$ | A transverse frame, pure with $\nu^{2}=\eta^{2}=-e_t$ and $R\nu=\eta$, $\eta R=\nu$ |
| $P_\parallel,P_\perp$ | The projections onto $C(R)$ and onto $V_\perp$, orthogonal for the Hermitian root |
| $A_\parallel,A_\perp$ | The two parts $P_\parallel A$ and $P_\perp A$ |
| $[A,B]$ | The commutator $AB-BA$ |
| $f$ | An integrable $\mathbb{B}$-valued function of the time |
| $\mathcal T_L,\mathcal T_R,\mathcal T_T$ | The left, right and two-sided transforms |
| $\mathcal T_R^{(W')}$ | The right placement with the kernel $W'$ |
| $G_L,G_R$ | The left and right invariance groups of a placement |
| $A_1,A_2$ | The two coefficients of a transverse-valued function, $f=A_1\nu+A_2\eta$ |
| $C_1,C_2$ | The two coefficients of its two-sided transform |
| $\alpha$ | The doubled frequency $2\omega$, the variable of the complex inversion |

## Further Reading

- *Biquaternion Continuous Harmonic Analysis*, for the kernel, its closed form, the two-unit transform, and the inversion and Plancherel theorems quoted here.
- *Biquaternion Discrete Harmonic Analysis*, for what the kernel does to a value in the discrete case, the model for §*The Commutant and the Complement*, which is not repeated here.
- *The Fourier Transform and the Symbol of a Differential Operator*, for the symbol whose left multiplication is the transform of a single exponential, and the zero set that decides where a placement can be inverted.
- *Inversion of the Biquaternion Fourier Transform: Poles, Tails and the Degenerate Set*, for the inverse at a null point of the symbol, where the frequency lost by the two-sided kernel is genuinely lost.
- *Norm and Unitary Conventions*, for the four norms of the algebra and the letters that distinguish them, the Euclidean norm used here being one of the four.
