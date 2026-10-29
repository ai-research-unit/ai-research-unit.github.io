# __Relations between the Quaternion Norm and Spectral Regularity and Degeneracy__

## Introduction

Two quadratic conditions single out the spectral behaviour of a quaternion. The first is the quaternion norm $|\tilde q|^2=\tilde q\tilde q^{\natural}=q_t^2+|\vec q|^2$, which is multiplicative and positive definite. The second is the squared length $|\vec q|^2$ of the vector part, which is the discriminant of the eigenvalue problem. This article compares the two forms, proves that they are independent, identifies the cells they cut in $\mathbb H$, and shows that the real axis minus the origin is precisely the set where norm regularity and spectral degeneracy coexist. The origin is the only doubly degenerate point, and the norm-degenerate set is $\{0\}$, which contains no zero divisor.

The algebra is [Quaternion Algebra](quaternion-algebra.html); the norm and invertibility are [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html); the spectral criterion is [Spectral Regularity and Degeneracy in the Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-quaternion-algebra.html); the sectors are [The Three Sectors of the Quaternion Algebra](the-three-sectors-of-the-quaternion-algebra.html); the comparison of the eight algebras is [Comparison of the Algebras](comparison-of-the-algebras.html).

**Notation.** $\tilde q=q_t+\vec q=q_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, $\vec q^2=-|\vec q|^2e_t$, $\tilde q^{\natural}=q_t-\vec q$, $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$, $|\tilde q|=\sqrt{\langle\tilde q\rangle_{\natural}}$, $s=|\vec q|$.

## The Two Quadratic Forms

**Definition.** The **quaternion norm** is $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+s^2$. The **spectral form** is $s^2=|\vec q|^2=q_x^2+q_y^2+q_z^2$. A quaternion is **norm-regular** if $\langle\tilde q\rangle_{\natural}\ne0$ and **norm-degenerate** if $\langle\tilde q\rangle_{\natural}=0$; it is **spectrally regular** if $s^2\ne0$ and **spectrally degenerate** if $s^2=0$.

**Theorem (the two radicals).** The norm is positive definite of rank four, with radical $\{0\}$:
$$\langle\tilde q\rangle_{\natural}=0\iff\tilde q=0.$$
The spectral form is positive semidefinite of rank three, with radical the real axis:
$$s^2=0\iff\tilde q\in\mathbb R.$$
Hence $\tilde q$ is norm-regular exactly when $\tilde q\ne0$, and spectrally regular exactly when $\tilde q\notin\mathbb R$.

*Proof.* Both forms are sums of squares of real coordinates. The norm is the sum of all four squares, so it vanishes only when all four coordinates vanish. The spectral form is the sum of the three vector squares, so it vanishes exactly when the vector part vanishes, that is, when $\tilde q=q_t\in\mathbb R$.

**Theorem (the inequality).** For every $\tilde q$,
$$|\tilde q|^2=q_t^2+s^2\ge s^2\ge0,$$
with equality $|\tilde q|^2=s^2$ exactly on the imaginary axis $q_t=0$. Both forms vanish together only at the origin.

*Proof.* $q_t^2\ge0$ and $s^2\ge0$; the first inequality is equality exactly when $q_t=0$. The last assertion is the two radicals: $\{0\}\cap\mathbb R=\{0\}$.

**Proposition (multiplicativity).** The norm is multiplicative and conjugation-invariant:
$$|\tilde q_1\tilde q_2|^2=|\tilde q_1|^2|\tilde q_2|^2,\qquad |\tilde q^{\natural}|^2=|\tilde q|^2.$$
The spectral form is conjugation-invariant but not multiplicative: $\vec e_x\vec e_x=-e_t$ gives $s^2(\vec e_x)s^2(\vec e_x)=1$ while $s^2(-e_t)=0$.

*Proof.* The norm identity is the multiplicativity of the quaternion norm; the conjugation identity is immediate from $q_t^2+s^2$. The counterexample computes both sides.

**Corollary (the one-way implication).** Spectral regularity implies norm regularity. Norm degeneracy implies spectral degeneracy. The converses fail.

