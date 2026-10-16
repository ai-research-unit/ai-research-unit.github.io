# __Reduced Biquaternions Polar Element Representation__

## Introduction

The **polar element representation** writes a reduced biquaternion as a pair of polar complex forms, one for each idempotent factor. For $T=A+Bj$ put $q_1=A+B$ and $q_2=A-B$, so that $T=q_1\Pi_{1}+q_2\Pi_{2}$ with $\Pi_{1,2}=\tfrac12(1\pm j)$; when $q_1$ and $q_2$ are both non-zero, each is written in polar form, $q_1=\rho_{1}e^{i\theta_{1}}$ and $q_2=\rho_{2}e^{i\theta_{2}}$, and
$$
T=\rho_{1}e^{i\theta_{1}}\Pi_{1}+\rho_{2}e^{i\theta_{2}}\Pi_{2}.
$$
This is the **two-factor reading**: the two factors $\Pi_{1},\Pi_{2}$ of the algebra carry independent complex polar data. The representation is unique once a phase range is fixed, and it fails exactly on the **zero divisors**, where one of the two coordinates vanishes. The algebra is **commutative**, so the polar form multiplies by multiplying the two scales and adding the two phases, and it is **not a division algebra**, so the failure set is non-empty.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $T=A+Bj$ with $A=a+ia'$, $B=b+ib'$; the idempotent coordinates are $q_1=A+B$ and $q_2=A-B$, and the reduced norm is $\langle T\rangle_{\natural}=A^{2}-B^{2}=q_1q_2$ of *The Four Products, Their Forms and Their Algebraic Norms*. The element glyph is $T$, without a tilde. The phase range is the half-open interval $(-\pi,\pi]$, the convention of *Conventions in Mathematics* for a complex phase.

**Boundaries.** The idempotent coordinates and the splitting $\mathbb{C}\oplus\mathbb{C}$ are *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the reduced norm and its vanishing set are *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* and *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the complex polar form of a single coordinate is *Complex Polar Element Representation*, and the hyperbolic case of the split-complex companion is *Split-Complex Polar Element Representation*. The other element representations are *Introduction to Reduced Biquaternion Element Representations*, *The Four-Vector Element Representation of the Reduced Biquaternions*, *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions* and *Reduced Biquaternion Other Algebraic Element Representations*. The biquaternion counterpart is *Biquaternions Polar Element Representation*.

## The Reduced Norm and Its Failure Set

**The norm is the product of the two idempotent coordinates, it is multiplicative, and it vanishes exactly on the zero divisors.**

**Theorem (the norm of the reading).** For $T=q_1\Pi_{1}+q_2\Pi_{2}$,
$$
\langle T\rangle_{\natural}=q_1q_2,\qquad \langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural},
$$
and $\langle T\rangle_{\natural}=0$ with $T\neq0$ exactly when one of $q_1,q_2$ is $0$, that is exactly on the two idempotent lines $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$.

*Proof.* $\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B)=q_1q_2$; the multiplicativity is $\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural}$ of *The Four Products, Their Forms and Their Algebraic Norms*; and a product of two complex numbers vanishes exactly when one of them does, the two sets $q_1=0$ and $q_2=0$ being the two idempotent lines of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*.

**Corollary (the failure set).** The polar representation is available exactly on the complement of the union of the two lines, that is on the **units**; the failure set is the union $\{q_1=0\}\cup\{q_2=0\}$ of two real planes through the origin, and it is the zero-divisor set. This is the boundary of the representation, and it is why the representation is stated before the unit criterion is used.

*Proof.* The representation uses the inverse of each of $q_1$ and $q_2$ in $\mathbb{C}$, which exists exactly when the number is non-zero; and the vanishing sets are the two lines.

## The Two Factors

**Definition.** Let $T=q_1\Pi_{1}+q_2\Pi_{2}$ with $\langle T\rangle_{\natural}\neq0$. The **polar representation** of $T$ is
$$
T=\rho_{1}e^{i\theta_{1}}\Pi_{1}+\rho_{2}e^{i\theta_{2}}\Pi_{2},\qquad
\rho_{1}=\lvert q_1\rvert>0,\quad \rho_{2}=\lvert q_2\rvert>0,\quad \theta_{1},\theta_{2}\in(-\pi,\pi],
$$
in which $\rho_{1},\rho_{2}$ are the **scales** and $\theta_{1},\theta_{2}$ the **phases**. The two-factor reading is the pair of polar complex forms of the two idempotent coordinates.

