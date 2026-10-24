# __The Norm-Degenerate, Spectrally Degenerate Sector__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries two quadratic conditions. The reduced norm $N(\tilde Q)=Q_t^2+B^2$, with $B^2=Q_x^2+Q_y^2+Q_z^2$, vanishes exactly on the non-units; its zero locus is the null cone $\mathcal C$. The square $B^2$ of the vector part vanishes exactly when the two eigenvalues of $\tilde Q$ coincide; its zero locus is the spectral-degenerate cone $\mathcal S$. The two conditions cut the algebra into four sectors. Write $\Sigma_{ij}$ for the sector with $i=1$ if $N\neq0$ and $i=0$ if $N=0$, and $j=1$ if $B^2\neq0$ and $j=0$ if $B^2=0$. This article treats $\Sigma_{00}$, the sector on which both conditions degenerate; the doubly regular sector $\Sigma_{11}$ is the sector on which neither does.

The sector is the set-theoretic intersection of the two cones. It has three descriptions, given in §*The Sector and Its Three Descriptions*: it is $\{Q_t=0,\ \vec Q^2=0\}$, it is the set of square-zero elements, and it is the pure stratum of the null cone with the origin adjoined. The article then computes its geometry (a complex cone of dimension two), its elements (nilpotents of index two), the special role of the origin, and its behaviour under multiplication. The last sections compare it with the other three sectors and collect the consequences.

**Scope and naming.** The product is the plain product of $\mathbb{B}$; the algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_k^2=-e_t$; the conjugation is ${}^{\natural}$, and $N(\tilde Q)=\tilde Q^{\natural}\tilde Q$ is central. The null cone is written $\mathcal C$ and the spectral-degenerate cone $\mathcal S$, as in *Norm Regularity and Degeneracy in the Biquaternion Algebra* and *Spectral Regularity and Degeneracy in the Biquaternion Algebra*. A **sector** is one of the four cells cut out by the two conditions. The word degenerate is qualified by the condition it refers to, so "doubly degenerate" means $N=0$ and $B^2=0$.

## The Sector and Its Three Descriptions

**Definition.** The sector is

$$
\Sigma_{00}=\{N=0,\ B^2=0\}=\{Q_t^2+B^2=0,\ B^2=0\}.
$$

