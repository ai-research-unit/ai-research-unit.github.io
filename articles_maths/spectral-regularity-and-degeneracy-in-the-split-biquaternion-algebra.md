# __Spectral Regularity and Degeneracy in the Split-Biquaternion Algebra__

## Introduction

The split-biquaternion algebra $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{H}\oplus\mathbb{H}$ is a product of two copies of the quaternion division algebra. Its spectrum is therefore not a single quaternionic spectrum but the union of two of them: the spectrum of $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$ is the union of the spectra of the halves $Q_+$ and $Q_-$. This article proves the formula and separates the two spectral cases: **regular**, with simple roots, and **degenerate**, with a repeated root.

The main results are these. The reduced characteristic polynomial is $p_{\tilde Q}=p_+p_-$, with $p_\pm(\lambda)=(\lambda-t_\pm)^2+|\vec q_\pm|^2$. A repeated root occurs exactly when one half is scalar or the half-spectra meet. Every element is semisimple, because each half lies in the division algebra $\mathbb{H}$; there is no defect. The contrast with the biquaternion algebra is sharp: there a complex isotropic vector exists and the spectral cone is defective off the scalar line; here the vector parts are real, their squared norms are sums of squares, and the product of two division algebras removes the defect.

**Conventions.** The split complex unit is $j$, with $j^2=1$, and it is central. The idempotents are $\tilde\Pi_{1,2}=\tfrac12(1\pm j)$. An element is written

$$
\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2,\qquad Q_\pm\in\mathbb{H},
$$

with

$$
Q_\pm=t_\pm+\vec q_\pm,\qquad t_\pm\in\mathbb{R},\qquad
\vec q_\pm=\sum_{k=x,y,z}q_{\pm k}\vec e_k,\qquad
|\vec q_\pm|^2=\sum_{k=x,y,z}q_{\pm k}^2,
$$

and quaternion norm $|Q_\pm|^2=t_\pm^2+|\vec q_\pm|^2$. The split-biquaternion norm is

$$
\langle\tilde Q\rangle_{\natural}=|Q_+|^2\tilde\Pi_1+|Q_-|^2\tilde\Pi_2
=\sum_{\mu=t,x,y,z}Q_\mu^2,
$$

and the reduced norm is $\Delta=|Q_+|^2|Q_-|^2=\langle\tilde Q\rangle_{\natural}\langle\tilde Q\rangle_{\natural}^{*}$. The algebra and idempotents are *[Split-Biquaternion Algebra](split-biquaternion-algebra.html)* and *[Split-Biquaternion Idempotents and Projections](split-biquaternion-idempotents-and-projections.html)*; the norm is *[Split-Biquaternion Norm and Invertibility](split-biquaternion-norm-and-invertibility.html)*; the spectrum is *[Split-Biquaternion Spectral Theory](split-biquaternion-spectral-theory.html)*. The companion articles are *[The Reduced Norm and Spectral Degeneracy in the Split-Biquaternion Algebra](relations-between-the-split-biquaternion-reduced-norm-and-spectral-regularity-and-degeneracy.html)* and *[The Three Sectors of the Split-Biquaternion Algebra](the-three-sectors-of-the-split-biquaternion-algebra.html)*.

## The Spectrum as the Union of the Two Half-Spectra

### The Spectrum of a Quaternion Half

**Definition (spectrum of a half).** For $Q\in\mathbb{H}$, let $L_Q:\mathbb{H}\to\mathbb{H}$ be left multiplication, $L_Q(X)=QX$. The **spectrum** $\sigma(Q)$ is the set of complex eigenvalues of $L_Q$ after complexification.

**Lemma (the spectrum of a quaternion).** Write $Q=t+\vec q$ with $t\in\mathbb{R}$ and $\vec q\in\mathbb{R}^3$. If $\vec q\neq0$, then

$$
\sigma(Q)=\{t+i|\vec q|,\ t-i|\vec q|\},
$$

each value occurring with multiplicity two. If $\vec q=0$, then $\sigma(Q)=\{t\}$, with multiplicity four.

*Proof.* Suppose $\vec q\neq0$ and put $u=\vec q/|\vec q|$. Then $u^2=-1$ and $L_Q=t\,\mathrm{id}+|\vec q|L_u$. Right multiplication $R_u$ is a complex structure commuting with $L_u$, so $\mathbb{H}$ is a two-dimensional complex space and $L_u$ is complex-linear. Since $L_u^2=-\mathrm{id}$ and $\operatorname{tr}L_u=4\,\mathrm{Re}\,u=0$, its eigenvalues are $i$ and $-i$. Hence $L_Q$ has $t\pm i|\vec q|$, each with real multiplicity two. If $\vec q=0$, then $L_Q=t\,\mathrm{id}$ on $\mathbb{R}^4$.