*Proof.* $s^2>0$ gives $q_t^2+s^2>0$; $|\tilde q|^2=0$ gives $\tilde q=0\in\mathbb R$. The converses fail at $\tilde q=1$ and at $\tilde q=0$ respectively.

## Independence

**Theorem (the forms are independent).** The two quadratic forms are not proportional, and neither determines the other.

*Proof.* If $|\tilde q|^2=c\,s^2$ for every $\tilde q$, evaluation at $\tilde q=1$ gives $1=0$, impossible. The forms are independent: $\tilde q=1$ and $\tilde q=2$ have $s^2=0$ but norms $1$ and $4$, so $s^2$ does not determine the norm; $\tilde q=2$ and $\tilde q=\sqrt3\,e_t+\vec e_x$ both have norm $4$ but $s^2=0$ and $1$, so the norm does not determine $s^2$.

**Corollary (the zero loci are nested, not equal).** The norm-degenerate set is $\{0\}$, the spectral-degenerate set is $\mathbb R$, and
$$\{0\}\subsetneq\mathbb R.$$
The only implication between the two degeneracies is norm degeneracy $\Rightarrow$ spectral degeneracy; the reverse fails on $\mathbb R^\times$.

**Remark.** The forms are independent because the same norm can carry different spectral behaviour and vice versa. The predicates are not symmetric: the norm's radical lies in the spectral radical, and this one-way dependence is the inequality $q_t^2+s^2\ge s^2$.

## The Real Axis Minus the Origin

**Theorem.** The set
$$\Sigma_{10}=\{\tilde q:|\tilde q|^2\ne0,\ s^2=0\}=\mathbb R^\times$$
consists exactly of the nonzero real quaternions. Every element is norm-regular and spectrally degenerate. It is a one-dimensional subgroup of $\mathbb H^\times$, central in $\mathbb H$, with two connected components $\mathbb R_{>0}$ and $\mathbb R_{<0}$.

*Proof.* $s^2=0$ gives $\tilde q=q_t$; norm regularity gives $q_t\ne0$. The inverse of $q_t$ is $q_t^{-1}$, and the set is closed under multiplication; it is central because real scalars commute with every quaternion. The two signs give the two components.

**Theorem (the operator on $\Sigma_{10}$).** For $\tilde q=q_t\ne0$, $L_{\tilde q}=q_t\,\mathrm{id}$, the spectrum is $\{q_t\}$, the eigenspace is all of $\mathbb H_{\mathbb C}$, and the minimal polynomial is $\lambda-q_t$. The element is semisimple, and its spectrum is a single nonzero real point.

*Proof.* The matrix is scalar and $q_t\ne0$; the minimal polynomial is linear and squarefree.

**Remark (the only coexistence).** $\Sigma_{10}$ is the only cell in which a quaternion is norm-regular and spectrally degenerate. Its elements are units, so spectral degeneracy here is neither non-invertibility nor defect; it is the collapse of the two eigenvalues onto the real axis. The comparison with the split and biquaternion algebras, where norm-regular spectrally degenerate elements can be defective, is in [Spectral Regularity and Degeneracy in the Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-quaternion-algebra.html).

## The Origin

**Theorem.** The set
$$\Sigma_{00}=\{\tilde q:|\tilde q|^2=0,\ s^2=0\}=\{0\}$$
is the unique doubly degenerate point. The origin is the only non-unit of $\mathbb H$, the only element of the norm-degenerate set, and the only element whose spectrum is $\{0\}$ with $L_0=0$.

*Proof.* Norm degeneracy gives $\tilde q=0$; the origin is real, hence spectrally degenerate. The spectrum of $L_0$ is $\{0\}$, the characteristic polynomial is $\lambda^4$, and the minimal polynomial is $\lambda$.

**Proposition.** The origin is semisimple: $\mathbb R[0]=\mathbb R$ is a field, and the minimal polynomial $\lambda$ is squarefree. It lies in the closure of both $\Sigma_{11}$ and $\Sigma_{10}$.

