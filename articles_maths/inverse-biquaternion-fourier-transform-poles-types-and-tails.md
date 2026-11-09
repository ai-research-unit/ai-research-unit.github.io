# __The Inverse Biquaternion Fourier Transform: Poles, Types and Tails__

## Introduction

This article is a programme. It asks for the kernel of the reciprocal of a biquaternion symbol, and it answers the question completely in one frequency variable and not at all in two or more; the sections are marked with what each one proves and what each one leaves open.

**The object.** Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with units $e_t,\vec e_x,\vec e_y,\vec e_z$, the relations $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, and the central imaginary $i$; let $\tilde{Ζ}$ be a pure root of $1$, fixed once and for all, so that $\tilde{Ζ}^{2}=e_t$ and $(\tilde{Ζ},\tilde{Ζ})=-1$; and let $W(t,\omega)=\exp(-2\pi i\tilde{Ζ}\omega t)$ be the kernel of *Biquaternion Continuous Harmonic Analysis*, multiplying the function on the left. For a symbol $\Sigma$ of a constant-coefficient operator, the object of this article is the **kernel of the reciprocal**,

$$
\kappa_\Sigma(t)=\int_{\mathbb{R}^n}\exp\bigl(2\pi i\tilde{Ζ}\,\omega\cdot t\bigr)\,\Sigma(\omega)^{-1}\,d\omega ,
$$

which is the element that carries a datum to a solution of the equation. Three questions decide what that integral means: where $\Sigma^{-1}$ fails to exist, which is the question of the poles; how the kernel behaves at large $\lvert t\rvert$, which is the question of the type; and what the singularity contributes at large time, which is the question of the tail.

**The status of the four sections, stated at once.** §*Residues at a Simple Null Point* and §*Residues at a Repeated Null Point* are proved, in one frequency variable, for a symbol that takes its values in a commutative plane of $\mathbb{B}$; the proofs are short and the formulas are exact. §*Exponential Type and the Tail* is proved in the easy direction of the Paley–Wiener correspondence and quoted in the converse, exactly as *The Inverse Fourier Transform of a Symbol* does in the real algebra, and the rate that a pole fixes is proved by a contour computation in one variable. §*Counting in Peirce Coordinates* is proved where it is algebraic and quoted where it needs the argument principle. §*The Obstacle: Codimension Two* proves that the one-variable method cannot be extended, and states what would replace it; nothing there is a theorem about the kernel. **The article is a programme because the last of these is the general case.**

**The warning, before any formula.** In two or more frequency variables there is no contour to close. The singular set of the reciprocal is cut by two real equations, and after the frequency is complexified it is a complex hypersurface of real codimension two; a hypersurface is not a point, so there is no isolated pole, no partial fraction expansion, and no sum of residues. What replaces the residue is a residue current, or a Leray form integrated over a real cycle that links the hypersurface. §*The Obstacle: Codimension Two* says exactly how far that goes and where it stops.

**Boundaries.** The transform itself, its kernel and its closed form are *Biquaternion Continuous Harmonic Analysis*; the symbol, the block determinant $\lvert N\rvert^{4}$ and the null cone are *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*; the support of the transformed object and the rank of the symbol on the null set are *The Biquaternion Fourier Transform: Support and Rank*; the real-algebra version of the three questions is *The Inverse Fourier Transform of a Symbol*; the placement of the kernel on the left, on the right or on both sides is *The Three Kernel Placements of the Biquaternion Fourier Transform*; the inversion through a generalised inverse is *Biquaternion Fourier Inversion on the Degenerate Set*. This article takes all of them as given and adds the reciprocal and its kernel.

**One convention, and why it is stated.** The eigenvalue of the transform at a real frequency $\omega$ is written $\Sigma(\omega)=\sum_\alpha a_\alpha\prod_k(2\pi i\tilde{Ζ}\omega_k)^{\alpha_k}$, an element of $\mathbb{B}$, exactly as in *The Biquaternion Fourier Transform: Support and Rank*. Inside a commutative plane the element is written $a(\omega)e_t+b(\omega)\tilde{Ζ}$, and its two **Peirce scalars** are $\sigma_\pm=a\pm b$, the coefficients of the element on the idempotents $\Pi_\pm(\tilde{Ζ})=\tfrac12(e_t\pm\tilde{Ζ})$. The pair is a pair of algebra homomorphisms on the plane and it separates points; what it does not do is decide whether an element is a unit, since the element is a unit exactly when **both** scalars are nonzero. §*What the Reduction Does Not Do* uses both facts.

## The Inverse Integral and the Plane Case

### The Kernel and the Integral

**Definition (the kernel of the symbol).** Let $\Omega(P)=\{\omega:N(\Sigma(\omega))=0\}$ be the frequency set, so that $\Sigma(\omega)$ is a unit exactly off $\Omega(P)$. The **reciprocal** is $m_\Sigma(\omega)=\Sigma(\omega)^{-1}$ on the complement of $\Omega(P)$, and the **kernel of the symbol** is its inverse transform, the integral displayed in the Introduction, read as a function where it converges and as a distribution where it does not.

**Remark (why the integral is the only thing there is).** The transform of a solution of $P(D)u=f$ is $\Sigma^{-1}$ times the transform of $f$, by the eigenvalue identity, so the solution is the convolution $u=\kappa_\Sigma*f$ and every question about the solution at large $\lvert x\rvert$ is a question about the kernel at large $\lvert t\rvert$. **The three themes of this article are three readings of one integral**: where its integrand blows up, how far the blow-up sits from the real frequencies, and what the blow-up contributes.

**Remark (the two normalisations in play).** Neither the transform nor its inverse carries a constant outside the exponent, because the factor $2\pi$ sits in the exponent through $\omega\cdot t$. **Every rate in this article is therefore a rate in $2\pi\delta$ and not in $\delta$**, where $\delta$ is a distance in the frequency plane; a formula imported from a convention with the constant outside will be wrong by that factor.