**Theorem (three descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\tilde Q\in\Sigma_{00}$;

(ii) $\tilde Q^2=0$;

(iii) $Q_t=0$ and $\vec Q^2=0$.

*Proof.* The identity

$$
\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q
$$

separates the central and the vector parts, so $\tilde Q^2=0$ exactly when $Q_t^2=B^2$ and $Q_t\vec Q=0$. If $Q_t\neq0$, the second equation gives $\vec Q=0$, hence $B^2=0$, hence $Q_t^2=0$, a contradiction. Therefore $Q_t=0$, and then $B^2=0$. Conversely, $Q_t=0$ and $B^2=0$ give $\tilde Q^2=-B^2e_t=0$. This proves (ii) $\iff$ (iii). For (i), $N=0$ with $Q_t=0$ gives $B^2=0$; conversely $N=0$ with $B^2=0$ gives $Q_t^2=0$, hence $Q_t=0$.

**Remark (the names of the pieces).** On $\Sigma_{00}\setminus\{0\}$ the three descriptions say: pure, square-zero, nilpotent of index two. This is exactly the **pure stratum** $\mathcal C_{\mathrm p}$ of the null cone of *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Two Strata*. The sector adds the origin, which is square-zero but is not a nilpotent of index two, since the word is reserved for non-zero elements. The name "nilpotent cone" refers to $\mathcal C_{\mathrm p}$; the sector is that cone with its apex adjoined.

## Geometry

**Theorem (a complex cone of dimension two).** $\Sigma_{00}$ is a complex cone of complex dimension $2$ and real dimension $4$ in $\mathbb{B}\cong\mathbb{C}^4$. It is smooth away from the origin and singular only at the origin.

*Proof.* The sector is the common zero set of $Q_t$ and $B^2=Q_x^2+Q_y^2+Q_z^2$. Their gradients are $(1,0,0,0)$ and $(0,2Q_x,2Q_y,2Q_z)$, which are linearly independent whenever $\vec Q\neq0$. Off the origin the intersection is therefore smooth of complex dimension $4-2=2$, hence of real dimension $4$. At the origin the second gradient vanishes: the variety is the cone over the smooth conic $\{Q_x^2+Q_y^2+Q_z^2=0\}\subset\mathbb{P}^2$ with apex $0$. Its Zariski tangent space there is $\{Q_t=0\}$, of dimension $3$, while the variety has dimension $2$, so the origin is singular. It is the only singular point.

**Bivector form and parametrisation.** Write $\vec Q=\vec\rho+i\vec\rho'$ with $\vec\rho,\vec\rho'\in\mathbb{R}^3$. Then

$$
B^2=(|\vec\rho|^2-|\vec\rho'|^2)+2i\,\vec\rho\cdot\vec\rho',
$$

so $B^2=0$ is equivalent to $|\vec\rho|=|\vec\rho'|$ and $\vec\rho\perp\vec\rho'$. Every point of the sector is therefore

$$
\tilde Q=r(\vec u+i\vec u_\perp),\qquad r\ge0,\quad \vec u\ \text{a real unit vector},\quad \vec u_\perp\ \text{a real unit vector perpendicular to}\ \vec u,
$$

the origin occurring at $r=0$. The count is $1+2+1=4$ real parameters, in agreement with the dimension. This is the parametrisation of the pure stratum of *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Two Strata*, with $r=0$ added.

**Scheme-theoretic form.** As a scheme, the intersection of the two cones is defined by

$$
(Q_t^2+B^2,\ B^2)=(Q_t^2,\ B^2),
$$

whose reduction is $(Q_t,\ B)$: the point set is the same, and the sector is a complete intersection of codimension two. The ideal is generated by two squares, so the scheme is non-reduced along both hypersurfaces, with multiplicity two in the scalar direction and multiplicity two in the normal direction of the isotropic cone.

## The Elements

Let $\tilde Q\in\Sigma_{00}$ with $\tilde Q\neq0$, so $\tilde Q=\vec\Upsilon$ is a pure nilpotent of index two.

**Annihilators.** In the plain product, the left and right annihilators

$$
A(\tilde Q)=\ker L_{\tilde Q}=\{\tilde X:\tilde Q\tilde X=0\},\qquad
B(\tilde Q)=\ker R_{\tilde Q}=\{\tilde X:\tilde X\tilde Q=0\}
$$

are distinct complex planes of $\mathbb{C}^4$, each of dimension two, meeting in the line $\mathbb{C}\tilde Q$. Both contain $\tilde Q$ because $\tilde Q^2=0$. The image of $L_{\tilde Q}$ is the left ideal $\mathbb{B}\tilde Q$, non-zero and proper, hence minimal of complex dimension two (*Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Decomposition into Minimal Left and Right Ideals*), so $L_{\tilde Q}$ has rank two and its kernel is a plane; the same argument on the right gives rank two for $R_{\tilde Q}$. The two planes cannot coincide, because $A(\tilde Q)$ is a right ideal and $B(\tilde Q)$ is a left ideal, so a common plane would be a two-sided ideal of the simple algebra $\mathbb{B}$, which a plane is not. Finally, $X\tilde Q=0$ is equivalent to $\tilde Q X^{\natural}=0$ because $\tilde Q^{\natural}=-\tilde Q$, so the conjugation exchanges the two planes:

$$
A(\tilde Q)^{\natural}=B(\tilde Q).
$$

Under the $\natural$-bilinear product $\tilde P\circ\tilde Q=\tilde P^{\natural}\tilde Q$, the left annihilator of $\tilde Q$ is therefore the other plane, $B(\tilde Q)$.

**One-sided multiplication.** Left and right multiplication by $\tilde Q$ both have complex rank $2$, with kernels $A(\tilde Q)$ and $B(\tilde Q)$. Both are square-zero operators,

$$
L_{\tilde Q}^2=L_{\tilde Q^2}=0,\qquad R_{\tilde Q}^2=R_{\tilde Q^2}=0,
$$

because $\tilde Q^2=0$. Neither is injective and neither is surjective, so $\tilde Q$ has no inverse on either side.

**Centraliser.** The centraliser is the plane

$$
\mathbb{C}[\tilde Q]=\{a e_t+b\tilde Q\ :\ a,b\in\mathbb{C}\}.
$$

Indeed, an element $X=x_0e_t+\vec x$ commutes with $\tilde Q=\vec\Upsilon$ exactly when $\vec x\times\vec\Upsilon=0$, that is, exactly when $\vec x$ is a multiple of $\vec\Upsilon$. Its only idempotents are $0$ and $e_t$: from $a^2=a$ and $2ab=b$ one obtains $(a,b)=(0,0)$ or $(1,0)$. Hence **no non-trivial idempotent commutes with $\tilde Q$**, and $\tilde Q$ admits no adapted Peirce decomposition.

**Peirce form.** Let $e$ be the projection onto the image of $\tilde Q$ along a complementary line. Since $\tilde Q$ kills its image, $e\tilde Q=\tilde Q$ and $\tilde Qe=0$; with $f=e_t-e$, the Peirce form is purely off-diagonal:

$$
e\tilde Qe=0,\qquad e\tilde Qf=\tilde Q,\qquad f\tilde Qe=0,\qquad f\tilde Qf=0.
$$

So $\tilde Q$ lies wholly in the mixed corner $\mathbb{B}_{+-}$ of that pair. No Peirce decomposition adapted to $\tilde Q$ can exist, since an adapted one would place $\tilde Q$ in the diagonal corners $\mathbb{B}_{++}\oplus\mathbb{B}_{--}$.

**Spectrum and minimal polynomial.** The spectrum is $\{0\}$ and the minimal polynomial is $X^2$, not $X$: the element is defective, a single Jordan block of size two with eigenvalue $0$.

## The Origin

The origin $\tilde Q=0$ lies in $\Sigma_{00}$ and is its only element that is not a nilpotent of index two.

- It is scalar, central and semisimple, with minimal polynomial $X$.
- It is the apex of the null cone, and it lies on the vertex $\mathbb{C}e_t$ of the spectral cone.
- It is the only element of the sector on which both multiplications are the zero map, $L_0=R_0=0$, of rank $0$ and kernel $\mathbb{B}$.
- It lies in the closure of every other sector: every sector is invariant under the scaling $\tilde Q\mapsto\lambda\tilde Q$ for $\lambda\neq0$, so every punctured neighbourhood of $0$ meets all four.
- It is the only diagonalisable element of the sector, which is why "spectrally degenerate" does not coincide with "non-diagonalisable".

## Multiplication

**The sector is not closed under the product.** The reduced norm is multiplicative, so $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)=0$ for $\tilde P,\tilde Q\in\Sigma_{00}$: products stay on the null cone. They do not stay on the sector. The witness is

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2e_t-2i\vec e_z,
$$

whose vector square is $B^2=(-2i)^2=-4\neq0$. The product lies in the norm-degenerate, spectrally regular sector $\Sigma_{01}$.

**Theorem (where the products go).** A product of two elements of $\Sigma_{00}$ is either $0$ or lies in $\Sigma_{01}$:

$$
\Sigma_{00}\cdot\Sigma_{00}\subseteq\{0\}\cup\Sigma_{01}.
$$

*Proof.* Write the non-zero factors as pure vectors, $\tilde P=\vec u$ and $\tilde Q=\vec v$, with $\vec u^2=\vec v^2=0$. Then

$$
\tilde P\tilde Q=-\vec u\cdot\vec v+\vec u\times\vec v.
$$

If the scalar part vanishes, $\vec u$ and $\vec v$ are orthogonal isotropic vectors of $\mathbb{C}^3$, hence proportional, since otherwise they would span a totally isotropic plane, which the form $Q_x^2+Q_y^2+Q_z^2$ does not admit; then the product is zero. If the scalar part does not vanish, the product has $N=0$ and

$$
B^2(\tilde P\tilde Q)=-(\vec u\cdot\vec v)^2\neq0,
$$

so it lies in $\Sigma_{01}$.

Both alternatives occur: the square of any element of the sector is $0$, and the witness above lands in $\Sigma_{01}$. Consequently the sector is a set of nilpotents, not a subalgebra: it is not closed under multiplication, and it is not a subsemigroup of the multiplicative semigroup $\mathcal C$.

## Relation to the Two Cones

**The sector is the intersection.** As point sets, $\Sigma_{00}=\mathcal C\cap\mathcal S$; as schemes, the ideal is $(Q_t^2,B^2)$, as computed in §*Geometry*. It is the only sector contained in both cones.

**The two cones are tangent along the whole sector.** Their algebraic gradients are

$$
\nabla N=2(Q_t,\vec Q),\qquad \nabla B^2=2(0,\vec Q),
$$

and they agree wherever $Q_t=0$, that is, on all of $\Sigma_{00}$. At the origin both vanish. The intersection is therefore nowhere transverse: it is a tangency of the two cones, not a transverse crossing, which is why its dimension is the expected $4-2=2$ while its scheme is non-reduced.

**The unique coincidence of the two degenerations.** $\Sigma_{00}$ is the only sector on which both questions of the arrangement — can $\tilde Q$ be inverted? can its two eigenvalues be told apart? — receive the negative answer. It is what the two cones have in common beyond their shared apex.

## Comparison with the Other Three Sectors

| sector | conditions | elements | adapted Peirce | product |
|---|---|---|---|---|
| **doubly regular** $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | units with distinct eigenvalues | exists, unique | $N\neq0$ preserved; can land in $\Sigma_{10}$ |
| **norm-degenerate, spectrally regular** $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | $2Q_t\tilde\Pi$ with $\tilde\Pi$ a non-trivial idempotent and $Q_t\neq0$; spectrum $\{0,2Q_t\}$ | exists, unique | $N=0$ preserved; can land in $\Sigma_{00}$ |
| **norm-regular, spectrally degenerate** $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | units with a repeated eigenvalue, plus the scalar line minus $0$; spectrum $\{Q_t\}$ | fails off the scalar line, one term on it | $N\neq0$ preserved; can land in $\Sigma_{11}$ |
| **doubly degenerate** $\Sigma_{00}$ | $N=0$, $B^2=0$ | non-zero nilpotents of index two, plus the origin; spectrum $\{0\}$ | fails off the origin | $0$ or $\Sigma_{01}$ |

**No sector is closed under multiplication.** Only the norm dichotomy is: $\mathcal C$ is a semigroup and $\mathbb{B}^{\times}$ is a group. The four witnesses are

$$
(e_t+\vec e_x)(e_t-\vec e_x)=2e_t\in\Sigma_{10},
$$

$$
(e_t+i\vec e_x)(e_t-i\vec e_x)=0\in\Sigma_{00},
$$

$$
(e_t+\vec e_x+i\vec e_y)(2e_t+\vec e_x-i\vec e_y)=3\vec e_x+i\vec e_y-2i\vec e_z\in\Sigma_{11},
$$

$$
(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=-2e_t-2i\vec e_z\in\Sigma_{01}.
$$

The first product has $N=4$ and $B^2=0$; the second vanishes because $(e_t+i\vec e_x)(e_t+i\vec e_x)^{\natural}=N(e_t+i\vec e_x)e_t=0$; the third has $N=4$ and $B^2=4$; the fourth has $N=0$ and $B^2=-4$. So each sector leaks into another, and the finer spectral split is not multiplicative.

The two mixed sectors, $\Sigma_{01}$ and $\Sigma_{10}$, are the witnesses that the two problems are independent: each is degenerate in one respect and non-degenerate in the other. The sector $\Sigma_{00}$ is the opposite case, where the two answers coincide, both negative, and it is the unique such sector.

## Consequences

**Eigenbasis.** None, except at the origin. Every non-zero element of $\Sigma_{00}$ has characteristic and minimal polynomial $X^2$: it is a single Jordan block with eigenvalue $0$; the eigenspace is the annihilator plane $A(\tilde Q)$.

**Polar decomposition.** The modulus is $\Rho=\sqrt{N(\tilde Q)}=0$, so the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Biquaternions* has no value on the sector: there is no unit factor of norm one.

**One-sided operators.** Rank $2$, square-zero; the kernels are the two annihilator planes; neither multiplication is invertible on either side.

**The "everything fails" cell.** It is the cell in which invertibility, the adapted Peirce decomposition (off the origin), the eigenbasis, the polar decomposition and the injectivity of both multiplications all fail. It is what makes the two problems look alike before the mixed sectors separate them.

## Summary

| question | answer |
|---|---|
| definition | $\Sigma_{00}=\{N=0,\ B^2=0\}$ |
| three descriptions | $\tilde Q^2=0$; $Q_t=0$ and $\vec Q^2=0$; the pure stratum with the origin adjoined |
| geometry | complex cone of complex dimension $2$ and real dimension $4$; smooth off $0$, singular only at $0$ |
| elements | non-zero nilpotents of index two, plus the origin |
| annihilators | two distinct planes of dimension $2$ meeting in $\mathbb{C}\tilde Q$, exchanged by the conjugation |
| centraliser | $\mathbb{C}[\tilde Q]$, with idempotents $0$ and $e_t$ |
| Peirce form | purely off-diagonal; no adapted decomposition off the origin |
| spectrum | $\{0\}$, minimal polynomial $X^2$ |
| multiplication | $\Sigma_{00}\cdot\Sigma_{00}\subseteq\{0\}\cup\Sigma_{01}$ |
| relation to the cones | $\Sigma_{00}=\mathcal C\cap\mathcal S$, with the two cones tangent along the whole sector |
| place in the arrangement | the only sector on which both answers are negative |

The sector is the doubly degenerate cell: the set of square-zero elements, the intersection of the two cones, the locus on which invertibility and spectral separation are both answered in the negative, and the one place where the origin, a semisimple point, sits among the defective ones.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{ij}$ | the sector with $i=1$ iff $N\neq0$, $j=1$ iff $B^2\neq0$ |
| $\Sigma_{00}$ | the doubly degenerate sector, this article |
| $\mathcal C=\{N=0\}$ | the null cone of the reduced norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathcal C_{\mathrm p}$ | the pure stratum of the null cone, $\Sigma_{00}\setminus\{0\}$ |
| $\vec\Upsilon$ | a non-zero pure vector with $\vec\Upsilon^2=0$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication |
| $A(\tilde Q)=\ker L_{\tilde Q}$ | the left annihilator, a right ideal |
| $B(\tilde Q)=\ker R_{\tilde Q}$ | the right annihilator, a left ideal |
| $\nabla N$, $\nabla B^2$ | the algebraic gradients $2(Q_t,\vec Q)$ and $2(0,\vec Q)$ |

## Further Reading

- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the reduced norm, the null cone, its pure and non-pure strata, and the annihilator planes.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the spectral-degenerate cone, the three regimes and the independence of the two cones.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus $\Rho=\sqrt{N}$ and the unit factor of norm one.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the Peirce corners and their dimensions.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the place of $N$ among the four norms and of $B^2$ outside them.
