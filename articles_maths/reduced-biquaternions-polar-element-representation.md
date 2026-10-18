# __Reduced Biquaternions Polar Element Representation__

## Introduction

The **polar element representation** writes a reduced biquaternion as a pair of polar complex forms, one for each idempotent factor. For $\breve Q=Q_++jQ_-$ put $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, so that $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$; when $Q_{++}$ and $Q_{--}$ are both non-zero, each is written in polar form, $Q_{++}=\rho_{1}e^{i\theta_{1}}$ and $Q_{--}=\rho_{2}e^{i\theta_{2}}$, and
$$
\breve Q=\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-.
$$
This is the **two-factor reading**: the two factors $\Pi_+,\Pi_-$ of the algebra carry independent complex polar data. The representation is unique once a phase range is fixed, and it fails exactly on the **zero divisors**, where one of the two coordinates vanishes. The algebra is **commutative**, so the polar form multiplies by multiplying the two scales and adding the two phases, and it is **not a division algebra**, so the failure set is non-empty.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $\breve Q=Q_++jQ_-$ with $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$; the idempotent coordinates are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, and the reduced norm is $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=Q_{++}Q_{--}$ of *The Four Products, Their Forms and Their Algebraic Norms*. The element glyph is $\breve Q$, with the breve and without a tilde. The phase range is the half-open interval $(-\pi,\pi]$, the convention of *Conventions in Mathematics* for a complex phase.

**Boundaries.** The idempotent coordinates and the splitting $\mathbb{C}\oplus\mathbb{C}$ are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the reduced norm and its vanishing set are *Norm and Invertibility in the Algebra of the Reduced Biquaternions* and *Zero Divisors of the Algebra of the Reduced Biquaternions*; the complex polar form of a single coordinate is *Complex Polar Element Representation*, and the hyperbolic case of the split-complex companion is *Split-Complex Polar Element Representation*. The other element representations are *Introduction to Reduced Biquaternion Element Representations*, *The Four-Vector Element Representation of the Reduced Biquaternions*, *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions* and *Reduced Biquaternion Other Algebraic Element Representations*. The biquaternion counterpart is *Biquaternions Polar Element Representation*.

## The Reduced Norm and Its Failure Set

**The norm is the product of the two idempotent coordinates, it is multiplicative, and it vanishes exactly on the zero divisors.**

**Theorem (the norm of the reading).** For $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$,
$$
\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--},\qquad \langle \breve Q_{1}\breve Q_{2}\rangle_{\natural}=\langle \breve Q_{1}\rangle_{\natural}\langle \breve Q_{2}\rangle_{\natural},
$$
and $\langle \breve Q\rangle_{\natural}=0$ with $\breve Q\neq0$ exactly when one of $Q_{++},Q_{--}$ is $0$, that is exactly on the two idempotent lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$.

*Proof.* $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_++Q_-)(Q_+-Q_-)=Q_{++}Q_{--}$; the multiplicativity is $\langle \breve Q_{1}\breve Q_{2}\rangle_{\natural}=\langle \breve Q_{1}\rangle_{\natural}\langle \breve Q_{2}\rangle_{\natural}$ of *The Four Products, Their Forms and Their Algebraic Norms*; and a product of two complex numbers vanishes exactly when one of them does, the two sets $Q_{++}=0$ and $Q_{--}=0$ being the two idempotent lines of *Zero Divisors of the Algebra of the Reduced Biquaternions*.

**Corollary (the failure set).** The polar representation is available exactly on the complement of the union of the two lines, that is on the **units**; the failure set is the union $\{Q_{++}=0\}\cup\{Q_{--}=0\}$ of two real planes through the origin, and it is the zero-divisor set. This is the boundary of the representation, and it is why the representation is stated before the unit criterion is used.

*Proof.* The representation uses the inverse of each of $Q_{++}$ and $Q_{--}$ in $\mathbb{C}$, which exists exactly when the number is non-zero; and the vanishing sets are the two lines.

## The Two Factors