### Reduction to a Commutative Plane

**Lemma (the plane case).** Let $\Sigma$ take its values in the real span of $e_t$ and $\tilde{Ζ}$, so that $\Sigma(\omega)=a(\omega)e_t+b(\omega)\tilde{Ζ}$ with $a,b$ complex-valued, and write $\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$. Then $\Sigma=\sigma_+\Pi_++\sigma_-\Pi_-$ with $\sigma_\pm=a\pm b$, the norm is $N(\Sigma)=a^{2}-b^{2}=\sigma_+\sigma_-$, the reciprocal is

$$
\Sigma(\omega)^{-1}=\frac{a(\omega)e_t-b(\omega)\tilde{Ζ}}{a(\omega)^{2}-b(\omega)^{2}}=\sigma_+(\omega)^{-1}\Pi_++\sigma_-(\omega)^{-1}\Pi_- ,
$$

and the kernel is a pair of classical one-variable integrals, one on each ideal.

*Proof.* The plane is commutative, because $\tilde{Ζ}^{2}=e_t$ and $\tilde{Ζ}$ commutes with $e_t$ and with $i$, so $(a e_t+b\tilde{Ζ})(a e_t-b\tilde{Ζ})=a^{2}e_t-ab\tilde{Ζ}+ba\tilde{Ζ}-b^{2}\tilde{Ζ}^{2}=(a^{2}-b^{2})e_t$. The idempotents satisfy $\Pi_\pm^{2}=\Pi_\pm$, $\Pi_+\Pi_-=0$, $\Pi_++\Pi_-=e_t$ and $\Pi_+-\Pi_-=\tilde{Ζ}$, so $a e_t+b\tilde{Ζ}=(a+b)\Pi_++(a-b)\Pi_-$ and the two displays follow. For the kernel, $W$ lies in the same plane and $\exp(2\pi i\tilde{Ζ}\omega t)=\exp(2\pi i\omega t)\Pi_++\exp(-2\pi i\omega t)\Pi_-$, so the integrand splits into two scalar contour integrals, one on each ideal, carrying conjugate unit complex exponentials.

**Remark (what the lemma buys, and what it costs).** It buys everything in one frequency variable: the reciprocal is a quotient of two polynomials, so the poles are the zeros of the denominator and the kernel is a sum of elementary contour integrals. It costs the general case: it applies only when the symbol stays in one plane, and even inside the plane one classical intuition fails.

### What the Reduction Does Not Do

**Proposition (a Peirce scalar is not injective, and its kernel is the null set of the plane).** The map $a e_t+b\tilde{Ζ}\mapsto a+b$ sends the plane onto $\mathbb{C}$ and is a homomorphism, but it is not injective: its kernel is spanned over $\mathbb{C}$ by $e_t-\tilde{Ζ}$, an element with $N(e_t-\tilde{Ζ})=1-1=0$. Consequently the plane is isomorphic, as an algebra, to $\mathbb{C}\times\mathbb{C}$ and not to $\mathbb{C}$, and the two components are the Peirce scalars $\sigma_+=a+b$ and $\sigma_-=a-b$.

*Proof.* The map is $\mathbb{C}$-linear and sends $e_t\mapsto1$, $\tilde{Ζ}\mapsto1$, and it is multiplicative because $(ae_t+b\tilde{Ζ})(ce_t+d\tilde{Ζ})=(ac+bd)e_t+(ad+bc)\tilde{Ζ}$ gives $(a+b)(c+d)=ac+ad+bc+bd$. It annihilates $e_t-\tilde{Ζ}$, which is nonzero, so it is not injective. On the other hand $(a e_t+b\tilde{Ζ})(a e_t-b\tilde{Ζ})=(a^{2}-b^{2})e_t$ shows that $N$ corresponds under the map to the product $\sigma_+\sigma_-$, and the pair $(\sigma_+,\sigma_-)$ separates points of the plane because $a=(\sigma_++\sigma_-)/2$ and $b=(\sigma_+-\sigma_-)/2$.

**Remark (what this changes in every formula below).** The zero set of $N$ inside the plane is the union of the two sets $\sigma_+=0$ and $\sigma_-=0$, and the reciprocal blows up on **both**, one ideal at a time: at a point where $\sigma_+=0$ and $\sigma_-\ne0$ the element is $\sigma_-\Pi_-$, a nonzero zero divisor whose norm vanishes, the component on $\Pi_+\mathbb{B}$ is singular and the component on $\Pi_-\mathbb{B}$ is regular; at a point where $\sigma_-=0$ the two roles are exchanged. **The word "pole" therefore does not mean "zero of the element"**, and the biquaternion element almost never vanishes at a pole. This is the difference between this article and *The Inverse Fourier Transform of a Symbol*: there the reciprocal blows up where the symbol vanishes, here it blows up where the symbol ceases to be a unit, and the two sets are different.

**Proposition (a null element need not vanish).** There are elements of $\mathbb{B}$ of norm zero that are not zero, and in the plane of $e_t$ and $\tilde{Ζ}$ they are exactly the multiples of $e_t+\tilde{Ζ}$ and of $e_t-\tilde{Ζ}$.

*Proof.* $N(e_t+\tilde{Ζ})=1-1=0$ with $e_t+\tilde{Ζ}=2\Pi_+\ne0$. In the plane $N=\sigma_+\sigma_-$, which vanishes exactly when one of the two scalars does, and $\sigma_+=0$ means $a=-b$, that is the element $b(\tilde{Ζ}-e_t)=-2b\Pi_-$; the other scalar gives the other family.

## Residues at a Simple Null Point

### The Reciprocal as Adjugate over Norm

**Proposition (the reciprocal as an adjugate over the norm).** Let $\tilde Q\in\mathbb{B}$ be arbitrary. In a real basis of $\mathbb{B}$ the block $L_{\tilde Q}$ has determinant $\lvert N(\tilde Q)\rvert^{4}$, and the entries of $L_{\tilde Q}^{-1}$ are the entries of its adjugate divided by that determinant. In the plane of $e_t$ and $\tilde{Ζ}$ the same statement collapses to the single quotient