*Proof.* The algebra is $\mathbb R$; every neighborhood of $0$ contains non-real quaternions and nonzero real quaternions.

**Remark (no cone).** The doubly degenerate set is a point, not a cone. In the split-quaternion and biquaternion algebras the corresponding set is a cone with nonzero points; here the positive definiteness of both forms collapses it to the origin.

## The Norm-Degenerate Set

**Theorem.** The norm-degenerate set is $\{0\}$. It contains no zero divisor, and $\mathbb H$ has no zero divisor: if $\tilde q_1\tilde q_2=0$, then $\tilde q_1=0$ or $\tilde q_2=0$.

*Proof.* $|\tilde q_1\tilde q_2|^2=|\tilde q_1|^2|\tilde q_2|^2$; if the product is zero, one factor has norm zero, hence is zero. The zero element is excluded from the definition of a zero divisor, so $\{0\}$ contains none.

**Corollary.** Every nonzero quaternion is a unit, and the unit group is $\mathbb H^\times=\mathbb H\setminus\{0\}$.

**Remark (the name).** "Norm-degenerate" does not mean "zero divisor": the only norm-degenerate element is the zero, and the zero is not a zero divisor. The norm-degenerate set is the smallest possible, a single point.

## The Place among the Eight Algebras

The eight algebras are $\mathbb R$, $\mathbb C$, $\mathbb D$, $\mathbb D'$, $\mathbb H$, $\mathbb H_{\mathrm{s}}$, $\mathbb B$ and $\mathbb H_{\mathbb D}$. The table records the two conditions; for $\mathbb H_{\mathbb D}$ the norm is split-complex valued and the spectral column is read on the two quaternion factors.

| algebra | norm | norm-degenerate | spectrally degenerate | $\Sigma_{01}$ |
|---|---|---|---|---|
| $\mathbb R$ | $a^2$ | $\{0\}$ | all | $\varnothing$ |
| $\mathbb C$ | $a^2+b^2$ | $\{0\}$ | real axis | $\varnothing$ |
| $\mathbb D$ | $a^2-b^2$ | $a=\pm b$ | real axis | nonempty |
| $\mathbb D'$ | $a^2$ | imaginary axis | all | $\varnothing$ |
| $\mathbb H$ | $q_t^2+q_x^2+q_y^2+q_z^2$ | $\{0\}$ | real axis | $\varnothing$ |
| $\mathbb H_{\mathrm{s}}$ | $q_t^2+q_x^2-q_y^2-q_z^2$ | null cone | isotropic cone of $\vec q$ | nonempty |
| $\mathbb B$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ (complex) | null cone | $Q_x^2+Q_y^2+Q_z^2=0$ | nonempty |
| $\mathbb H_{\mathbb D}$ | split-complex valued, anisotropic | $\{0\}$ | read on the factors | — |

**Theorem (the place of $\mathbb H$).** Among the eight, $\mathbb H$ is the only noncommutative division algebra, the only one whose norm is positive definite and whose spectral form has rank three. It is one of the four rows with $\Sigma_{01}=\varnothing$, the others being $\mathbb R$, $\mathbb C$ and $\mathbb D'$. The three rows with $\Sigma_{01}\ne\varnothing$ are $\mathbb D$, $\mathbb H_{\mathrm{s}}$ and $\mathbb B$.

*Proof.* The norms and signatures are those of [Comparison of Norms and Invertibility](comparison-of-norms-and-invertibility.html). The emptiness of $\Sigma_{01}$ in $\mathbb H$ is the implication of the previous section; in $\mathbb R$, $\mathbb C$ and $\mathbb D'$ it follows from the table. The nonemptiness in $\mathbb D$ is witnessed by $1+j$, with norm $0$ and eigenvalues $2,0$; in $\mathbb H_{\mathrm{s}}$ by $1+\vec e_y$, with norm $0$ and $\vec q^2=+1$; in $\mathbb B$ by $1+i\vec e_x$, with norm $0$ and $B^2=-1$.

## The Chain of Invariants