### The Spectrum of the Element

**Definition (the spectrum).** The **spectrum** of $\tilde Q$ is the spectrum of the real operator $L_{\tilde Q}$ on $\mathbb{H}_{\mathbb{D}}$, complexified.

**Theorem (the union formula).** For $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$,

$$
\sigma(\tilde Q)
=\{t_++i|\vec q_+|,\ t_+-i|\vec q_+|\}
\cup
\{t_-+i|\vec q_-|,\ t_--i|\vec q_-|\}.
$$

Each value contributed by a half occurs twice in the characteristic polynomial of $L_{\tilde Q}$; when a half is scalar, its two values coincide and its contribution has multiplicity four.

*Proof.* The idempotents $\tilde\Pi_{1,2}$ are central, so for $X=X_+\tilde\Pi_1+X_-\tilde\Pi_2$ one has

$$
\tilde QX=(Q_+X_+)\tilde\Pi_1+(Q_-X_-)\tilde\Pi_2.
$$

Hence $L_{\tilde Q}$ is the block diagonal operator $\mathrm{diag}(L_{Q_+},L_{Q_-})$ on the two copies of $\mathbb{H}$. The spectrum is the union of the two block spectra, with multiplicities added. The lemma gives the two displayed values and the multiplicities.

**Corollary (the full characteristic polynomial).** Let

$$
p_\pm(\lambda)=(\lambda-t_\pm)^2+|\vec q_\pm|^2.
$$

The characteristic polynomial of $L_{\tilde Q}$ is

$$
\chi_{\tilde Q}(\lambda)=p_+(\lambda)^2p_-(\lambda)^2.
$$

*Proof.* By the lemma, the characteristic polynomial of $L_{Q_\pm}$ is $p_\pm^2$: for a non-scalar half the two roots of $p_\pm$ each occur twice, and for a scalar half $p_\pm=(\lambda-t_\pm)^2$ and its square is $(\lambda-t_\pm)^4$. The block diagonal characteristic polynomial is the product.

### The Reduced Characteristic Polynomial

**Definition (reduced characteristic polynomial).** The **reduced characteristic polynomial** is

$$
p_{\tilde Q}(\lambda)=p_+(\lambda)p_-(\lambda)
=\bigl((\lambda-t_+)^2+|\vec q_+|^2\bigr)\bigl((\lambda-t_-)^2+|\vec q_-|^2\bigr).
$$

It is the monic polynomial with $\chi_{\tilde Q}=p_{\tilde Q}^2$. Its roots are the spectrum values counted once per half.

Each half contributes its reduced polynomial $p_\pm$; the operator $L_{\tilde Q}$ doubles each factor, and $p_{\tilde Q}$ removes the doubling.

### The Criterion for a Repeated Root

**Theorem (repeated roots).** The reduced polynomial $p_{\tilde Q}$ has a repeated root exactly when one of the following holds:

1. $\vec q_+=0$;
2. $\vec q_-=0$;
3. $t_+=t_-$ and $|\vec q_+|=|\vec q_-|$.

*Proof.* The polynomial $p_\pm$ has discriminant $-4|\vec q_\pm|^2$, so it has a double root exactly when $|\vec q_\pm|=0$, which is cases 1 and 2. A root is shared by $p_+$ and $p_-$ exactly when

$$
t_++\varepsilon i|\vec q_+|=t_-+\varepsilon' i|\vec q_-|
$$

for some signs $\varepsilon,\varepsilon'\in\{1,-1\}$. If $\varepsilon=\varepsilon'$, comparison of real and imaginary parts gives $t_+=t_-$ and $|\vec q_+|=|\vec q_-|$, which is case 3. If $\varepsilon=-\varepsilon'$, comparison of imaginary parts gives $|\vec q_+|=-|\vec q_-|$, hence both are zero, which is already contained in cases 1 and 2. Conversely, each of the three conditions produces a double root or a shared root.

**Corollary (spectral regularity).** The element is **spectrally regular** exactly when

$$
\vec q_+\neq0,\qquad \vec q_-\neq0,\qquad
(t_+,|\vec q_+|)\neq(t_-,|\vec q_-|).
$$