**Definition.** Let $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ with $\langle \breve Q\rangle_{\natural}\neq0$. The **polar representation** of $\breve Q$ is
$$
\breve Q=\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-,\qquad
\rho_{1}=\lvert Q_{++}\rvert>0,\quad \rho_{2}=\lvert Q_{--}\rvert>0,\quad \theta_{1},\theta_{2}\in(-\pi,\pi],
$$
in which $\rho_{1},\rho_{2}$ are the **scales** and $\theta_{1},\theta_{2}$ the **phases**. The two-factor reading is the pair of polar complex forms of the two idempotent coordinates.

### The Two-Factor Reading

**Theorem (existence and uniqueness).** Every element with $\langle \breve Q\rangle_{\natural}\neq0$ has exactly one polar representation with $\rho_{i}>0$ and $\theta_{i}\in(-\pi,\pi]$.

*Proof.* Existence is the polar form of each non-zero complex number, $Q_{++}=\rho_{1}e^{i\theta_{1}}$ and $Q_{--}=\rho_{2}e^{i\theta_{2}}$. For uniqueness, suppose $\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-=\rho_{1}'e^{i\theta_{1}'}\Pi_++\rho_{2}'e^{i\theta_{2}'}\Pi_-$; since $\Pi_+,\Pi_-$ are a basis of the complex space, the two coordinates agree, so $\rho_{1}e^{i\theta_{1}}=\rho_{1}'e^{i\theta_{1}'}$ and $\rho_{2}e^{i\theta_{2}}=\rho_{2}'e^{i\theta_{2}'}$; the polar form of a complex number with positive modulus and phase in $(-\pi,\pi]$ is unique, whence $\rho_{i}=\rho_{i}'$ and $\theta_{i}=\theta_{i}'$.

**Corollary (the parameter count).** The representation carries two real scales and two real phases, four real parameters, which is the real dimension of the algebra; the **scale pair** carries the two moduli and the **phase pair** the two angles.

*Proof.* The count is $2+2=4$ real parameters, against the four real coordinates $(q_+,q'_+,q_- ,q'_-)$ of *The Four-Vector Element Representation of the Reduced Biquaternions*.

## The Phase-Range Convention

**The phase pair is taken in $(-\pi,\pi]$, and the convention is what makes the representation unique.**

The complex phase $e^{i\theta}$ has period $2\pi$, so without a range the pair $(\theta_{1},\theta_{2})$ is defined only modulo $(2\pi\mathbb{Z})^{2}$; fixing $\theta_{i}\in(-\pi,\pi]$ removes the ambiguity and gives the uniqueness of §*The Two Factors*. The two exceptional phases are the boundary values: $\theta=\pi$ is identified with the negative real axis and written $+\pi$, never $-\pi$, and $\theta=0$ is the positive real axis. The scales are unambiguous, being positive by definition. The same convention is used for a single complex number in *Complex Polar Element Representation* and for the central phase of every algebra of the family.

**Corollary (the phase is a pair of angles).** The pair of phases $(\theta_{1},\theta_{2})$ is a point of the torus $(-\pi,\pi]^{2}$, and the unit factor of the representation is the element $e^{i\theta_{1}}\Pi_++e^{i\theta_{2}}\Pi_-$, whose two coordinates are the two phases.

*Proof.* Each phase is a point of the circle $(-\pi,\pi]$, so a pair is a point of the two-torus, and the displayed element has coordinates $Q_{++}=e^{i\theta_{1}}$, $Q_{--}=e^{i\theta_{2}}$.

## The Slots of the Family

**The family writes an element as a scale, a central phase, a boost and a rotor; the reduced biquaternions fill the scale and the central phase, each doubly, and have neither a boost nor a rotor of their own.**

The four slots of the family are a positive scale, a central phase $e^{i\theta}$ generated by a definite unit, a boost $e^{j\phi}$ generated by a split unit, and a rotor generated by a non-commutative unit. In $\mathbb{B}_{\mathrm{r}}$ the two factors are complex, so each carries the definite unit $i$ and each has a phase: the **central phase slot is filled twice**, by $\theta_{1}$ and $\theta_{2}$. The scale slot is likewise filled twice, by $\rho_{1}$ and $\rho_{2}$.