$$
\Sigma^{-1}=\frac{\operatorname{ad}\Sigma}{N(\Sigma)},\qquad \operatorname{ad}\bigl(a e_t+b\tilde{Ζ}\bigr)=a e_t-b\tilde{Ζ} ,
$$

with $\operatorname{ad}\Sigma$ polynomial in the coefficients.

*Proof.* The determinant formula is the proposition of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*. The adjugate is the transpose of the cofactor matrix, hence polynomial in the entries of the block, hence polynomial in the coordinates of $\tilde Q$. In the plane the block is $2\times2$ over the plane and its adjugate is the conjugate element, by the computation $(a e_t+b\tilde{Ζ})(a e_t-b\tilde{Ζ})=(a^{2}-b^{2})e_t$ of the previous section.

**Remark (three orders again, and now they differ by more than a factor).** The order of the operator is $m$; the degree of the block determinant is $8m$ in the real coordinates; and the order of the pole is neither. In the plane the pole order is the order of the zero of $N$ minus the order of the zero of the adjugate at the same point, and both numbers are read from the two scalar factors: **the pole order on an ideal is the order of the vanishing of that ideal's scalar.** If $\sigma_+$ vanishes to order $j$ at $\omega_0$ and $\sigma_-$ does not vanish there, the component on $\Pi_+\mathbb{B}$ has a pole of order $j$ and the component on $\Pi_-\mathbb{B}$ is regular; the pole is an object of one ideal at a time.

**Corollary (the order of the pole).** Let $\omega_0$ be a point where $N(\Sigma(\omega_0))=0$, let $j$ be the order of vanishing of $N(\Sigma(\cdot))$ at $\omega_0$, and let $j'$ be the order of vanishing of $\operatorname{ad}\Sigma(\cdot)$ there. Then $\Sigma^{-1}$ has a pole of order $j-j'$ at $\omega_0$ when $j>j'$, and no pole when $j\le j'$.

*Proof.* A quotient of two plane-valued holomorphic functions with a denominator of finite order is expanded by the orders of its numerator and denominator, the plane being commutative.

**Remark (why the block determinant misleads in the plane).** In the plane $\det L_\Sigma=\lvert N\rvert^{4}=\lvert\sigma_+\sigma_-\rvert^{4}$, whose order at a simple zero of one scalar is $4$; the pole order is $1$. **The determinant of the regular representation counts the complex dimension of the algebra and the modulus, and neither number is the pole order.** A reader who reads the pole order off $\det L_\Sigma$ is wrong by a factor of four in the plane, and the factor is not a normalisation.

### The Residue Formula

**Theorem (the residue at a simple null point).** Let $\omega_0$ be a point where $N(\Sigma(\omega_0))=0$, suppose that $N(\Sigma(\cdot))$ has a simple zero there, and suppose that $\operatorname{ad}\Sigma(\omega_0)\ne0$. Then $\Sigma^{-1}$ has a simple pole at $\omega_0$, and its residue is

$$
\operatorname{Res}_{\omega=\omega_0}\Sigma^{-1}=\frac{\operatorname{ad}\Sigma(\omega_0)}{\dfrac{d}{d\omega}N\bigl(\Sigma(\omega)\bigr)\Big|_{\omega_0}} .
$$

*Proof.* Write the denominator as $c\,h+O(h^{2})$ with $h=\omega-\omega_0$ and $c\ne0$, and the numerator as $\operatorname{ad}\Sigma(\omega_0)+O(h)$; the quotient is $\operatorname{ad}\Sigma(\omega_0)/(ch)+O(1)$, and the coefficient of $h^{-1}$ is the displayed quotient.

**Remark (the residue is itself a null element).** At a simple null point the residue is a nonzero multiple of $\operatorname{ad}\Sigma(\omega_0)$, and $N(\operatorname{ad}\Sigma)=N(\Sigma)$ because the adjugate in the plane is the conjugate and conjugation preserves the norm; so the residue has norm zero. **The residue of the reciprocal at a null point lies on the null cone**, and this is the structural reason why the residue cannot be inverted and why it does not behave like a scalar coefficient. In Peirce coordinates the reason is visible: the residue is a multiple of the idempotent of the scalar that vanishes, and every idempotent of the pair is null.

**Remark (the two kinds of simple null point).** The theorem needs only that $N$ vanish simply. If $\Sigma(\omega_0)=0$ as well, the point is of the **first kind** and the element itself vanishes; if $\Sigma(\omega_0)\ne0$ and only the norm vanishes, it is of the **second kind**. In the plane the second kind is generic, because the vanishing of the element is two complex conditions on the coefficients and the vanishing of the norm is one; and the two kinds produce different residues.

### One Worked Kernel

**Example (a first-order symbol with two null points, one per ideal).** Let $\varepsilon>0$ and let

$$
\Sigma(\omega)=(1+i\varepsilon)e_t-2\pi\omega\tilde{Ζ},
$$

a symbol of order one in one frequency variable, with values in the plane of $e_t$ and $\tilde{Ζ}$. Its Peirce scalars are $\sigma_\pm(\omega)=(1+i\varepsilon)\mp2\pi\omega$, so the norm is $N(\Sigma(\omega))=(1+i\varepsilon)^{2}-4\pi^{2}\omega^{2}$, whose zeros are $\omega_0=(1+i\varepsilon)/(2\pi)$ and $\omega_1=-(1+i\varepsilon)/(2\pi)$, one in each half-plane. The adjugate is $\operatorname{ad}\Sigma=(1+i\varepsilon)e_t+2\pi\omega\tilde{Ζ}$, which is a nonzero null element at both zeros and in particular does not vanish there. So the reciprocal has two simple poles, **one per ideal**: $\sigma_+$ vanishes at $\omega_0$, which is the pole of the component on $\Pi_+\mathbb{B}$, and $\sigma_-$ vanishes at $\omega_1$, which is the pole of the component on $\Pi_-\mathbb{B}$.

