# __The Three Sectors of the Split-Biquaternion Algebra__

## Introduction

Two predicates cut the split-biquaternion algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ into four cells: the reduced norm $\Delta=|Q_+|^2|Q_-|^2$ is zero or non-zero, and the reduced characteristic polynomial $p_{\tilde Q}=p_+p_-$ has a repeated root or not. The four cells are the **sectors** $\Sigma_{ij}$, with $i=1$ for $\Delta\neq0$ and $j=1$ for spectral regularity. Three of them are non-empty; the fourth, $\Sigma_{01}$, is empty. This article defines the sectors, proves that three are non-empty and one is empty, and describes each one with its dimension and closure. The spectral criterion is *[Spectral Regularity and Degeneracy in the Split-Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-biquaternion-algebra.html)*; the comparison is *[The Reduced Norm and Spectral Degeneracy in the Split-Biquaternion Algebra](relations-between-the-split-biquaternion-reduced-norm-and-spectral-regularity-and-degeneracy.html)*.

**Conventions.** The split complex unit is $j$, with $j^2=1$, and $\tilde\Pi_{1,2}=\tfrac12(1\pm j)$. An element is $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$ with $Q_\pm=t_\pm+\vec q_\pm$, $t_\pm\in\mathbb{R}$, $\vec q_\pm=\sum_k q_{\pm k}\vec e_k$, $|\vec q_\pm|^2=\sum_k q_{\pm k}^2$, and $|Q_\pm|^2=t_\pm^2+|\vec q_\pm|^2$. The reduced norm is $\Delta=|Q_+|^2|Q_-|^2$. The spectrum is $\{t_+\pm i|\vec q_+|\}\cup\{t_-\pm i|\vec q_-|\}$, and a repeated root occurs exactly when $\vec q_+=0$, or $\vec q_-=0$, or $t_+=t_-$ and $|\vec q_+|=|\vec q_-|$. The algebra is *[Split-Biquaternion Algebra](split-biquaternion-algebra.html)*; the norm and zero divisors are *[Split-Biquaternion Norm and Invertibility](split-biquaternion-norm-and-invertibility.html)* and *[Split-Biquaternion Zero Divisors](split-biquaternion-zero-divisors.html)*.

## The Sectors

**Definition (sectors).** For $i,j\in\{0,1\}$, the **sector** $\Sigma_{ij}$ is the set of elements with $\Delta\neq0$ if $i=1$ and $\Delta=0$ if $i=0$, and with no repeated root of $p_{\tilde Q}$ if $j=1$ and with a repeated root if $j=0$. Explicitly,

$$
\Sigma_{11}=\{\Delta\neq0,\ \text{spectrally regular}\},\qquad
\Sigma_{10}=\{\Delta\neq0,\ \text{spectrally degenerate}\},
$$

$$
\Sigma_{01}=\{\Delta=0,\ \text{spectrally regular}\},\qquad
\Sigma_{00}=\{\Delta=0,\ \text{spectrally degenerate}\}.
$$

The index $i$ refers to the reduced norm, not to a half's quaternion norm. The index $j$ refers to the reduced polynomial $p_{\tilde Q}$; the full operator polynomial is $p_{\tilde Q}^2$, so the two have the same root set.

**Proposition (explicit conditions).** The sectors are also given by

$$
\Sigma_{11}=\{\Delta\neq0,\ \vec q_+\neq0,\ \vec q_-\neq0,\ (t_+,|\vec q_+|)\neq(t_-,|\vec q_-|)\},
$$

$$
\Sigma_{10}=\{\Delta\neq0,\ \vec q_+=0\text{ or }\vec q_-=0\text{ or }(t_+=t_-,\ |\vec q_+|=|\vec q_-|)\},
$$

$$
\Sigma_{00}=\{\Delta=0\},\qquad
\Sigma_{01}=\{\Delta=0,\ \vec q_+\neq0,\ \vec q_-\neq0,\ (t_+,|\vec q_+|)\neq(t_-,|\vec q_-|)\}.
$$

*Proof.* The repeated-root criterion says that a repeated root occurs exactly in the three displayed cases. Its negation is that both vector parts are non-zero and the pairs $(t_\pm,|\vec q_\pm|)$ differ. On $\Sigma_{11}$ that negation holds; on $\Sigma_{10}$ it fails and $\Delta\neq0$; on $\Sigma_{00}$ the reduced norm vanishes; on $\Sigma_{01}$ the negation holds and the reduced norm vanishes.

**Theorem (partition).** The algebra is the disjoint union