**Theorem (the boost is the relative scale).** The hyperbolic one-parameter subgroup $e^{j\phi}=\cosh\phi+\sinh\phi\,j$ of the split unit $j$ has the polar data
$$
e^{j\phi}=\rho_{1}\Pi_++\rho_{2}\Pi_-,\qquad \rho_{1}=e^{\phi},\quad \rho_{2}=e^{-\phi},\quad \theta_{1}=\theta_{2}=0,
$$
so its two phases vanish and its **relative scaling** $\rho_{1}/\rho_{2}=e^{2\phi}$ is the boost parameter. There is **no separate boost slot**: the split unit $j$ is spent on the idempotents, and the boost of the split-complex companion is recovered as the relative scale of the two factors.

*Proof.* $e^{j\phi}$ has coordinates $Q_{++}=e^{j\phi}\big|_{\Pi_+}$ and $Q_{--}=e^{j\phi}\big|_{\Pi_-}$; evaluating $e^{j\phi}=\cosh\phi+\sinh\phi\,j$ on $\Pi_+=\tfrac12(1+j)$ gives $\cosh\phi+\sinh\phi=e^{\phi}$ and on $\Pi_-=\tfrac12(1-j)$ gives $\cosh\phi-\sinh\phi=e^{-\phi}$, since $\cosh\phi\pm\sinh\phi=e^{\pm\phi}$.

**Corollary (no rotor).** There is **no rotor slot**, because the algebra is commutative: every unit factor commutes with every element, and no non-commutative unit is available. The absent slots are the reason the reduced biquaternion polar form is a pair of complex polar forms and not a richer object.

*Proof.* A rotor is a unit element whose multiplication is not the identity on the commutant; the algebra is commutative, so the multiplication by any unit is the identity on the commutant, and the slot is empty.

## Multiplication, Powers and Roots

**The polar form multiplies componentwise, which makes the powers, the roots and the unit group transparent.**

**Theorem (the product in polar form).** For $\breve Q_{1}=\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-$ and $\breve Q_{2}=\sigma_{1}e^{i\varphi_{1}}\Pi_++\sigma_{2}e^{i\varphi_{2}}\Pi_-$ a pair of units,
$$
\breve Q_{1}\breve Q_{2}=(\rho_{1}\sigma_{1})e^{i(\theta_{1}+\varphi_{1})}\Pi_++(\rho_{2}\sigma_{2})e^{i(\theta_{2}+\varphi_{2})}\Pi_-,
$$
the scales multiplying and the phases adding, each in its own factor.

*Proof.* The product is componentwise in the idempotent coordinates, $\breve Q_{1}\breve Q_{2}=(Q_{1++}Q_{2++})\Pi_++(Q_{1--}Q_{2--})\Pi_-$; multiplying the two polar forms of each coordinate multiplies the moduli and adds the phases.

**Corollary (powers and roots).** For a positive integer $n$,
$$
\breve Q^{n}=\rho_{1}^{n}e^{in\theta_{1}}\Pi_++\rho_{2}^{n}e^{in\theta_{2}}\Pi_-,
$$
and the $n$-th roots of a unit are the $n$ choices of the phase of $Q_{++}$ combined with the $n$ choices of the phase of $Q_{--}$, that is $n^{2}$ roots; in particular a generic element has **four square roots**, $Q_{++}$ and $Q_{--}$ each having two, in agreement with *Square Roots of a General Element in the Algebra of the Reduced Biquaternions*. The unit group in polar form is the product of the two circles, $(\theta_{1},\theta_{2})$ on the two-torus with both scales equal to one.

*Proof.* The power is the repeated product of the theorem; the roots of $Q_{++}$ are the $n$ numbers of modulus $\rho_{1}^{1/n}$ with the $n$ phase offsets, and similarly for $Q_{--}$, and the two choices are independent, giving $n^{2}$; for $n=2$ this is four.

**Corollary (the unit group).** The polar form identifies the unit group with
$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong(\mathbb{R}_{>0})^{2}\times(S^{1})^{2},
$$
the two scales and the two phases, the phase pair being the compact part of *Introduction to Reduced Biquaternion Element Representations* and the scale pair its non-compact part.

*Proof.* A unit is an element with $\langle \breve Q\rangle_{\natural}\neq0$, that is with both coordinates non-zero; each coordinate is a non-zero complex number, that is a positive modulus and a phase, and the identification is the display.

## Worked Examples