**Theorem (the chain).** The following implication chain holds, and its middle implication is strict:
$$\tilde q=0\iff|\tilde q|^2=0\implies s^2=0\iff\tilde q\in\mathbb R.$$
The failure of the reverse implication is exactly $\Sigma_{10}=\mathbb R^\times$.

*Proof.* The first equivalence is positive definiteness; the implication is $s^2\le|\tilde q|^2$; the second equivalence is the radical of the spectral form. It fails at $\tilde q=1$.

**The invariants.** The norm $|\tilde q|^2$ decides invertibility; the spectral form $s^2$ decides the separation of the eigenvalues; the scalar part $q_t$ locates the centre of the spectrum and separates the positive and negative components of $\Sigma_{10}$. The pair $(q_t,s)$ gives the spectrum $q_t\pm is$ and the polar angle.

**Corollary (the four sectors).** The truth values of the two conditions partition $\mathbb H$ into
$$\Sigma_{11}=\mathbb H\setminus\mathbb R,\qquad \Sigma_{10}=\mathbb R^\times,\qquad \Sigma_{01}=\varnothing,\qquad \Sigma_{00}=\{0\}.$$
The partition, its dimensions and its closures are the subject of [The Three Sectors of the Quaternion Algebra](the-three-sectors-of-the-quaternion-algebra.html).

## Summary

The quaternion norm $q_t^2+s^2$ and the spectral form $s^2$ are independent quadratic forms: neither is proportional to the other, and neither determines the other. The norm is positive definite with radical $\{0\}$; the spectral form is positive semidefinite of rank three with radical the real axis. Hence the norm-degenerate set is $\{0\}$ and the spectral-degenerate set is $\mathbb R$, with $\{0\}\subsetneq\mathbb R$. The real axis minus the origin is exactly the set of norm-regular, spectrally degenerate elements; these are the nonzero real scalars, all units and all semisimple. The origin is the only doubly degenerate point, the only non-unit and the only element of the norm-degenerate set, which contains no zero divisor.

Among the eight, $\mathbb H$ is the only noncommutative division algebra with both forms positive definite. The cell $\Sigma_{01}$ is empty for $\mathbb R,\mathbb C,\mathbb D',\mathbb H$ and nonempty for $\mathbb D,\mathbb H_{\mathrm{s}},\mathbb B$. The chain
$$\tilde q=0\iff|\tilde q|^2=0\implies s^2=0\iff\tilde q\in\mathbb R$$
has one strict implication, whose failure is $\mathbb R^\times$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$ | the quaternion norm |
| $|\tilde q|=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus |
| $s=|\vec q|$ | the length of the vector part |
| $s^2=|\vec q|^2$ | the spectral form |
| $\Sigma_{ij}$ | the cell with norm truth value $i$ and spectral truth value $j$ |
| $\Sigma_{10}=\mathbb R^\times$ | norm-regular, spectrally degenerate |
| $\Sigma_{00}=\{0\}$ | doubly degenerate |
| $\Sigma_{01}=\varnothing$ | norm-degenerate, spectrally regular |
| $\mathbb D,\mathbb D'$ | split-complex and dual numbers |
| $\mathbb H_{\mathrm{s}},\mathbb B,\mathbb H_{\mathbb D}$ | split-quaternion, biquaternion, split-biquaternion algebras |

## Further Reading

- [Quaternion Algebra](quaternion-algebra.html), for the multiplication and the scalar–vector decomposition.
- [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html), for the norm, its multiplicativity and the unit group.
- [Spectral Regularity and Degeneracy in the Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-quaternion-algebra.html), for the spectral criterion and the minimal polynomial.
- [The Three Sectors of the Quaternion Algebra](the-three-sectors-of-the-quaternion-algebra.html), for the partition, dimensions and closures.
- [Comparison of Norms and Invertibility](comparison-of-norms-and-invertibility.html), for the norms and signatures of the eight algebras.
- [Comparison of the Algebras](comparison-of-the-algebras.html), for the master table of the eight.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the biquaternion norm, its null cone and the four sectors.
- [Split-Quaternion Norm and Invertibility](split-quaternion-norm-and-invertibility.html), for the indefinite norm and its null cone.