It is **spectrally degenerate** exactly when one of the three cases of the theorem holds.

The cases overlap at the origin and in the both-scalar part of case 3.

## Semisimplicity and the Absence of Defect

**Definition (semisimple and defective).** An element of a finite-dimensional algebra is **semisimple** when its minimal polynomial is squarefree, equivalently when left multiplication by it is diagonalisable over the algebraic closure. An element is **defective** when it is not semisimple.

**Lemma (division algebras have no defect).** Every element of a finite-dimensional division algebra over $\mathbb{R}$ is semisimple.

*Proof.* Let $a$ be an element of a division algebra $D$ with minimal polynomial $m$. If $m=g^2h$ with $g$ non-constant, minimality gives $g(a)\neq0$ and $h(a)\neq0$, while $g(a)^2h(a)=0$; hence $g(a)$ is a zero divisor, impossible. Hence $m$ is squarefree.

**Theorem (every split biquaternion is semisimple).** Every element of $\mathbb{H}_{\mathbb{D}}$ is semisimple. Consequently there is no defective element and no defective stratum.

*Proof.* The two halves $Q_\pm$ lie in $\mathbb{H}$, which is a division algebra, so each is semisimple by the lemma. In the direct sum $\mathbb{H}\oplus\mathbb{H}$, the minimal polynomial of $(Q_+,Q_-)$ is the least common multiple of the minimal polynomials of the two halves. A least common multiple of squarefree polynomials is squarefree, so $\tilde Q$ is semisimple.

**Corollary (repetition is not defect).** A repeated root of $p_{\tilde Q}$ does not make $\tilde Q$ defective. A scalar half has a linear minimal polynomial, not the repeated quadratic $p_\pm$; a shared value occurs in two different summands and is recorded once. In both cases the minimal polynomial remains squarefree.

### The Contrast with the Biquaternion Complex Cone

In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the vector part $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ has complex coefficients and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t.
$$

When $B^2=0$ and $\vec Q\neq0$, the vector part is square-zero, so $L_{\vec Q}$ is nilpotent and $Q_te_t+\vec Q$ has minimal polynomial $(X-Q_t)^2$; it is defective. Thus the spectral cone $\{B^2=0\}$ has defect off its scalar line. This is *[The Spectrum](the-spectrum.html)*, §*The Two Cases* and §*The Degenerate Case: The Spectral-Degenerate Cone*.

The split algebra cannot reproduce this phenomenon. Its vector parts have real coefficients, and

$$
|\vec q_\pm|^2=q_{\pm x}^2+q_{\pm y}^2+q_{\pm z}^2
$$

is a sum of squares, vanishing only at $\vec q_\pm=0$. There is no non-zero isotropic vector, hence no non-zero square-zero vector part, hence no defect of that kind. Structurally, $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is a product of division algebras; a nilpotent in a product would have nilpotent components, and a division algebra has none.

The product structure explains why a meeting is harmless: in $\mathbb{B}$ the two eigenvalues live in the same simple algebra $M_2(\mathbb{C})$, so coalescence can force a Jordan block; in $\mathbb{H}\oplus\mathbb{H}$ they live in different summands, so it is only an equality of values.

## The Scalar Strata of the Halves

**Definition (scalar strata).** The **scalar strata** of the two halves are

$$
\mathcal S_+=\{\tilde Q:\vec q_+=0\},\qquad
\mathcal S_-=\{\tilde Q:\vec q_-=0\}.
$$

**Proposition (geometry and size).** Each scalar stratum is a real linear subspace of dimension five: one real parameter $t_\pm$ for the scalar half and four real parameters for the other half. Their intersection is the centre,

$$
\mathcal S_+\cap\mathcal S_-=\{(t_+,t_-):t_+,t_-\in\mathbb{R}\}=\mathbb{D},
$$

of real dimension two.

*Proof.* The condition $\vec q_+=0$ removes three real coordinates, so $\dim\mathcal S_+=5$; likewise $\dim\mathcal S_-=5$. An element in both has both vector parts zero, so it is a pair of real scalars, exactly the centre $\mathbb{D}$.

**Proposition (the spectrum on a scalar stratum).** On $\mathcal S_+$ the plus half is the real scalar $t_+$, so $p_+=(\lambda-t_+)^2$ has a repeated root; hence $\mathcal S_+\cup\mathcal S_-$ is spectrally degenerate. If $t_+\neq0$ the half is a central unit; if $t_+=0$ it is the zero scalar.