### The Two-Factor Reading

**Theorem (existence and uniqueness).** Every element with $\langle T\rangle_{\natural}\neq0$ has exactly one polar representation with $\rho_{i}>0$ and $\theta_{i}\in(-\pi,\pi]$.

*Proof.* Existence is the polar form of each non-zero complex number, $q_1=\rho_{1}e^{i\theta_{1}}$ and $q_2=\rho_{2}e^{i\theta_{2}}$. For uniqueness, suppose $\rho_{1}e^{i\theta_{1}}\Pi_{1}+\rho_{2}e^{i\theta_{2}}\Pi_{2}=\rho_{1}'e^{i\theta_{1}'}\Pi_{1}+\rho_{2}'e^{i\theta_{2}'}\Pi_{2}$; since $\Pi_{1},\Pi_{2}$ are a basis of the complex space, the two coordinates agree, so $\rho_{1}e^{i\theta_{1}}=\rho_{1}'e^{i\theta_{1}'}$ and $\rho_{2}e^{i\theta_{2}}=\rho_{2}'e^{i\theta_{2}'}$; the polar form of a complex number with positive modulus and phase in $(-\pi,\pi]$ is unique, whence $\rho_{i}=\rho_{i}'$ and $\theta_{i}=\theta_{i}'$.

**Corollary (the parameter count).** The representation carries two real scales and two real phases, four real parameters, which is the real dimension of the algebra; the **scale pair** carries the two moduli and the **phase pair** the two angles.

*Proof.* The count is $2+2=4$ real parameters, against the four real coordinates $(a,a',b,b')$ of *The Four-Vector Element Representation of the Reduced Biquaternions*.

## The Phase-Range Convention

**The phase pair is taken in $(-\pi,\pi]$, and the convention is what makes the representation unique.**

The complex phase $e^{i\theta}$ has period $2\pi$, so without a range the pair $(\theta_{1},\theta_{2})$ is defined only modulo $(2\pi\mathbb{Z})^{2}$; fixing $\theta_{i}\in(-\pi,\pi]$ removes the ambiguity and gives the uniqueness of §*The Two Factors*. The two exceptional phases are the boundary values: $\theta=\pi$ is identified with the negative real axis and written $+\pi$, never $-\pi$, and $\theta=0$ is the positive real axis. The scales are unambiguous, being positive by definition. The same convention is used for a single complex number in *Complex Polar Element Representation* and for the central phase of every algebra of the family.

**Corollary (the phase is a pair of angles).** The pair of phases $(\theta_{1},\theta_{2})$ is a point of the torus $(-\pi,\pi]^{2}$, and the unit factor of the representation is the element $e^{i\theta_{1}}\Pi_{1}+e^{i\theta_{2}}\Pi_{2}$, whose two coordinates are the two phases.

*Proof.* Each phase is a point of the circle $(-\pi,\pi]$, so a pair is a point of the two-torus, and the displayed element has coordinates $q_1=e^{i\theta_{1}}$, $q_2=e^{i\theta_{2}}$.

## The Slots of the Family

**The family writes an element as a scale, a central phase, a boost and a rotor; the reduced biquaternions fill the scale and the central phase, each doubly, and have neither a boost nor a rotor of their own.**

The four slots of the family are a positive scale, a central phase $e^{i\theta}$ generated by a definite unit, a boost $e^{j\phi}$ generated by a split unit, and a rotor generated by a non-commutative unit. In $\mathbb{B}_{\mathrm{r}}$ the two factors are complex, so each carries the definite unit $i$ and each has a phase: the **central phase slot is filled twice**, by $\theta_{1}$ and $\theta_{2}$. The scale slot is likewise filled twice, by $\rho_{1}$ and $\rho_{2}$.