$$
\mathbb{H}_{\mathbb{D}}=\Sigma_{11}\sqcup\Sigma_{10}\sqcup\Sigma_{01}\sqcup\Sigma_{00}.
$$

*Proof.* Each element has exactly one truth value for $\Delta\neq0$ and exactly one for "spectrally regular", hence lies in exactly one of the four combinations.

## Three Non-Empty Sectors and One Empty Sector

**Theorem (the count).** $\Sigma_{11}$, $\Sigma_{10}$ and $\Sigma_{00}$ are non-empty, and $\Sigma_{01}$ is empty.

*Proof.* Three witnesses and one theorem.

- **$\Sigma_{11}$.** Take $Q_+=\vec e_x$ and $Q_-=2\vec e_z$. Then $\Delta=1\cdot4=4$. The plus spectrum is $\{i,-i\}$ and the minus spectrum is $\{2i,-2i\}$; they are disjoint, so the element is spectrally regular.
- **$\Sigma_{10}$.** Take $Q_+=1$ and $Q_-=\vec e_z$. Then $\Delta=1$. The plus half is scalar, so $p_+=(\lambda-1)^2$ has the repeated root $1$; the element is spectrally degenerate.
- **$\Sigma_{00}$.** Take $Q_+=0$ and $Q_-=1$. Then $\Delta=0$; the element is a zero divisor, hence spectrally degenerate.

For $\Sigma_{01}$, suppose $\Delta=0$. By the zero criterion, $Q_+=0$ or $Q_-=0$. A zero half is the zero scalar, so $\vec q_+=0$ or $\vec q_-=0$; by the repeated-root criterion, $p_{\tilde Q}$ has a repeated root. Hence no element of $\{\Delta=0\}$ is spectrally regular, and $\Sigma_{01}=\varnothing$.

**Corollary (three sectors).** The algebra is the disjoint union of the three non-empty sectors

$$
\mathbb{H}_{\mathbb{D}}=\Sigma_{11}\sqcup\Sigma_{10}\sqcup\Sigma_{00}.
$$

The fourth cell is empty, so the partition has three members.

## The Sector $\Sigma_{11}$: Reduced-Norm-Regular, Spectrally Regular

**Description.** $\Sigma_{11}$ consists of the units whose two halves are both non-scalar and whose half-spectra are disjoint. It is the complement of the set where one half is scalar or the two spectra meet.

**Theorem (dimension and topology).** $\Sigma_{11}$ is open and dense in $\mathbb{H}_{\mathbb{D}}\cong\mathbb{R}^8$, has real dimension $8$, and its complement $S$ is closed of real dimension $6$. Hence $\Sigma_{11}$ has full measure and is the generic sector.

*Proof.* Let

$$
S=\{\vec q_+=0\}\cup\{\vec q_-=0\}\cup\{t_+=t_-,\ |\vec q_+|=|\vec q_-|\}.
$$

The first two sets are linear subspaces of dimension $5$. The third contains a $6$-dimensional piece, with $t_+=t_-$, $\vec q_+\neq0$, and a unit direction for $\vec q_-$; its remaining part is the diagonal scalar line of dimension $2$. Their union is closed of dimension $6$. Its complement is exactly $\Sigma_{11}$, and since $S$ is closed of dimension $6$, that complement is open, dense and of full measure.

**Proposition (inverse closure).** If $\tilde Q\in\Sigma_{11}$, then $\tilde Q^{-1}\in\Sigma_{11}$.

*Proof.* The halves of the inverse are $Q_\pm^{-1}$, both non-zero. A quaternion is scalar exactly when its inverse is scalar, so both inverse halves are non-scalar. The spectrum of $Q_\pm^{-1}$ is the image of the spectrum of $Q_\pm$ under $z\mapsto z^{-1}$; since inversion is injective, disjointness is preserved. Finally $\Delta(\tilde Q^{-1})=\Delta(\tilde Q)^{-1}\neq0$.

**Proposition (not product closed).** The product of two elements of $\Sigma_{11}$ need not lie in $\Sigma_{11}$.

*Proof.* Take $Q_+=\vec e_x$ and $Q_-=2\vec e_z$, an element of $\Sigma_{11}$. Its square has halves $\vec e_x^2=-1$ and $(2\vec e_z)^2=-4$, both non-zero real scalars. It is a unit with a repeated root, hence lies in $\Sigma_{10}$.

## The Sector $\Sigma_{10}$: Reduced-Norm-Regular, Spectrally Degenerate

**Description.** $\Sigma_{10}$ consists of the units with a repeated root. The repetition has two causes: one half is scalar, or the two non-scalar half-spectra meet.

**Definition (the three pieces).** Put