*Proof.* This is case 1 of the repeated-root theorem. The unit and zero-divisor assertions are the invertibility criterion in the idempotent basis.

The scalar strata are the parts of the spectral-degenerate locus where the repetition happens inside one half. The remaining part is the **meeting locus**

$$
\mathcal M=\{\tilde Q:\vec q_+\neq0,\ \vec q_-\neq0,\ t_+=t_-,\ |\vec q_+|=|\vec q_-|\},
$$

where two non-scalar halves share a spectrum value. The spectral-degenerate locus is the union

$$
\{\text{repeated root}\}=\mathcal S_+\cup\mathcal S_-\cup\mathcal M.
$$

The scalar strata are linear; the meeting locus is not, being cut out by the equality of two norms.

## Summary

The spectrum of a split biquaternion is the union of the spectra of its two quaternion halves. A half $Q=t+\vec q$ contributes $t\pm i|\vec q|$, each value twice; when the half is scalar the two values coincide and the multiplicity is four. The reduced characteristic polynomial is $p_{\tilde Q}=p_+p_-$, with $p_\pm=(\lambda-t_\pm)^2+|\vec q_\pm|^2$, and the full characteristic polynomial of left multiplication is $p_{\tilde Q}^2$.

A repeated root occurs exactly when one half is scalar or when the two half-spectra meet. The three cases are $\vec q_+=0$, $\vec q_-=0$, and $t_+=t_-$ with $|\vec q_+|=|\vec q_-|$. Spectral regularity is the negation of this list.

Every element is semisimple, because each half lies in $\mathbb{H}$ and a direct sum of semisimple elements is semisimple. There is no defective element: a repeated root is a repetition of a value, not a Jordan block. The scalar strata are five-dimensional and meet in the two-dimensional centre; the biquaternion algebra, by contrast, has a complex vector part and defective elements off the scalar line. The product structure of the split algebra separates the two eigenvalue problems, and that is why the defect disappears.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{H}\oplus\mathbb{H}$ | Split-biquaternion algebra |
| $\tilde\Pi_{1,2}=\tfrac12(1\pm j)$ | Central idempotents |
| $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$ | Idempotent decomposition into two quaternion halves |
| $Q_\pm=t_\pm+\vec q_\pm$ | A half, with real scalar part and real vector part |
| $\lvert Q_\pm\rvert^2=t_\pm^2+\lvert\vec q_\pm\rvert^2$ | Quaternion norm of a half |
| $\langle\tilde Q\rangle_{\natural}=\lvert Q_+\rvert^2\tilde\Pi_1+\lvert Q_-\rvert^2\tilde\Pi_2$ | Split-biquaternion norm |
| $\Delta=\lvert Q_+\rvert^2\lvert Q_-\rvert^2$ | Reduced norm |
| $p_\pm(\lambda)=(\lambda-t_\pm)^2+\lvert\vec q_\pm\rvert^2$ | Reduced characteristic polynomial of a half |
| $p_{\tilde Q}=p_+p_-$ | Reduced characteristic polynomial of the element |
| $\chi_{\tilde Q}=p_{\tilde Q}^2$ | Characteristic polynomial of $L_{\tilde Q}$ |
| $\sigma(\tilde Q)$ | Spectrum, the union of the two half-spectra |
| $\mathcal S_\pm=\{\vec q_\pm=0\}$ | Scalar strata of the halves |
| $\mathcal M$ | Meeting locus of the two non-scalar half-spectra |

## Further Reading

- [Split-Biquaternion Algebra](split-biquaternion-algebra.html), for the algebra, its idempotents and the isomorphism $\mathbb{H}\oplus\mathbb{H}$.
- [Split-Biquaternion Idempotents and Projections](split-biquaternion-idempotents-and-projections.html), for the four idempotents.
- [Split-Biquaternion Norm and Invertibility](split-biquaternion-norm-and-invertibility.html), for the norm, the reduced norm and the unit criterion.
- [Split-Biquaternion Spectral Theory](split-biquaternion-spectral-theory.html), for left multiplication and the quaternionic spectra.
- [The Spectrum](the-spectrum.html), for the complex cone and the defective elements off the scalar line.
- [The Reduced Norm and Spectral Degeneracy in the Split-Biquaternion Algebra](relations-between-the-split-biquaternion-reduced-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of the two predicates.
- [The Three Sectors of the Split-Biquaternion Algebra](the-three-sectors-of-the-split-biquaternion-algebra.html), for the cells and their dimensions.