**A unit.** For $\breve Q=1+j$ one has $Q_{++}=2$ and $Q_{--}=0$, so $\breve Q$ is a zero divisor and has no polar representation; the element is $2\Pi_+$, on the first idempotent line. For $\breve Q=1+2j$ one has $Q_{++}=3$ and $Q_{--}=-1$, so $\langle \breve Q\rangle_{\natural}=-3\neq0$ and the polar data are $\rho_{1}=3$, $\theta_{1}=0$ and $\rho_{2}=1$, $\theta_{2}=\pi$; the representation is $3\Pi_+-1\Pi_-$.

**A hyperbolic unity.** For $\breve Q=e^{j\phi}$ with $\cosh\phi=2$, the data are $\rho_{1}=e^{\phi}=2+\sqrt3$ and $\rho_{2}=e^{-\phi}=2-\sqrt3$, both phases zero, and $\rho_{1}\rho_{2}=1=\langle \breve Q\rangle_{\natural}$, the relative scale being $e^{2\phi}=(2+\sqrt3)^{2}=7+4\sqrt3$.

**A pure phase pair.** For $\breve Q=e^{i\alpha}\Pi_++e^{i\beta}\Pi_-$ the scales are both one and the phases are $\alpha,\beta$; the norm is $\langle \breve Q\rangle_{\natural}=e^{i(\alpha+\beta)}$, and the element is a unit with $\langle \breve Q\rangle_{\natural*}=1$.

**A generic element.** For $\breve Q=Q_++jQ_-$ with $Q_+=3+4i$ and $Q_-=1-i$ one has $Q_{++}=Q_++Q_-=4+3i$ and $Q_{--}=Q_+-Q_-=2+5i$, so $\rho_{1}=5$, $\theta_{1}=\arctan\tfrac34=0.6435$, $\rho_{2}=\sqrt{29}=5.3852$ and $\theta_{2}=\arctan\tfrac52=1.1903$; the norm is $\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}=(4+3i)(2+5i)=8+20i+6i+15i^{2}=-7+26i$, a complex number of modulus $\sqrt{49+676}=\sqrt{725}=26.9258$, consistent with $\lvert \langle \breve Q\rangle_{\natural}\rvert=\rho_{1}\rho_{2}=5\sqrt{29}=26.9258$.

## Summary

The polar element representation of a reduced biquaternion writes it as a pair of polar complex forms in the two idempotent coordinates, $\breve Q=\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-$, with the two scales $\rho_{1}=\lvert Q_{++}\rvert$ and $\rho_{2}=\lvert Q_{--}\rvert$ positive and the two phases in $(-\pi,\pi]$. The representation exists exactly for the elements with $\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}\neq0$, that is for the **units**; its **failure set is the union of the two idempotent lines**, the zero divisors, where one coordinate vanishes. The representation is unique under the phase-range convention, and it carries four real parameters, the scale pair and the phase pair. Of the four slots of the family it fills the **scale** and the **central phase**, each twice, and has neither a **boost** — the split unit $j$ giving only the relative scale $e^{2\phi}$ of the two factors — nor a **rotor**, the algebra being **commutative**. The polar form multiplies componentwise, so powers raise the scales and multiply the phases, the $n$-th roots number $n^{2}$, the square roots number four, and the unit group is $(\mathbb{R}_{>0})^{2}\times(S^{1})^{2}$; the multiplication **has zero divisors** and is **not a division algebra**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ | the idempotent coordinates |
| $\rho_{1},\rho_{2}$ | the two scales, $\lvert Q_{++}\rvert$ and $\lvert Q_{--}\rvert$ |
| $\theta_{1},\theta_{2}$ | the two phases, in $(-\pi,\pi]$ |
| $\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-$ | the polar representation |
| $e^{j\phi}$ | the hyperbolic subgroup, phases zero and relative scale $e^{2\phi}$ |
| $\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}$ | the reduced norm, whose non-vanishing is the existence condition |

## Further Reading

- *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the idempotent coordinates.
- *Norm and Invertibility in the Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the reduced norm and the unit criterion.
- *Zero Divisors of the Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the two idempotent lines.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`), for the polar form of each coordinate.
- *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the hyperbolic companion whose boost becomes the relative scale.
- *Square Roots of a General Element in the Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the four square roots.