**Theorem (the boost is the relative scale).** The hyperbolic one-parameter subgroup $e^{j\phi}=\cosh\phi+\sinh\phi\,j$ of the split unit $j$ has the polar data
$$
e^{j\phi}=\rho_{1}\Pi_{1}+\rho_{2}\Pi_{2},\qquad \rho_{1}=e^{\phi},\quad \rho_{2}=e^{-\phi},\quad \theta_{1}=\theta_{2}=0,
$$
so its two phases vanish and its **relative scaling** $\rho_{1}/\rho_{2}=e^{2\phi}$ is the boost parameter. There is **no separate boost slot**: the split unit $j$ is spent on the idempotents, and the boost of the split-complex companion is recovered as the relative scale of the two factors.

*Proof.* $e^{j\phi}$ has coordinates $q_1=e^{j\phi}\big|_{\Pi_{1}}$ and $q_2=e^{j\phi}\big|_{\Pi_{2}}$; evaluating $e^{j\phi}=\cosh\phi+\sinh\phi\,j$ on $\Pi_{1}=\tfrac12(1+j)$ gives $\cosh\phi+\sinh\phi=e^{\phi}$ and on $\Pi_{2}=\tfrac12(1-j)$ gives $\cosh\phi-\sinh\phi=e^{-\phi}$, since $\cosh\phi\pm\sinh\phi=e^{\pm\phi}$.

**Corollary (no rotor).** There is **no rotor slot**, because the algebra is commutative: every unit factor commutes with every element, and no non-commutative unit is available. The absent slots are the reason the reduced biquaternion polar form is a pair of complex polar forms and not a richer object.

*Proof.* A rotor is a unit element whose multiplication is not the identity on the commutant; the algebra is commutative, so the multiplication by any unit is the identity on the commutant, and the slot is empty.

## Multiplication, Powers and Roots

**The polar form multiplies componentwise, which makes the powers, the roots and the unit group transparent.**

**Theorem (the product in polar form).** For $T=\rho_{1}e^{i\theta_{1}}\Pi_{1}+\rho_{2}e^{i\theta_{2}}\Pi_{2}$ and $W=\sigma_{1}e^{i\varphi_{1}}\Pi_{1}+\sigma_{2}e^{i\varphi_{2}}\Pi_{2}$ a pair of units,
$$
TW=(\rho_{1}\sigma_{1})e^{i(\theta_{1}+\varphi_{1})}\Pi_{1}+(\rho_{2}\sigma_{2})e^{i(\theta_{2}+\varphi_{2})}\Pi_{2},
$$
the scales multiplying and the phases adding, each in its own factor.

*Proof.* The product is componentwise in the idempotent coordinates, $TW=(q_1q_2)\Pi_{1}+(q_1'q_2')\Pi_{2}$; multiplying the two polar forms of each coordinate multiplies the moduli and adds the phases.

**Corollary (powers and roots).** For a positive integer $n$,
$$
T^{n}=\rho_{1}^{n}e^{in\theta_{1}}\Pi_{1}+\rho_{2}^{n}e^{in\theta_{2}}\Pi_{2},
$$
and the $n$-th roots of a unit are the $n$ choices of the phase of $q_1$ combined with the $n$ choices of the phase of $q_2$, that is $n^{2}$ roots; in particular a generic element has **four square roots**, $q_1$ and $q_2$ each having two, in agreement with *Square Roots of a General Element in the General Plain Algebra of the Reduced Biquaternions*. The unit group in polar form is the product of the two circles, $(\theta_{1},\theta_{2})$ on the two-torus with both scales equal to one.

*Proof.* The power is the repeated product of the theorem; the roots of $q_1$ are the $n$ numbers of modulus $\rho_{1}^{1/n}$ with the $n$ phase offsets, and similarly for $q_2$, and the two choices are independent, giving $n^{2}$; for $n=2$ this is four.

**Corollary (the unit group).** The polar form identifies the unit group with
$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong(\mathbb{R}_{>0})^{2}\times(S^{1})^{2},
$$
the two scales and the two phases, the phase pair being the compact part of *Introduction to Reduced Biquaternion Element Representations* and the scale pair its non-compact part.

*Proof.* A unit is an element with $\langle T\rangle_{\natural}\neq0$, that is with both coordinates non-zero; each coordinate is a non-zero complex number, that is a positive modulus and a phase, and the identification is the display.

## Worked Examples

