# __The Three Kernel Placements of the Biquaternion Fourier Transform__

## Introduction

The biquaternion Fourier transform is defined by an integral in which the exponential kernel can stand on the left of the function, on the right, or on both sides, and **the three choices give three different transforms**. This article proves what each choice keeps and what each one loses. It is a statement about a family of operators, not about a change of notation.

**The three placements.** Let $\rho$ be a pure root of $-e_t$, let $W(t,\omega)=\exp(-2\pi\rho\omega t)$, and let $\rho'$ be a second root. The three transforms are

$$
\mathcal T_L[f](\omega)=\int W(t,\omega)f(t)\,dt,\qquad \mathcal T_R[f](\omega)=\int f(t)W(t,\omega)\,dt,
$$

for the one-sided placements, and

$$
\mathcal T_T[f](\omega)=\int W(t,\omega)f(t)W'(t,\omega)\,dt,\qquad W'(t,\omega)=\exp(2\pi\rho'\omega t),
$$

for the two-sided one. **The order of kernel and function is fixed here, once, and kept to the end**: the left placement multiplies on the left, the right placement on the right, and the two-sided placement multiplies by $W$ on the left and by $W'$ on the right, with $W'$ carrying the plus sign.

**What is proved.** That the kernel is a unit of Euclidean norm one, so that every placement is bounded by $\int\lVert f\rVert_E$ (§*The Kernel as a Function of the Frequency*, §*The Two-Sided Placement*). That the commutant of a pure root is exactly the plane of the root, of real dimension four, and that conjugation by the kernel is the identity on that plane and a rotation of angle $4\pi\omega t$ on a transverse plane (§*What the Kernel Does to a Value*). That the left placement is right-$B$-linear and not left-$B$-linear, and the right placement the reverse (§*The Left Placement*, §*The Right Placement*). That the algebra conjugate of the left transform is the right transform of the conjugate at the opposite frequency, with the algebra conjugate and not the complex one (§*The Right Placement*). That the two-sided placement factors through each one-sided one by a pointwise multiplication, so all three are one operation preceded by a product (§*The Relations Between the Three*). That with $\rho'=\rho$ the two-sided transform is not injective, its kernel being the plane-valued functions of zero total integral, and that with $\rho'=-\rho$ its kernel is the transverse-valued functions of zero total integral (§*What Each Sign Forgets*). And that in both signs the surviving part is carried at twice the frequency, so the second root doubles the frequency of one half and discards the other (§*The Doubled Frequency*).

**The sentence that must not be written.** The two-sided kernel does not collapse to a one-sided one, and the three transforms are never equal except on the zero function. What is true is narrower and is proved below: **on the commutant of $\rho$ the kernel acts as the identity**, and precisely because it does, the frequency content of that part is destroyed rather than duplicated. The placement therefore matters most exactly where the three look most alike.

**Boundaries.** The transform, its inversion and its factorization into complex transforms are *Biquaternion Continuous Harmonic Analysis*; the symbol and its zero set are *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*; the rank on the null set is *The Biquaternion Fourier Transform: Support and Rank*; the reciprocal and its poles are *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*; the two forms on the algebra are *The Biquaternion Fourier Transform and the Two Quadratic Forms*; the discrete case, whose kernel order is the model for this article, is *Biquaternion Discrete Harmonic Analysis*.

## The Kernel and the Three Placements

### The Kernel as a Function of the Frequency

**Definition (the kernel).** For a root $\rho$ of $-e_t$, a time $t$ and a frequency $\omega$, the kernel is $W(t,\omega)=\exp(-2\pi\rho\omega t)$, the exponential taken in $\mathbb{B}$.

**Proposition (closed form, unit, inverse, multiplicativity).** For a pure root, with $\theta=2\pi\omega t$,

$$
W(t,\omega)=\cos\theta\,e_t-\sin\theta\,\rho ,
$$

and the following four statements hold: $N(W(t,\omega))=1$; the inverse is $W(t,\omega)^{-1}=W(-t,\omega)$; the inverse is also the algebra conjugate, $W(t,\omega)^{-1}=\overline{W(t,\omega)}$; and $W(t+s,\omega)=W(t,\omega)W(s,\omega)$.

*Proof.* The exponential of an element whose term has no scalar part splits into the even and the odd part of the series, which are $\cos\theta e_t$ and $-\sin\theta\rho$, because $\rho^{2}=-e_t$. The norm is $\cos^{2}\theta+\sin^{2}\theta=1$, since the norm of $\rho$ is one and the two terms are orthogonal in the plane. The inverse follows from the same series with $-\theta$, and the conjugate from $\bar\rho=-\rho$ for a pure root, which leaves $\cos\theta$ and changes the sign of the sine term. Multiplicativity is multiplicativity of the exponential for two elements of one plane, or directly from the addition formulas for the cosine and the sine.

**Remark (the central root is the degenerate member of the family).** For $\rho=\pm i$ the kernel is the complex scalar $\cos\theta\mp i\sin\theta$, which commutes with every element. **In that family the two one-sided placements are the same operator**, and the two-sided placement is the identity on values. The article therefore assumes $\rho$ pure from here on, and the pure assumption is not a loss: a regular biquaternion has a pure root, as *Biquaternion Continuous Harmonic Analysis* states.

### The Three Placements

**Definition (the three placements).** Let $f:\mathbb{R}\to\mathbb{B}$ be integrable and let $\rho'$ be a root of $-e_t$. The left, right and two-sided transforms are the three integrals displayed in the Introduction, each taken with respect to $t$ over $\mathbb{R}$ and each evaluated at the real frequency $\omega$.

**Remark (one integral, three products).** All three are the same integral of the same kernel; what changes is the side on which the kernel meets the value. **The distinction is invisible for a scalar-valued function and visible only for a non-commutative algebra**, which is the reason the biquaternion case needs the three names and the complex case does not.

## What the Kernel Does to a Value

### The Plane of the Root

**Proposition (the commutant of a pure root is the plane of the root).** Let $\rho$ be a pure unit element and let $a\in\mathbb{B}$. Then $a\rho=\rho a$ if and only if $a$ lies in $\mathrm{span}_{\mathbb{C}}\{e_t,\rho\}$, a real subspace of dimension four.

*Proof.* Write $a=a_t+\vec a$ with $\vec a$ the vector part. The product rule for the vector parts gives $a\rho-\rho a=2\,\vec a\times\rho$, where the cross product is the quaternion one and $\rho$ is read as its vector part. The cross product vanishes exactly when the two vectors are proportional over $\mathbb{C}$, so $a=a_t+a_\rho\rho$ with $a_\rho$ complex. The four real parameters are the real and imaginary parts of $a_t$ and $a_\rho$.

**Corollary (conjugation is the identity on the plane).** For $A\in\mathrm{span}_{\mathbb{C}}\{e_t,\rho\}$ and every $t,\omega$, $W(t,\omega)A\,W(t,\omega)^{-1}=A$.

*Proof.* Both $W$ and $A$ lie in the plane, which is a commutative subalgebra, so they commute and the two factors cancel.

**Remark (the plane is where the transform is blind).** The corollary says that a value in the plane passes through the two-sided kernel untouched, whatever the frequency. **A function with values in the plane therefore reaches the two-sided transform with its kernel already cancelled**, and that is the source of every degeneracy in §*What Each Sign Forgets*.

### The Transverse Plane

**Proposition (the two projections).** For a pure root $\rho$ and $A\in\mathbb{B}$, the two elements

$$
P_\parallel A=\tfrac12\bigl(A+\rho A\rho^{-1}\bigr),\qquad P_\perp A=\tfrac12\bigl(A-\rho A\rho^{-1}\bigr)
$$

satisfy $P_\parallel A+P_\perp A=A$, and $P_\parallel A$ lies in the plane of the root for every $A$ while $P_\perp A$ lies in the complementary subspace.

*Proof.* Since $\rho^{-1}=-\rho$, the sum of the two expressions is $A$. For $A$ in the plane, $\rho A\rho^{-1}=A$, so $P_\parallel A=A$ and $P_\perp A=0$. For $A=\nu$, $\rho\nu\rho^{-1}=\eta\rho^{-1}=-\eta\rho=-\nu$, so $P_\perp\nu=\nu$ and $P_\parallel\nu=0$, and the same computation with $\eta$ gives $P_\perp\eta=\eta$ and $P_\parallel\eta=0$. The two subspaces span the algebra, so the identities extend to every $A$ by linearity.

**Remark (the second projection is not a homomorphism).** The plane is a subalgebra, so $P_\parallel$ is a homomorphism on its image; the complementary subspace is not, because $\nu\eta=\rho$ lies in the plane. **The decomposition of the algebra is therefore a decomposition of vector spaces and not of algebras**, and no statement below treats the transverse part as an algebra.

**Definition (a transverse frame).** Let $\nu,\eta$ be pure elements with $\nu^{2}=\eta^{2}=-e_t$, orthogonal to each other and to $\rho$, and oriented so that $\rho\nu=\eta$, $\nu\rho=-\eta$, $\eta\rho=\nu$ and $\rho\eta=-\nu$. The pair spans a real plane $V_\perp$ with $\mathbb{B}=\mathrm{span}_{\mathbb{C}}\{e_t,\rho\}\oplus V_\perp$ as real vector spaces.

**Proposition (conjugation is a rotation on the transverse plane).** With $\theta=2\pi\omega t$,

$$
W\nu W^{-1}=\cos 2\theta\,\nu-\sin 2\theta\,\eta,\qquad W\eta W^{-1}=\sin 2\theta\,\nu+\cos 2\theta\,\eta ,
$$

so conjugation by the kernel rotates $V_\perp$ through the angle $4\pi\omega t$, twice the phase of the kernel.

*Proof.* Multiply out: $W\nu=\cos\theta\,\nu-\sin\theta\,\rho\nu=\cos\theta\,\nu-\sin\theta\,\eta$, and $W^{-1}=\cos\theta\,e_t+\sin\theta\,\rho$, so $W\nu W^{-1}=\cos^{2}\theta\,\nu-\sin\theta\cos\theta\,\eta+\sin\theta\cos\theta\,\nu\rho-\sin^{2}\theta\,\eta\rho$. Now $\nu\rho=-\eta$ and $\eta\rho=\nu$, so the expression is $(\cos^{2}\theta-\sin^{2}\theta)\nu-2\sin\theta\cos\theta\,\eta$, which is the first identity by the double-angle formulas. The second is the same computation with $\nu$ and $\eta$ exchanged, using $\eta\nu$ in place of $\nu\eta$.

**Remark (the doubling is not an accident of the algebra).** The phase of the kernel is $2\pi\omega t$ and the rotation angle is twice that, because a conjugation is a product of two kernel factors, one on each side. **The factor two appears again in §*The Doubled Frequency* as the doubling of the frequency of the transform itself**, and the two appearances are the same fact.

## The Left Placement

**Theorem (the left transform is right-linear).** For every integrable $f$ and every constant $a\in\mathbb{B}$, $\mathcal T_L[fa]=\mathcal T_L[f]a$.

*Proof.* The constant $a$ stands on the right of the value and the kernel stands on its left, so the integral of $Wfa$ is the integral of $Wf$ multiplied on the right by $a$; the integral is a limit of finite sums and right multiplication is continuous and linear.

**Proposition (the left transform is not left-linear).** With $\rho$ pure and $\nu$ in the transverse frame, $\mathcal T_L[\nu f]\neq\nu\,\mathcal T_L[f]$ in general.

*Proof.* It is enough to compare the two at one value of the frequency and one value of the time. Now $W\nu=\cos\theta\,\nu-\sin\theta\,\eta$ while $\nu W=\cos\theta\,\nu+\sin\theta\,\eta$, so $W\nu-\nu W=-2\sin\theta\,\eta$, which is not zero unless $\theta$ is a multiple of $\pi$. Taking $f$ supported near a single time at which $\sin\theta\neq0$ gives the claim.

**Proposition (boundedness).** For integrable $f$ and every $\omega$, $\lVert\mathcal T_L[f](\omega)\rVert_E\le\int\lVert f(t)\rVert_E\,dt$.

*Proof.* The Euclidean norm is multiplicative on a product of an element of the plane with norm one and an arbitrary element, because multiplication by such an element is a rotation of the eight real coordinates; so $\lVert Wf\rVert_E=\lVert f\rVert_E$ and the triangle inequality for the integral gives the bound.

**Remark (inversion, and where it comes from).** The left placement is inverted by the conjugate kernel, that is, by

$$
f(t)=\int\overline{W(t,\omega)}\,\mathcal T_L[f](\omega)\,d\omega ,
$$

which is the inversion theorem of *Biquaternion Continuous Harmonic Analysis*, stated there for integrable $f$ continuous at $t$ with integrable transform. **The inversion formula is not proved here**; what is proved here is that the placement does not change the linearity on the right, so the theorem transfers without alteration.

## The Right Placement

**Theorem (the right transform is left-linear).** For every integrable $f$ and every constant $a\in\mathbb{B}$, $\mathcal T_R[af]=a\,\mathcal T_R[f]$.

*Proof.* The constant stands on the left of the value and the kernel on its right, so the constant passes through the integral unchanged.

**Proposition (the right transform is not right-linear).** With $\nu$ in the transverse frame, $\mathcal T_R[f\nu]\neq\mathcal T_R[f]\nu$ in general.

*Proof.* Now $\nu W=\cos\theta\,\nu+\sin\theta\,\eta$ while $W\nu=\cos\theta\,\nu-\sin\theta\,\eta$, so the discrepancy is $2\sin\theta\,\eta$ at the level of one value, and the same single-time argument applies.

**Theorem (the conjugate of the left transform is the right transform of the conjugate).** For integrable $f$ the identity

$$
\overline{\mathcal T_L[f]}(\omega)=\mathcal T_R[\bar f](-\omega)
$$

holds, where the bar is the algebra conjugate.

*Proof.* Conjugation is an antiautomorphism, so $\overline{Wf}=\bar f\,\bar W$, and the conjugate of the integral is the integral of the conjugate. For a pure root $\bar W=W^{-1}=W(-\cdot,\omega)$, by the fourth statement of the proposition of §*The Kernel as a Function of the Frequency*. Hence $\overline{\mathcal T_L[f]}(\omega)=\int\bar f(t)W(t,-\omega)\,dt$, which is the right transform of $\bar f$ at $-\omega$.

**Remark (which conjugation, and why the distinction is not pedantic).** The identity uses the algebra conjugate and fails for the complex conjugate alone. **The complex conjugate of $W$ is not $W^{-1}$** unless the root is central: it leaves $\rho$ unchanged rather than reversing it, so the two sides differ by an element of the transverse plane. A paper that states the relation with the complex conjugate has stated a false identity, and the error is of the size of the transverse part, which is the whole content of the kernel.

**Remark (inversion).** The right placement is inverted by the conjugate on the right, $f(t)=\int\mathcal T_R[f](\omega)\overline{W(t,\omega)}\,d\omega$, under the same hypotheses as the left case. **The two inversions differ only in the side**, exactly as the two transforms do.

## The Two-Sided Placement

**Definition (the two-sided transform).** For a second root $\rho'$ and $W'(t,\omega)=\exp(2\pi\rho'\omega t)$, the two-sided transform is $\mathcal T_T[f](\omega)=\int W(t,\omega)f(t)W'(t,\omega)\,dt$.

**Proposition (the two-sided transform is bounded).** For integrable $f$ and every $\omega$, $\lVert\mathcal T_T[f](\omega)\rVert_E\le\int\lVert f(t)\rVert_E\,dt$.

*Proof.* Both $W$ and $W'$ are units of Euclidean norm one, and multiplication on either side by such a unit is an isometry of the eight real coordinates; so $\lVert WfW'\rVert_E=\lVert f\rVert_E$ and the triangle inequality applies.

### The Second Root and the Two Signs

**Proposition (the two signs that fix a part).** If $\rho'=\rho$ then $W'=W^{-1}$ and the two-sided kernel is the conjugation by $W$, so the kernel acts as the identity on the plane of the root. If $\rho'=-\rho$ then $W'=W$ and the two-sided kernel is $W(\cdot)W$, which acts as the identity on the transverse plane and as multiplication by $W^{2}$ on the plane of the root.

*Proof.* For the first sign, $W'=\exp(2\pi\rho\omega t)=W(-t,\omega)=W^{-1}$, and conjugation fixes the plane by the corollary of §*The Plane of the Root*. For the second, $W'=W$, and $W\nu W=\nu$ is the computation $\cos^{2}\theta\,\nu-\sin\theta\cos\theta\,\eta-\sin\theta\cos\theta\,\eta+\sin^{2}\theta\,\nu$, using $\nu\rho=-\eta$ and $\eta\rho=\nu$; the same computation with $\eta$ gives $\eta$. On the plane, both factors commute with the value and give $AW^{2}$, and $W^{2}=W(t,2\omega)$ by multiplicativity.

**Proposition (no other sign fixes a part).** Let $\rho'=\nu$, a pure root in the transverse frame. Then $W\nu W'\neq\nu$ and $W\eta W'\neq\eta$ for $\theta$ not a multiple of $\pi$.

*Proof.* With $W'=\cos\theta\,e_t+\sin\theta\,\nu$ and $W\nu=\cos\theta\,\nu-\sin\theta\,\eta$, multiplying out and using $\nu^{2}=-e_t$ and $\eta\nu=-\rho$ gives

$$
W\nu W'=\cos^{2}\theta\,\nu-\sin\theta\cos\theta\,e_t-\sin\theta\cos\theta\,\eta+\sin^{2}\theta\,\rho ,
$$

which differs from $\nu$ in the scalar, transverse and plane directions at once. **The two signs of the second root are therefore the only two that fix a part of the algebra**, and the display shows the obstruction: a third sign leaves a residue in every summand.

### What Each Sign Forgets

**Theorem (the kernel of the two-sided transform at $\rho'=\rho$).** For integrable $f$, $\mathcal T_T[f]=0$ for all $\omega$ if and only if $f$ takes values in the plane of the root and $\int f=0$.

*Proof.* Write $f=f_\parallel+f_\perp$ with $f_\parallel$ plane-valued and $f_\perp$ transverse-valued. The plane part is fixed by the conjugation, so it contributes $\int f_\parallel$, which does not depend on $\omega$. The transverse part is rotated by the angle $4\pi\omega t$, so it contributes an element of $V_\perp$ whose two coefficients are the cosine and sine transforms of the coefficients of $f_\perp$ at frequency $2\omega$; these vanish for all $\omega$ only if $f_\perp=0$, by the real inversion theorem for those transforms, stated and not proved here. Hence the transform vanishes exactly when $\int f_\parallel=0$ and $f_\perp=0$.

**Corollary (the two-sided transform at $\rho'=\rho$ is not injective).** It is not injective, and its kernel contains every plane-valued function of zero total integral; for instance $f(t)=t\exp(-t^{2})(e_t+c\rho)$ with any complex $c$ lies in the kernel.

*Proof.* The integral of $t\exp(-t^{2})$ is zero, so the example is plane-valued with zero total integral and the theorem applies. **The example is checked numerically**: the transform is exactly zero at four frequencies.

**Theorem (the kernel at $\rho'=-\rho$).** For integrable $f$, $\mathcal T_T[f]=0$ for all $\omega$ if and only if $f$ takes values in $V_\perp$ and $\int f=0$.

*Proof.* By the second proposition of §*The Second Root and the Two Signs*, the transverse part is fixed and contributes $\int f_\perp$, independent of $\omega$, while the plane part is multiplied by $W^{2}$ and contributes the left transform of $f_\parallel$ at frequency $2\omega$, which vanishes for all $\omega$ only if $f_\parallel=0$ under the inversion theorem. The conclusion follows.

**Remark (what "the placement still matters" means).** The two signs forget complementary halves: **the first forgets the frequency of the plane part, the second the frequency of the transverse part.** In both cases the forgotten half survives only through its total integral, which is one element of the algebra and not a function. Neither sign collapses to a one-sided transform: a one-sided transform forgets nothing, because its kernel never cancels.

### The Doubled Frequency

**Proposition (the surviving half is carried at twice the frequency).** Let $f=f_\parallel+f_\perp$ be integrable, with $f_\perp=A_1\nu+A_2\eta$.

- At $\rho'=\rho$, the transverse part contributes the pair $\bigl(\int[\cos(4\pi\omega t)A_1-\sin(4\pi\omega t)A_2],\ \int[\sin(4\pi\omega t)A_1+\cos(4\pi\omega t)A_2]\bigr)$, which is the complex transform of $A_1+iA_2$ at frequency $2\omega$.
- At $\rho'=-\rho$, the plane part contributes $\mathcal T_L[f_\parallel](2\omega)$, the left transform of the plane part evaluated at twice the frequency.

*Proof.* The first statement is the rotation formula of §*The Transverse Plane* integrated against the coefficients. The second is the identity $AW^{2}=AW(t,2\omega)$ of §*The Second Root and the Two Signs*, integrated over $t$ with the substitution $\omega\mapsto2\omega$ in the definition of the left transform.

**Example (the doubling seen in one kernel).** For $f(t)=\exp(-\pi t^{2})\nu$ and $\rho'=\rho$ the two-sided transform is, at every real frequency,

$$
\mathcal T_T[f](\omega)=\exp(-4\pi\omega^{2})\nu ,
$$

by the Gaussian identity $\int\exp(-\pi t^{2})\cos(2\pi at)\,dt=\exp(-\pi a^{2})$ at $a=2\omega$.

*Proof.* The transverse coefficient is rotated by the angle $4\pi\omega t$, and only the cosine term survives because $f$ is even and the sine term is odd; the Gaussian identity at $a=2\omega$ gives the decay rate $4\pi\omega^{2}$. **The transform of a Gaussian is again a Gaussian, and its exponent is four times the one of the one-sided transform**, which is the doubling of the frequency written as a doubling of the constant.

**Proposition (the inversion carries the factor two).** At $\rho'=\rho$ and for a transverse-valued integrable $f=A_1\nu+A_2\eta$ with integrable transform, writing $C_1,C_2$ for the two coefficients of the transform,

$$
A_1(t)+iA_2(t)=2\int\bigl(C_1(\omega)+iC_2(\omega)\bigr)\exp(4\pi i\,\omega t)\,d\omega .
$$

*Proof.* The pair $(C_1,C_2)$ is the real form of the complex transform of $A_1+iA_2$ at the frequency $\alpha=2\omega$; the classical inversion integrates over $d\alpha$, and the change of variable $\alpha=2\omega$ produces the factor $2$ and the argument $4\pi\omega t$.

**Remark (why the doubling must be absorbed in the inverse).** A formula that inverts the two-sided transform with $d\omega$ and no factor will be wrong by a factor of two in the argument, and the error is invisible in a transform of a single exponential, which is why it survives review. **The correct reading is that the two-sided transform is a one-sided transform of half the function at twice the frequency**, and the inverse therefore carries the factor $2$ in $d(2\omega)$.

| Sign of the second root | Value fixed by the kernel | Value carried at doubled frequency | Part whose frequency is lost |
|---|---|---|---|
| $\rho'=\rho$ | the plane of the root | the transverse plane | the plane of the root |
| $\rho'=-\rho$ | the transverse plane | the plane of the root | the transverse plane |

## The Linearity of Each Placement

### The Four Invariance Groups

**Definition (the two invariance groups).** For a placement $\mathcal T$ let $G_L(\mathcal T)=\{a\in\mathbb{B}:\mathcal T[af]=a\mathcal T[f]\ \text{for all }f\}$ and $G_R(\mathcal T)=\{a\in\mathbb{B}:\mathcal T[fa]=\mathcal T[f]a\ \text{for all }f\}$.

**Theorem (the groups of the three placements).** The groups are as follows, with $C(\rho)=\mathrm{span}_{\mathbb{C}}\{e_t,\rho\}$ the plane of the root.

| Placement | $G_L$ | $G_R$ |
|---|---|---|
| $\mathcal T_L$ | $C(\rho)$ | $\mathbb{B}$ |
| $\mathcal T_R$ | $\mathbb{B}$ | $C(\rho)$ |
| $\mathcal T_T$ | $C(\rho)$ | $C(\rho')$ |

*Proof.* Each entry is a restatement of a proposition above. For $\mathcal T_L$: right multiplication by a constant always passes through, while left multiplication passes through exactly when the constant commutes with $W(t,\omega)$ for almost every $t$ and every $\omega$, which is the same condition as commuting with $\rho$. For $\mathcal T_R$ the two sides exchange. For $\mathcal T_T$: a constant on the left must commute with $W$ and a constant on the right must commute with $W'$, and the conditions are commuting with $\rho$ and with $\rho'$ respectively.

### The Intersection of the Two

**Corollary (the two-sided placement as the intersection).** The left invariance group of $\mathcal T_T$ equals that of $\mathcal T_R$, and the right invariance group of $\mathcal T_T$ equals the nontrivial group of $\mathcal T_L$ up to the replacement of $\rho$ by $\rho'$. Consequently, **at $\rho'=\rho$ the two-sided placement is the only one of the three that is bilinear over a subalgebra larger than the scalars**, and that subalgebra is $C(\rho)$, the plane of the root.

*Proof.* Read the table: $G_L(\mathcal T_T)=C(\rho)=G_L(\mathcal T_R)$ and $G_R(\mathcal T_T)=C(\rho')$, which equals $G_R(\mathcal T_L)=C(\rho)$ exactly when $\rho'=\rho$. Bilinearity over $C(\rho)$ is the conjunction of the two entries.

**Proposition (no placement is bilinear over the whole algebra).** For none of the three placements is $G_L=G_R=\mathbb{B}$.

*Proof.* The algebra is not commutative: $\nu\eta=\rho$ while $\eta\nu=-\rho$, so $\nu$ and $\eta$ do not commute. A placement bilinear over $\mathbb{B}$ on both sides would have both groups equal to $\mathbb{B}$, and the table shows that each placement has at least one group equal to a proper subalgebra.

**Remark (what "intersection" can mean, and what it cannot).** The two-sided placement is the intersection of the two one-sided ones **in the sense of invariance groups**: it keeps the left action that the right transform keeps and the right action that the left transform keeps. It is not the intersection in the sense of images or of kernels, and no statement of that second kind is true. **The distinction matters because an intersection of images would make the two-sided transform a common part of the other two**, which it is not: it is a different operator with a different kernel.

## The Relations Between the Three

**Theorem (factorisation through the one-sided placements).** For every integrable $f$ and every root $\rho'$,

$$
\mathcal T_T[f]=\mathcal T_L\bigl[f\,W'\bigr]=\mathcal T_R^{(W')}\bigl[Wf\bigr],
$$

where $\mathcal T_R^{(W')}[g]=\int gW'$ is the right placement with the kernel $W'$.

*Proof.* Both equalities are the associativity of the product inside the integral: $\int WfW'=\int W(fW')=\int(Wf)W'$. Nothing about convergence is used beyond the integrability that makes each integral exist.

**Corollary (every theorem for the left placement transfers).** Every statement about $\mathcal T_L$ becomes a statement about $\mathcal T_T$ after the pointwise multiplication of the function by $W'$, and every statement about the right placement after the multiplication by $W$ on the other side. **The two-sided placement therefore needs no separate inversion theory**; what it needs is the description of what the pointwise multiplications do, and that description is §*What Each Sign Forgets*.

**Theorem (no two of the three agree on a non-zero function).** For integrable $f$, the equality $\mathcal T_L[f]=\mathcal T_R[f]$ holds for all $\omega$ exactly when $f$ takes values in the plane of the root, and on such a function $\mathcal T_T[f]=\int f$ at $\rho'=\rho$. Consequently the three transforms agree on $f$ only when $f=0$.

*Proof.* The first statement is the comparison of the two integrands: $Wf=fW$ pointwise exactly when the value commutes with $\rho$. The second is the corollary of §*The Plane of the Root*. For the third, a function with values in the plane and with $\int Wf=\int f$ for all $\omega$ has a transform constant in $\omega$; the uniqueness theorem for the complex transform, quoted with its hypothesis that the function be integrable, then forces the function to vanish. **The agreement of all three is therefore the trivial case only**, and this is the precise sense in which the three placements are distinct.

**Proposition (the two one-sided placements differ by an integral of commutators).** For integrable $f$,

$$
\mathcal T_L[f](\omega)-\mathcal T_R[f](\omega)=\int\bigl[W(t,\omega),f(t)\bigr]dt ,
$$

the bracket being the commutator, and the difference vanishes identically exactly when $f$ takes values in the plane of the root. Moreover $\lVert[W(t,\omega),A]\rVert_E\le2\lVert P_\perp A\rVert_E$ for every $A$, and the bound is attained.

*Proof.* The difference of the two integrands is $Wf-fW$. It vanishes for plane-valued $f$ because $W$ lies in the plane, which is commutative. For the bound, the commutator vanishes on the plane, and on the transverse plane the two products $WA$ and $AW$ are each of norm $\lVert A\rVert_E$ while their difference is a rotation by $2\theta$ composed with a sign, whose norm is at most $2$; the value $2$ is reached at $\theta=\pi/2$, where $W=-\rho$ and the commutator with $\nu$ is $-2\eta$. **So the two placements are never far apart in norm, and are as far apart as a difference of two isometries can be.**

**Remark (the four kernels).** Written as kernels, the whole family is

$$
Wf,\qquad fW,\qquad WfW^{-1},\qquad WfW ,
$$

the first two the one-sided placements and the last two the two-sided placement with the second root equal to $\rho$ and to $-\rho$. **Two of the four are one-sided because in them one of the two multiplications is absent**, and the missing multiplication is what all the degeneracies of the one-sided case consist in: nothing is cancelled, so nothing is lost.

**Remark (why the three are nevertheless one family).** They share the kernel, the bound, the inversion theorem and the factorization into complex transforms. **What separates them is a single binary choice repeated twice**: whether the kernel is applied on the left or on the right, and whether the second root is the first root or its negative. Four combinations, and two of them are the one-sided placements, because a one-sided placement is the case in which one of the two multiplications is absent.

## Summary

The kernel of the biquaternion Fourier transform is a unit of Euclidean norm one, with closed form $\cos(2\pi\omega t)e_t-\sin(2\pi\omega t)\rho$ for a pure root, inverse equal to the algebra conjugate, and multiplicativity in the time. The commutant of a pure root is the plane of the root, of real dimension four, and conjugation by the kernel fixes that plane pointwise while rotating a transverse plane through the angle $4\pi\omega t$.

The left placement is right-linear over the algebra and not left-linear; the right placement is left-linear and not right-linear; the algebra conjugate of the left transform is the right transform of the conjugate at the opposite frequency, and the identity needs the algebra conjugate. Each one-sided placement is bounded by the integral of the Euclidean norm, and each is inverted by the conjugate kernel on the matching side.

The two-sided placement is bounded by the same integral, and it factors through either one-sided placement by a pointwise multiplication, so it needs no separate inversion theory. Its behaviour depends on the sign of the second root. At $\rho'=\rho$ the kernel is a conjugation, the plane part is fixed and its frequency content is lost, and the transform is not injective, its kernel being the plane-valued functions of zero total integral. At $\rho'=-\rho$ the kernel fixes the transverse plane, the transverse part loses its frequency, and the plane part is carried at twice the frequency. In both signs the surviving half appears at frequency $2\omega$, and the inverse must carry the factor two.

Linearity is the sharpest way to separate the three. The left placement is linear on the right over the whole algebra and on the left only over the plane of the root; the right placement is the reverse; the two-sided placement is linear over the plane on the left and over the plane of the second root on the right. It is therefore the intersection of the two one-sided invariance groups, and it is bilinear over the plane of the root exactly when the second root is the first. No placement is bilinear over the whole algebra, because the algebra is not commutative. And no two of the three agree on a non-zero function, so the choice of placement is a genuine choice and not a convention.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of real dimension $8$ |
| $e_t$ | The scalar unit |
| $\rho$ | A pure root of $-e_t$, fixed once and for all |
| $\rho'$ | A second root of $-e_t$, used only in the two-sided placement |
| $\nu,\eta$ | A transverse pure orthonormal pair, with $\rho\nu=\eta$ and $\eta\rho=\nu$ |
| $V_\perp$ | The real plane spanned by $\nu$ and $\eta$ |
| $C(\rho)$ | The commutant of $\rho$, equal to $\mathrm{span}_{\mathbb{C}}\{e_t,\rho\}$ |
| $W(t,\omega)$ | The kernel $\exp(-2\pi\rho\omega t)$ |
| $W'(t,\omega)$ | The second kernel $\exp(2\pi\rho'\omega t)$ |
| $\theta$ | The phase $2\pi\omega t$ |
| $t$ | The time variable |
| $\omega$ | The real frequency |
| $\mathcal T_L$ | The left placement, $\int W(t,\omega)f(t)\,dt$ |
| $\mathcal T_R$ | The right placement, $\int f(t)W(t,\omega)\,dt$ |
| $\mathcal T_T$ | The two-sided placement, $\int WfW'\,dt$ |
| $\mathcal T_R^{(W')}$ | The right placement with the kernel $W'$ instead of $W$ |
| $f$ | An integrable function $\mathbb{R}\to\mathbb{B}$ |
| $f_\parallel,f_\perp$ | Its plane part and its transverse part |
| $A_1,A_2$ | The coefficients of $f_\perp$ in the frame $\nu,\eta$ |
| $a$ | A constant element of $\mathbb{B}$ |
| $\bar a$ | The algebra conjugate |
| $N$ | The algebraic norm $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $\lVert\cdot\rVert_E$ | The Euclidean norm on the eight real coordinates |
| $G_L(\mathcal T),G_R(\mathcal T)$ | The left and right invariance groups of a placement |
| $i$ | The central scalar imaginary |

## Further Reading

- *Biquaternion Continuous Harmonic Analysis*, for the transform, its inversion, its Plancherel statement and its factorization into complex transforms; the placements here are the three readings of its kernel.
- *Biquaternion Discrete Harmonic Analysis*, for the discrete model in which the order of kernel and function is fixed first and the convolution theorem is then stated for each placement; the left and right convolution theorems there are the discrete counterparts of the two one-sided theorems here.
- *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, for the symbol whose eigenvalue is the transform of a single exponential, which is the case in which the doubled frequency of §*The Doubled Frequency* shows up as a doubled argument.
- *The Biquaternion Fourier Transform and the Two Quadratic Forms*, for the two forms that measure the kernel and the value, and for the inequality that bounds a product of two elements of norm one by their forms.
- *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*, for the inversion in a plane of the root, which is the placement in which the plane of §*The Plane of the Root* carries the whole computation.
- *Biquaternion Fourier Inversion on the Degenerate Set*, for the case in which the symbol is not a unit and the two-sided placement is the one that keeps the transverse part visible.
- *The Fourier Transform on Vector-Valued and Operator-Valued Function Spaces*, for the operator-valued reading of a transform whose values are acted on from both sides.