**Example (the two residues, computed).** The derivative of the norm at $\omega_0$ is $\sigma_+'(\omega_0)\sigma_-(\omega_0)=-2\pi\cdot2(1+i\varepsilon)=-4\pi(1+i\varepsilon)$, and $\operatorname{ad}\Sigma(\omega_0)=2(1+i\varepsilon)\Pi_+$, so the formula of the theorem gives

$$
\operatorname{Res}_{\omega=\omega_0}\Sigma^{-1}=\frac{\operatorname{ad}\Sigma(\omega_0)}{N'(\omega_0)}=-\frac{1}{4\pi}e_t-\frac{1}{4\pi}\tilde{Ζ}=-\frac{\Pi_+}{2\pi},
$$

and the same computation at $\omega_1$, with the two scalars exchanged, gives

$$
\operatorname{Res}_{\omega=\omega_1}\Sigma^{-1}=+\frac{1}{4\pi}e_t-\frac{1}{4\pi}\tilde{Ζ}=+\frac{\Pi_-}{2\pi}.
$$

At $\varepsilon=0.7$ the two coefficients are $\mp0.1592$, and a numerical contour integral over a small circle about each zero reproduces the corresponding residue to six figures. **The two computations agree because the formula is the adjugate over the derivative of the norm, and each residue lives on the ideal whose scalar vanishes.**

**Remark (the residue is not the inverse of the derivative of the symbol).** It is tempting to write the residue as $\Sigma'(\omega_0)^{-1}$, by analogy with the scalar case, where a simple zero of the scalar gives $1/\sigma'(\omega_0)$. That formula is false for the element: $\Sigma'(\omega_0)=-2\pi\tilde{Ζ}$ is a unit with inverse $-\tfrac{1}{2\pi}\tilde{Ζ}$, while the residue is the null element $-\Pi_+/(2\pi)$. **The analogy fails because the symbol does not vanish at the pole**; the norm does. What survives is the scalar statement in the ideal that carries the pole, where $1/\sigma_+'(\omega_0)=-1/(2\pi)$ is exactly the scalar coefficient of the residue.

## Residues at a Repeated Null Point

### The Order of the Pole

**Example (a pole of order two, and a norm of order four).** Let $\Sigma(\omega)=(\omega-\omega_0)^{2}e_t$, a symbol of order two in one variable. Then $N(\Sigma(\omega))=(\omega-\omega_0)^{4}$ and $\operatorname{ad}\Sigma(\omega)=(\omega-\omega_0)^{2}e_t$, so the pole order is $4-2=2$ and the reciprocal is $e_t/(\omega-\omega_0)^{2}$.

**Remark (the general ledger of orders).** Three orders meet at a repeated null point and only one of them is the pole order. The order of the operator is $m=2$; the order of the norm is $4$; the order of the pole is $2$. **The pole order is the difference, and the difference is the order of the adjugate**, which is the order to which the numerator of the quotient vanishes. In the general algebra the same ledger holds with the block determinant in place of the norm, and the numbers change but the arithmetic does not.

**Lemma (the expansion at a null point of the first kind).** Let $\Sigma(\omega_0)=0$ and suppose that $\Sigma(\omega_0+h)=h^{k}A+h^{k+1}B+h^{k+2}C+\cdots$ with $A$ a unit and $h$ a complex scalar. Then

$$
\Sigma^{-1}=h^{-k}A^{-1}-h^{-k+1}A^{-1}BA^{-1}+h^{-k+2}\bigl(A^{-1}BA^{-1}BA^{-1}-A^{-1}CA^{-1}\bigr)+\cdots
$$

*Proof.* Factor $\Sigma=h^{k}(A+hB+h^{2}C+\cdots)$ and invert the parenthesis by the geometric series $(A+hB+h^{2}C)^{-1}=A^{-1}-hA^{-1}BA^{-1}+h^{2}(A^{-1}BA^{-1}BA^{-1}-A^{-1}CA^{-1})+\cdots$, which is legitimate because $h$ is central and $A$ is invertible; multiply by $h^{-k}$.

**Remark (why $h$ must be central, and why it is).** The expansion uses the commutation of $h$ with the coefficients, and it is available because $h$ is a complex scalar: the analytic continuation is in the frequency variable, which is a complex number, and not in the algebra, which is not commutative. **The continuation in the frequency is legitimate and the continuation in the algebra is not**, and every formula in this article respects the distinction.

### The Expansion

**Corollary (the residues at orders one, two and three).** With the notation of the lemma, the residue of $\Sigma^{-1}$ at $\omega_0$ is

$$
A^{-1}\ \ (k=1),\qquad -A^{-1}BA^{-1}\ \ (k=2),\qquad A^{-1}BA^{-1}BA^{-1}-A^{-1}CA^{-1}\ \ (k=3).
$$

*Proof.* Read off the expansion: the residue is the coefficient of $h^{-1}$, which is the coefficient of $h^{k-1}$ in the inverted parenthesis.

**Remark (the shape of the answer, and the reason it is a sum of words).** The residue at a null point of order $k$ is a finite sum of words of length at most $k$ in the inverse of the leading term and the higher coefficients, with alternating signs. **It is not a scalar multiple of anything and it is not a derivative of anything**: the non-commutativity is what makes it a sum of words rather than a quotient, and the sum is the correct generalisation of the scalar derivative formula.

**Proposition (the growth at a repeated pole).** Let $\delta=\lvert\operatorname{Im}\omega_0\rvert$ and let $k$ be the order of the pole. Then the contribution of $\omega_0$ to the kernel is bounded by $C(1+\lvert t\rvert)^{k-1}e^{-2\pi\delta\lvert t\rvert}$ on the side of the axis where the contour closes, and it vanishes on the other side.

*Proof.* Close the contour in the half-plane into which the exponential decays. The integrand is $\exp(2\pi i\omega t)$ times a function with a pole of order $k$ at $\omega_0$, whose residue is a derivative of order $k-1$ of the exponential, hence a polynomial in $t$ of degree $k-1$ times $\exp(2\pi i\omega_0t)$; the modulus of the exponential is $e^{-2\pi\delta\lvert t\rvert}$ on that side, and the arc contributes nothing by the decay.

**Remark (growth and decay are one sentence).** A repeated pole gives a polynomial factor and the distance gives the exponential: **the kernel of a rational symbol never exceeds a power of $\lvert t\rvert$ times $e^{-2\pi\delta\lvert t\rvert}$**, and on the side where the contour does not close it is zero. The growth rate is a decay rate in disguise, and the type is the number $\tau=2\pi\delta$.

### Cancellation and the Apparent Order

**Remark (the adjugate removes half of the null set).** In the worked example the norm vanished at two points and the reciprocal had one pole, because the adjugate vanished at the other one. **The null set of the norm is twice the pole set of the reciprocal in the plane**, and the doubling is exact: the norm is $\sigma\sigma^{*}$ and the adjugate is, up to the plane's conjugation, the factor $\sigma^{*}$, so a zero of $\sigma^{*}$ cancels in the quotient.

**Remark (the same cancellation at a higher order).** The example $\Sigma=(\omega-\omega_0)^{2}e_t$ has norm of order four and pole of order two because the adjugate carries two of the four factors. In general at a null point of the first kind with expansion $h^{k}A+h^{k+1}B+\cdots$, the norm begins at order $2k$ and the adjugate at order $k$; **the pole order is $k$ and the order of the block determinant is $4k$ in $\mathbb{B}$**. Three integers, one pole order.

**Remark (what cancellation does not do).** It does not remove the singularity of the *norm*; it removes the singularity of the *reciprocal*. The set where the symbol is not a unit is a real object, cut by two real equations, and it does not shrink when the reciprocal is simplified. **The pole set of the kernel and the frequency set of the equation are different sets**, the first being the set where the reciprocal is singular as an analytic object after cancellation, the second being the set where the symbol is not a unit.

## Exponential Type and the Tail

### The Type of the Transformed Object

**Theorem (the easy direction of Paley–Wiener, proved).** Let $f:\mathbb{R}\to\mathbb{B}$ be supported in $[-R,R]$ and integrable. Then its transform $F(\omega)=\int\exp(-2\pi i\tilde{Ζ}\omega t)f(t)\,dt$ extends to an entire function of $\omega\in\mathbb{C}$ with the bound

$$
\lVert F(\omega)\rVert\le\lVert f\rVert_{1}e^{2\pi R\lvert\operatorname{Im}\omega\rvert} .
$$

*Proof.* For $\omega=u+iv$ the kernel is $\exp(-2\pi i\tilde{Ζ}ut)\exp(2\pi\tilde{Ζ}vt)$, since the two exponents commute; the first factor is a rotation in the plane of $e_t$ and $\tilde{Ζ}$, and the second has modulus at most $e^{2\pi vt}$ because $\lVert\tilde{Ζ}\rVert=1$ for a pure root of $1$; so the modulus is at most $e^{2\pi v t}$, which is at most $e^{2\pi R\lvert v\rvert}$ on the support. The integrand is entire in $\omega$ for each $t$ and dominated by an integrable function on compacts, so the integral is entire by dominated convergence, and the bound follows.

**Remark (the converse, quoted and not proved).** The converse — that an entire function of exponential type $\tau$ whose restriction to the real axis is of integrable product with itself is the transform of a function supported in $[-\tau/(2\pi),\tau/(2\pi)]$ — is the Paley–Wiener theorem, quoted from *The Inverse Fourier Transform of a Symbol* where it is stated with its hypotheses for $A_{\mathbb{C}}$-valued functions. **The type is $\tau=2\pi R$ and the support radius is $\tau/(2\pi)$**, and the factor $2\pi$ is the one of the exponent.

**Remark (what the type of the transform says about the kernel).** The type of $F$ is read from the support of $f$ and the type of $\kappa_\Sigma$ from the distance of the singular set from the real axis. **The two numbers are independent**, and a solution whose kernel has type $\tau$ behaves at large $\lvert x\rvert$ according to $\tau$ and not according to $R$.

### The Rate the Pole Fixes

**Proposition (the tail of the worked kernel, computed).** For the symbol $\Sigma(\omega)=(1+i\varepsilon)e_t-2\pi\omega\tilde{Ζ}$ the kernel is

$$
\kappa_\Sigma(t)=\theta(t)\,e^{-\varepsilon t}\bigl(\sin t-i\cos t\bigr)e_t ,
$$

with $\theta$ the step at the origin: it vanishes for $t<0$ and oscillates with the decaying amplitude $e^{-\varepsilon t}$ for $t>0$.

*Proof.* By the plane lemma and the Peirce form of the kernel the integral splits into one scalar integral on each ideal, $\kappa=\Pi_+J_++\Pi_-J_-$ with $J_+=\int\exp(2\pi i\omega t)\sigma_+(\omega)^{-1}\,d\omega$ and $J_-=\int\exp(-2\pi i\omega t)\sigma_-(\omega)^{-1}\,d\omega$. For $J_+$ the pole $\omega_0$ lies above the real axis and the exponential decays above, so for $t>0$ the contour closes upward and $J_+=2\pi i\exp(2\pi i\omega_0t)/(-2\pi)=-i\exp(it-\varepsilon t)$, while for $t<0$ it closes below, where there is no pole, and $J_+=0$. For $J_-$ the pole $\omega_1$ lies below and the exponential decays below; the substitution $\omega\mapsto-\omega$ turns $J_-$ into $J_+$ exactly, so $J_-=J_+$. Hence $\kappa=J_+(\Pi_++\Pi_-)=\theta(t)(-i)\exp(it-\varepsilon t)e_t$, and $-i\exp(it)=\sin t-i\cos t$ gives the display.

**Remark (the two numbers, and how they meet).** The poles sit at distance $\delta=\varepsilon/(2\pi)$ from the real axis, and the decay rate of the kernel is $\varepsilon=2\pi\delta$. **The distance and the rate are the same number in two units**, and the factor between them is the $2\pi$ of the exponent. A pole on the real axis, $\delta=0$, gives a kernel that does not decay at all: the worked example with $\varepsilon=0$ has the principal value $-\tfrac{i}{2}\operatorname{sgn}(t)\exp(it)e_t$, a step times an oscillation, and the indentation replaces it by the one-sided piece of the same size.

**Remark (why the kernel is one-sided, and when it is not).** Each ideal carries one pole, and each integral closes in the half-plane where its own exponential decays; the two contributions happen to be equal here, so their sum is a single one-sided piece on $t>0$. A symbol whose two poles lie in the same half-plane still produces one piece per ideal, but the two pieces then act on that common side with two different rates, and a symbol whose poles lie in opposite half-planes produces one piece on each side. **The side on which a pole acts is decided by the sign of its imaginary part relative to its own ideal**, so in the biquaternion case there are two such decisions and not one.

### The Tail of a Solution

**Proposition (the bound on a solution).** Let $f$ be integrable and supported in a ball of radius $R$, and let $\kappa$ be a kernel bounded by $C(1+\lvert t\rvert)^{k-1}e^{-2\pi\delta\lvert t\rvert}$ on the side where it does not vanish. Then the solution $u=\kappa*f$ obeys

$$
\lvert u(x)\rvert\le C'\lVert f\rVert_{1}\bigl(1+\lvert x\rvert\bigr)^{k-1}e^{-2\pi\delta(\lvert x\rvert-R)} .
$$

*Proof.* For $y$ in the support of $f$, $\lvert x-y\rvert\ge\lvert x\rvert-R$, and the bound is monotone in $\lvert x-y\rvert$ on the side where the kernel lives; integrate the bound against $\lvert f\rvert$.

**Remark (the tail, in one sentence).** **The tail of the solution is the tail of the kernel, shifted by the radius of the data.** A pole at distance $\delta$ from the real axis gives a solution that decays like $e^{-2\pi\delta\lvert x\rvert}$; a pole on the axis gives a solution that is merely bounded, and its dependence on the datum is not localised by any exponential.

**Remark (the case $\delta=0$ is the interesting one, and it is the generic one).** In the biquaternion setting the frequency set is cut by two real equations, so it generically misses the real frequencies entirely and the poles sit at a positive distance; but a symbol can be arranged so that a pole lands exactly on the real axis, and then the kernel is bounded and does not decay. **The generic case is the one with decay and the exceptional case is the one without**, which is the reverse of the scalar situation in one variable, where a real zero is generic for a real symbol.

## Counting in Peirce Coordinates

### The Complete Pair and the Two Null Planes

**Proposition (the complete pair).** The elements $\Pi_+=\tfrac12(e_t+i\vec e_z)$ and $\Pi_-=\tfrac12(e_t-i\vec e_z)$ are idempotents, they satisfy $\Pi_++\Pi_-=e_t$ and $\Pi_+\Pi_-=0$, and the two spaces $\Pi_+\mathbb{B}$ and $\Pi_-\mathbb{B}$ are real four-dimensional linear subspaces of $\mathbb{B}$.

*Proof.* $\Pi_+^{2}=\tfrac14(e_t+2i\vec e_z+i^{2}\vec e_z^{2})=\tfrac14(e_t+2i\vec e_z+e_t)=\Pi_+$, because $\vec e_z^{2}=-e_t$; the conjugate computation gives $\Pi_-$; the sum and the product follow from $\vec e_z$ cancelling. Each space $\Pi_\pm\mathbb{B}$ is the image of left multiplication by $\Pi_\pm$, whose rank is four in the real basis.

**Proposition (both planes lie in the null cone).** For every $\tilde Q\in\mathbb{B}$ the elements $\Pi_+\tilde Q$ and $\Pi_-\tilde Q$ have norm zero. Consequently every element of $\mathbb{B}$ is the sum of two null elements, one from each plane.

*Proof.* Quaternion conjugation sends $\Pi_+$ to $\Pi_-$ and is an antiautomorphism, so $N(\Pi_+\tilde Q)=\Pi_+\tilde Q\,\overline{\Pi_+\tilde Q}=\Pi_+\tilde Q\tilde Q\,\Pi_-=N(\tilde Q)\Pi_+\Pi_-=0$, the last step using that $N(\tilde Q)$ is central. The second sentence is the identity $\tilde Q=\Pi_+\tilde Q+\Pi_-\tilde Q$.

**Remark (why this is the Peirce reading of the cone).** The two planes are not the cone: the cone has real dimension six and the planes have dimension four. **They are the maximal linear families inside it**, the ones of the proposition of *The Biquaternion Fourier Transform: Support and Rank*, and they are exactly the planes on which a symbol can have degenerate norm. The pair $\Pi_\pm$ is therefore the coordinate system in which degeneracy is visible, and that is why the counting below is done in it.

### The Norm as Two Corner Terms

**Proposition (the corner form of the norm).** Write $\tilde Q=S_++S_-$ with $S_\pm=\Pi_\pm\tilde Q$. Then

$$
N(\tilde Q)=S_+\,\overline{S_-}+S_-\,\overline{S_+} ,
$$

a sum of two terms, each of which lies in one corner of the pair.

*Proof.* Expand $(\tilde Q)(\overline{\tilde Q})$ with $\tilde Q=S_++S_-$ and $\overline{\tilde Q}=\overline{S_+}+\overline{S_-}$; the terms $S_+\overline{S_+}$ and $S_-\overline{S_-}$ vanish by the previous proposition, and the two cross terms are the displayed ones.

**Remark (the two equations of the zero set, read in Peirce coordinates).** The zero set is cut by the two real equations $N=0$, and in Peirce coordinates the norm is a sum of two corner terms; **so the two equations are the two corners, and a symbol is null exactly when the two corner sums cancel.** That is the sense in which the counting is done in Peirce coordinates: the count of null points is the count of the points where two corner functions are opposite.

**Remark (what the corner form does not give).** Not a factorisation: the norm is a sum, so a zero of the sum is not a zero of either term. **The Peirce coordinates display the degeneracy without resolving it**, and the resolution is *Biquaternion Fourier Inversion on the Degenerate Set*.

### Counting and the Doubling of the Null Set

**Proposition (the count in the plane).** Let $\Sigma$ take its values in a commutative plane of $\mathbb{B}$ and let its two Peirce scalars be polynomials $\sigma_\pm$ of degree $m$. Then the reciprocal has at most $2m$ poles in the complexified frequency plane, counted with multiplicity, $m$ on each ideal, and exactly $2m$ when the two scalars have no common zero; the null set of the norm has the same count, because $N=\sigma_+\sigma_-$ is their product.

*Proof.* The poles are the zeros of $\sigma_+$ and of $\sigma_-$ by the corollary of §*The Reciprocal as Adjugate over Norm*, and each polynomial of degree $m$ has $m$ zeros counted with multiplicity. A zero of one scalar is a pole of the component on its own ideal even when the other scalar does not vanish, because the adjugate swaps the two ideals and is a unit at such a point. A common zero is a null point of the first kind, where the element itself vanishes; the pole there can be shorter than the sum of the two orders, and the corollary gives the corrected order.

**Remark (the argument principle, quoted for the scalar case).** The count of the zeros of $\sigma$ inside a contour is $\frac{1}{2\pi i}\oint\sigma'/\sigma$, the argument principle, quoted from Ahlfors in its scalar form. **It fails for the algebra case**, and the failure is the one identified in *The Inverse Fourier Transform of a Symbol*: the quotient $\Sigma'/\Sigma$ is not a logarithmic derivative of a commutative object, and its integral is not a winding number.

**Remark (the counting, in the form that survives).** What survives in the algebra case is the counting of the *zeros of the norm* along a complex line, which is the count of a holomorphic function of one variable and is therefore finite and computable in principle; and the count of the *poles*, which is the count of the zeros of the norm minus the zeros of the adjugate. **Two counts, one line, and the difference is the correction the adjugate makes**; the counting in the general case is the counting of a divisor on a hypersurface, and it is open.

## The Obstacle: Codimension Two

### Why No Contour Closes

**Proposition (the singular set in more than one variable).** Let $n\ge2$ and let $\zeta$ be the complexified frequency in $\mathbb{C}^{n}$. The set $\{\zeta:N(\Sigma(\zeta))=0\}$ is, where the gradient of the function does not vanish, a complex hypersurface of complex dimension $n-1$ and real codimension two; it contains no isolated point.

*Proof.* The function $\zeta\mapsto N(\Sigma(\zeta))$ is holomorphic, because $\Sigma$ is a polynomial in the frequency with coefficients in $\mathbb{B}$ and $N$ is a polynomial in those coefficients. One holomorphic equation in $n$ variables defines a hypersurface off the critical set, and a hypersurface of complex dimension $n-1$ has real dimension $2n-2$.

**Remark (the deformation argument, and where it stops).** In one variable the singular set is a discrete set of points in the complex plane, a small circle about a point links it, and the residue theorem applies; that is the content of the two sections on residues, and it is complete. In $n\ge2$ the same deformation produces a set of real codimension two, whose link is a bundle of circles rather than a sphere, and the integral of a form with a simple pole along a hypersurface is not a number attached to a point. **The obstruction is the number of variables and not the algebra.**

**Remark (the dimension count, for $n=4$).** For the four frequency variables of the gradient the singular hypersurface has real dimension six, and the cycle over which its residue is integrated has the same dimension; the link of the hypersurface is a circle bundle over it. **"Real codimension two" is the whole story**: it is what makes the link a circle and what makes the residue a current rather than a value.

### What Replaces the Residue

**Definition (residue current, stated and not used).** Let $f$ be holomorphic on a neighbourhood of the origin of $\mathbb{C}^{n}$ with $f(0)=0$ and $df(0)\ne0$. The **residue current** of a form $\alpha$ with a simple pole along $\{f=0\}$ is defined by a limit of integrals over the tubes $\{\lvert f\rvert=\epsilon\}$ as $\epsilon\to0$, and it is a current of degree one less than $\alpha$, supported on the hypersurface.

**Remark (the two routes, named and not proved).** The two known routes to the kernel in $n\ge2$ are the residue currents of Coleff–Herrera and their analytic continuation by Andersson and Wulcan, and the Leray form integrated over a real cycle that links the hypersurface. **Neither is proved here, and neither is applied here**; the definition is quoted so that the reader knows what object the programme is about.

**Remark (what the residue current would give, if it were computed).** It would give the kernel as an integral over the hypersurface of the residue of $\Sigma^{-1}d\omega_1\wedge\cdots\wedge d\omega_n$ against the exponential, which is the exact analogue of the sum over poles in one variable: the sum becomes an integral over a real six-dimensional set. **The kernel would then be a distribution supported on the projection of the hypersurface**, in the same sense in which the one-variable kernel is supported on a half-line.

### The Singular Point of the Cone

**Remark (the point where the gradient vanishes).** At the origin of $\mathbb{B}$ the gradient of $N$ vanishes and the null cone has a singular point there; the same happens for a symbol whose value at a frequency is zero, since then the hypersurface has a singular point at that frequency. **At such a frequency there is no normal direction and no residue at all**, and the local analysis needs the first non-vanishing jet.

**Remark (the three open points, listed).** The programme has three open points and they are named rather than hidden. First, the kernel as a sum of contributions in $n\ge2$, for which the residue current is the candidate and not the answer. Second, the singular points of the hypersurface, where the gradient of the norm vanishes; the null cone meets this case at its vertex, and a symbol with a zero at a frequency meets it there. Third, the non-commutative case even in one variable: the residue formula of §*The Expansion* holds for any associative algebra with a central parameter, but the global count and the closed form of the kernel need the plane.

**Remark (what is not open).** The one-variable theory in a plane is complete: the reciprocal is an adjugate over a norm, the poles are the zeros of the two Peirce scalars, the residues are the quotients of the theorem, the repeated case is the lemma's expansion, the rate is the distance, the tail is the bound of the proposition. **All of it is proved above.**

## Summary

The kernel of the reciprocal of a biquaternion symbol is an integral of the reciprocal against the kernel of the transform. In one frequency variable, with the symbol taking its values in a commutative plane of the algebra, the reciprocal is an adjugate over a norm, the poles are the zeros of the norm after the cancellation of the adjugate, and the residue at a simple null point is the adjugate at that point divided by the derivative of the norm. The residue is a null element, it is not the inverse of the derivative of the symbol, and the order of the pole is the order of the norm minus the order of the adjugate.

At a repeated null point the reciprocal expands in powers of the local variable with coefficients that are sums of words in the leading term and the higher coefficients, the residue at order $k$ being the coefficient of the first negative power; the kernel then carries a polynomial factor of degree $k-1$. The exponential type of the transformed object is the support radius of the datum, by Paley–Wiener; the rate of the kernel is the distance of the pole from the real axis, in the units of the exponent; and the tail of a solution is the tail of the kernel shifted by the radius of the data.

In Peirce coordinates the algebra splits by a complete pair of idempotents into two real four-dimensional planes, both of which lie in the null cone, so every element is a sum of two null elements; the norm is then a sum of two corner terms, which is how the two real equations of the zero set are read. The count of the poles is the count of the zeros of the two Peirce scalars, one count on each ideal, and the count of the null points is their sum, because the norm is the product of the two scalars and either factor produces a pole on its own ideal.

In two or more frequency variables none of the residue theory extends. The singular set is a complex hypersurface of real codimension two, there is no isolated pole and no partial fraction expansion, and the integral becomes a residue current or a Leray form over a real cycle linking the hypersurface. That is the programme, and the one-variable case proved here is what the programme must reproduce.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, of real dimension $8$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The units, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | The central scalar imaginary |
| $N(\tilde Q)$ | The norm $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, central and complex-valued |
| $\tilde{Ζ}$ | A pure root of $1$, fixed once, $\tilde{Ζ}^{2}=e_t$ |
| $W(t,\omega)$ | The kernel $\exp(-2\pi i\tilde{Ζ}\omega t)$, multiplying on the left |
| $F(\omega)$ | The transform $\int\exp(-2\pi i\tilde{Ζ}\omega t)f(t)\,dt$ |
| $\Sigma(\omega)$ | The eigenvalue of the transform, $\sum_\alpha a_\alpha\prod_k(2\pi i\tilde{Ζ}\omega_k)^{\alpha_k}$ |
| $\omega$, $\omega_0$ | The frequency, and a point at which the symbol is not a unit |
| $n$ | The number of frequency variables |
| $\Omega(P)$ | The frequency set $\{\omega:N(\Sigma(\omega))=0\}$ |
| $\kappa_\Sigma$ | The kernel of the reciprocal, the inverse transform of $\Sigma^{-1}$ |
| $a$, $b$ | The coefficients of $e_t$ and $\tilde{Ζ}$ for a symbol in a commutative plane |
| $\sigma_+$, $\sigma_-$ | The Peirce scalars $a+b$ and $a-b$ of an element of the plane |
| $\operatorname{ad}\Sigma$ | The adjugate of the symbol; $a e_t-b\tilde{Ζ}$ in the plane |
| $h$ | The complex scalar $\omega-\omega_0$ |
| $k$ | The order of the pole of the reciprocal |
| $\delta$ | The distance of a null point from the real frequency axis |
| $\tau$ | The exponential type of the kernel, $\tau=2\pi\delta$ |
| $\theta$ | The step at the origin |
| $\Pi_+$, $\Pi_-$ | The idempotents $\tfrac12(e_t\pm i\vec e_z)$, a complete pair |
| $S_+$, $S_-$ | The halves $\Pi_+\tilde Q$ and $\Pi_-\tilde Q$ |
| $R$ | The support radius of the datum |
| $\varepsilon$ | The shift of the worked example, with poles at distance $\varepsilon/(2\pi)$ |

## Further Reading

- *The Inverse Fourier Transform of a Symbol*, for the same three questions asked of a general real algebra, the adjugate and the three orders, and the programme for $n\ge2$ that this article carries into the biquaternion case.
- *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, for the determinant $\lvert N\rvert^{4}$, the null cone and the classification of the null elements that the adjugate cancels.
- *The Biquaternion Fourier Transform: Support and Rank*, for the frequency set, the rank of the symbol on it, and the maximal linear null families that the Peirce planes instantiate.
- *Biquaternion Continuous Harmonic Analysis*, for the kernel, its closed form, its inverse, and the convergence conditions of the inverse transform.
- *The Three Kernel Placements of the Biquaternion Fourier Transform*, for what changes in the residue when the kernel moves to the right or to both sides; the placement decides the half-plane in which the contour closes.
- *The Biquaternion Fourier Transform and the Two Quadratic Forms*, for the form that polarises the norm used here and the form obtained by differentiating the symbol, the two objects the residue must not confuse.
- *Biquaternion Fourier Inversion on the Degenerate Set*, for the inversion when the symbol is not a unit at every frequency, where the reciprocal has no pole to take a residue at and a generalised inverse replaces it.