**A unit.** For $T=1+j$ one has $q_1=2$ and $q_2=0$, so $T$ is a zero divisor and has no polar representation; the element is $2\Pi_{1}$, on the first idempotent line. For $T=1+2j$ one has $q_1=3$ and $q_2=-1$, so $\langle T\rangle_{\natural}=-3\neq0$ and the polar data are $\rho_{1}=3$, $\theta_{1}=0$ and $\rho_{2}=1$, $\theta_{2}=\pi$; the representation is $3\Pi_{1}-1\Pi_{2}$.

**A hyperbolic unity.** For $T=e^{j\phi}$ with $\cosh\phi=2$, the data are $\rho_{1}=e^{\phi}=2+\sqrt3$ and $\rho_{2}=e^{-\phi}=2-\sqrt3$, both phases zero, and $\rho_{1}\rho_{2}=1=\langle T\rangle_{\natural}$, the relative scale being $e^{2\phi}=(2+\sqrt3)^{2}=7+4\sqrt3$.

**A pure phase pair.** For $T=e^{i\alpha}\Pi_{1}+e^{i\beta}\Pi_{2}$ the scales are both one and the phases are $\alpha,\beta$; the norm is $\langle T\rangle_{\natural}=e^{i(\alpha+\beta)}$, and the element is a unit with \langle T\rangle_{\natural*}=1$.

**A generic element.** For $T=A+Bj$ with $A=3+4i$ and $B=1-i$ one has $q_1=A+B=4+3i$ and $q_2=A-B=2+5i$, so $\rho_{1}=5$, $\theta_{1}=\arctan\tfrac34=0.6435$, $\rho_{2}=\sqrt{29}=5.3852$ and $\theta_{2}=\arctan\tfrac52=1.1903$; the norm is $\langle T\rangle_{\natural}=q_1q_2=(4+3i)(2+5i)=8+20i+6i+15i^{2}=-7+26i$, a complex number of modulus $\sqrt{49+676}=\sqrt{725}=26.9258$, consistent with $\lvert \langle T\rangle_{\natural}\rvert=\rho_{1}\rho_{2}=5\sqrt{29}=26.9258$.

## Summary

The polar element representation of a reduced biquaternion writes it as a pair of polar complex forms in the two idempotent coordinates, $T=\rho_{1}e^{i\theta_{1}}\Pi_{1}+\rho_{2}e^{i\theta_{2}}\Pi_{2}$, with the two scales $\rho_{1}=\lvert A+B\rvert$ and $\rho_{2}=\lvert A-B\rvert$ positive and the two phases in $(-\pi,\pi]$. The representation exists exactly for the elements with $\langle T\rangle_{\natural}=q_1q_2\neq0$, that is for the **units**; its **failure set is the union of the two idempotent lines**, the zero divisors, where one coordinate vanishes. The representation is unique under the phase-range convention, and it carries four real parameters, the scale pair and the phase pair. Of the four slots of the family it fills the **scale** and the **central phase**, each twice, and has neither a **boost** — the split unit $j$ giving only the relative scale $e^{2\phi}$ of the two factors — nor a **rotor**, the algebra being **commutative**. The polar form multiplies componentwise, so powers raise the scales and multiply the phases, the $n$-th roots number $n^{2}$, the square roots number four, and the unit group is $(\mathbb{R}_{>0})^{2}\times(S^{1})^{2}$; the multiplication **has zero divisors** and is **not a division algebra**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $q_1=A+B$, $q_2=A-B$ | the idempotent coordinates |
| $\rho_{1},\rho_{2}$ | the two scales, $\lvert q_1\rvert$ and $\lvert q_2\rvert$ |
| $\theta_{1},\theta_{2}$ | the two phases, in $(-\pi,\pi]$ |
| $\rho_{1}e^{i\theta_{1}}\Pi_{1}+\rho_{2}e^{i\theta_{2}}\Pi_{2}$ | the polar representation |
| $e^{j\phi}$ | the hyperbolic subgroup, phases zero and relative scale $e^{2\phi}$ |
| $\langle T\rangle_{\natural}=q_1q_2$ | the reduced norm, whose non-vanishing is the existence condition |

## Further Reading

- *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the idempotent coordinates.
- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the reduced norm and the unit criterion.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the two idempotent lines.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`), for the polar form of each coordinate.
- *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the hyperbolic companion whose boost becomes the relative scale.
- *Square Roots of a General Element in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the four square roots.