$$
\Sigma_{10}^{+}=\{\vec q_+=0,\ t_+\neq0,\ Q_-\neq0\},\qquad
\Sigma_{10}^{-}=\{\vec q_-=0,\ t_-\neq0,\ Q_+\neq0\},
$$

$$
\Sigma_{10}^{\mathrm{m}}=\{t_+=t_-,\ |\vec q_+|=|\vec q_-|>0\}.
$$

**Proposition (decomposition).** $\Sigma_{10}=\Sigma_{10}^{+}\cup\Sigma_{10}^{-}\cup\Sigma_{10}^{\mathrm{m}}$.

*Proof.* If a half is scalar and non-zero, the element lies in $\Sigma_{10}^{+}$ or $\Sigma_{10}^{-}$, and $\Delta\neq0$ exactly when the other half is non-zero. If no half is scalar and the spectra meet, both vector parts are non-zero, $t_+=t_-$, and the norms are equal, so the element lies in $\Sigma_{10}^{\mathrm{m}}$. Conversely, each of the three pieces has $\Delta\neq0$ and a repeated root.

**Theorem (dimension and closure).** $\Sigma_{10}$ has real dimension $6$, empty interior, and closure

$$
\overline{\Sigma_{10}}=\Sigma_{10}\cup\Sigma_{00}=S.
$$

It is neither open nor closed.

*Proof.* Each of $\Sigma_{10}^{+}$ and $\Sigma_{10}^{-}$ has dimension $1+4=5$; $\Sigma_{10}^{\mathrm{m}}$ has dimension $1+3+2=6$. The union has dimension $6$. It has empty interior because it is contained in $S$, which has dimension $6$ in $\mathbb{R}^8$. The closure of $\Sigma_{10}$ is $S$: every point of $\Sigma_{00}$ is a limit of points of $\Sigma_{10}$ obtained by perturbing its zero halves to small non-zero scalars, and every other point of $S$ lies in $\Sigma_{10}$. Since $S$ is closed and strictly larger than $\Sigma_{10}$, the sector is not closed; since it has empty interior, it is not open.

**Theorem (no defect).** Every element of $\Sigma_{10}$ is semisimple. The repeated root is a coalescence of eigenvalues, not a Jordan block.

*Proof.* This is the semisimplicity theorem of *[Spectral Regularity and Degeneracy in the Split-Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-biquaternion-algebra.html)*: each half lies in the division algebra $\mathbb{H}$, hence is semisimple, and a direct sum of semisimple elements is semisimple. On the scalar pieces the minimal polynomial of the scalar half is linear; on the meeting piece the shared root occurs in two different summands and is recorded once.

## The Sector $\Sigma_{00}$: Reduced-Norm-Degenerate

**Description.** $\Sigma_{00}$ consists of the zero divisors together with the origin. It is the union of the two four-dimensional subspaces

$$
Z_+=\{Q_+=0\},\qquad Z_-=\{Q_-=0\},
$$

which meet only at $0$.

**Theorem (dimension, closure and nilpotents).** $\Sigma_{00}$ is closed, has real dimension $4$, and is the union of two $4$-planes that meet at the origin. It contains no non-zero nilpotent. Every element of $\Sigma_{00}$ is semisimple.

*Proof.* The condition $Q_+=0$ is four real linear equations, so $Z_+$ has dimension $4$; likewise $Z_-$. Their intersection is $Q_+=Q_-=0$, the origin. The set $\Sigma_{00}=Z_+\cup Z_-$ is closed, and its dimension is $4$. If $\tilde Q^2=0$, then $Q_+^2=0$ and $Q_-^2=0$; a division algebra has no non-zero nilpotent, so $Q_+=Q_-=0$ and $\tilde Q=0$. Semisimplicity is the general theorem for all elements of $\mathbb{H}_{\mathbb{D}}$.

**Proposition (spectrum).** Every element of $\Sigma_{00}$ is spectrally degenerate. If $Q_+=0$ and $Q_-\neq0$, the spectrum is $\{0\}\cup\{t_-\pm i|\vec q_-|\}$, and the value $0$ is repeated; the same holds with the halves exchanged.

*Proof.* The zero half has $t=0$ and $\vec q=0$, so its reduced polynomial is $\lambda^2$; the repeated-root criterion applies. The displayed spectrum is the union formula of the spectral article.

**Remark (the defining equation).** The set $\Sigma_{00}$ is not the zero set of the split-biquaternion norm: that norm is anisotropic and vanishes only at $0$. It is the zero set of the reduced norm $\Delta$, a real quartic that factors as $|Q_+|^2|Q_-|^2$.

## The Absence of a Defective Stratum

**Definition (defective).** An element is **defective** when it is not semisimple, equivalently when its minimal polynomial has a repeated factor.

**Theorem (no defective stratum).** Every element of $\mathbb{H}_{\mathbb{D}}$ is semisimple. Hence no sector contains a defective stratum.

*Proof.* Each half lies in the division algebra $\mathbb{H}$ and is semisimple. The minimal polynomial of the pair is the least common multiple of the two half-minimal-polynomials, and a least common multiple of squarefree polynomials is squarefree.

The decomposition of $\Sigma_{10}$ into the scalar pieces and the meeting locus is therefore by the **cause** of the repeated root, not by defect. The biquaternion degenerate sector has nilpotent and Jordan strata; here neither occurs, only the scalar stratum. A nilpotent in a product would have nilpotent components, and a division algebra has none.

## The Sectors at a Glance

| Sector | Condition | Description | Dimension |
|---|---|---|---|
| $\Sigma_{11}$ | $\Delta\neq0$, $\vec q_\pm\neq0$, $(t_+,\lvert\vec q_+\rvert)\neq(t_-,\lvert\vec q_-\rvert)$ | Units with two non-scalar halves and disjoint spectra; open and dense | $8$ |
| $\Sigma_{10}$ | $\Delta\neq0$ and ($\vec q_+=0$ or $\vec q_-=0$ or ($t_+=t_-$, $\lvert\vec q_+\rvert=\lvert\vec q_-\rvert$)) | Units with a scalar half or meeting spectra; semisimple, empty interior | $6$ |
| $\Sigma_{00}$ | $\Delta=0$ | Zero divisors and $0$; one half zero; two $4$-planes | $4$ |
| $\Sigma_{01}$ | $\Delta=0$ and spectrally regular | Empty | --- |

## Summary

Two predicates cut the algebra into four sectors. Spectral regularity and reduced-norm regularity are not independent: $\Sigma_{01}$ is empty, because a vanishing reduced norm forces one half to be zero, and a zero half is a repeated root at zero. The three non-empty sectors are $\Sigma_{11}$, the units with two non-scalar halves and disjoint spectra; $\Sigma_{10}$, the units with a scalar half or meeting spectra; and $\Sigma_{00}$, the zero divisors and the origin.

The dimensions are $8$, $6$ and $4$. $\Sigma_{11}$ is open and dense; $\Sigma_{10}$ has empty interior and closure $S$; $\Sigma_{00}$ is closed, the union of two $4$-planes. Every element is semisimple, so there is no defective stratum: the repeated roots are repetitions of eigenvalues, not Jordan blocks. The biquaternion algebra has a Jordan part and nilpotents; the product of two division algebras removes both.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ | Split-biquaternion algebra |
| $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$ | Idempotent decomposition |
| $Q_\pm=t_\pm+\vec q_\pm$ | A half |
| $\Delta=\lvert Q_+\rvert^2\lvert Q_-\rvert^2$ | Reduced norm |
| $\Sigma_{ij}$ | Sector with reduced-norm index $i$ and spectral index $j$ |
| $\Sigma_{11}$ | Reduced-norm regular, spectrally regular |
| $\Sigma_{10}$ | Reduced-norm regular, spectrally degenerate |
| $\Sigma_{00}$ | Reduced-norm degenerate, spectrally degenerate |
| $\Sigma_{01}$ | Reduced-norm degenerate, spectrally regular; empty |
| $S=\Sigma_{10}\cup\Sigma_{00}$ | Complement of $\Sigma_{11}$ and closure of $\Sigma_{10}$ |
| $Z_\pm=\{Q_\pm=0\}$ | The two $4$-planes of $\Sigma_{00}$ |

## Further Reading

- [Split-Biquaternion Algebra](split-biquaternion-algebra.html), for the algebra and its idempotents.
- [Split-Biquaternion Norm and Invertibility](split-biquaternion-norm-and-invertibility.html), for the reduced norm and the unit criterion.
- [Split-Biquaternion Zero Divisors](split-biquaternion-zero-divisors.html), for the two ideals $Z_+$ and $Z_-$.
- [Spectral Regularity and Degeneracy in the Split-Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-biquaternion-algebra.html), for the union spectrum and the repeated-root criterion.
- [The Reduced Norm and Spectral Degeneracy in the Split-Biquaternion Algebra](relations-between-the-split-biquaternion-reduced-norm-and-spectral-regularity-and-degeneracy.html), for the empty mixed cell and the chain of invariants.
- [The Spectrum](the-spectrum.html), for the defective Jordan part and the nilpotents.
