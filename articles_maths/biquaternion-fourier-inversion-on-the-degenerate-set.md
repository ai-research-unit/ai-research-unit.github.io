# __Biquaternion Fourier Inversion on the Degenerate Set: Peirce Coordinates and the Exponential__

## Introduction

This article computes the inversion of the biquaternion Fourier transform at the frequencies where the symbol is **not a unit**, and it does so in a frame in which the algebra becomes two-by-two complex matrices. **The frame is the Peirce frame of a complete pair of idempotents, and in it the symbol is a matrix, the norm is its determinant, and the inversion is the adjugate.** That is the first half of the article. The second half is negative: the route through the exponential, which is the route of *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*, closes before it reaches the degenerate set, and the article proves the closure in all three cases of the closed form rather than asserting it.

**The status of each part, stated once.** §*The Peirce Frame of the Algebra* and §*The Degenerate Set in Coordinates* are proved, from the frame outwards, with no appeal beyond the matrix units. §*Inversion in Peirce Coordinates* is proved, the only quoted ingredient being the Plancherel theorem of *The Inverse Fourier Transform of a Symbol*. §*The Exponential on the Degenerate Set* quotes the three closed forms of *Biquaternion Elementary Functions*, §*The Closed Form*, with their hypotheses, and proves the corollary that follows. §*The Generalised Inverse* is proved, the existence of the Moore–Penrose inverse in a finite-dimensional inner-product space being standard and quoted as such. §*Inversion When the Symbol Is Nowhere a Unit* is proved for the two model families in which the symbol is a fixed null element times a scalar function, and the general case is labelled **open** there, with the specific obstacle named. **No part of the article is a programme**: where a statement is not proved, it says so.

**The equation.** Let $P(D)=\sum_{\lvert\alpha\rvert\le m}a_\alpha D^\alpha$ have constant coefficients in $\mathbb{B}$ and symbol $\sigma_P(\zeta)=\sum a_\alpha(i\zeta)^\alpha$, with $\zeta\in\mathbb{R}^n$ and $n$ the number of variables, as in *The Fourier Transform and the Symbol of a Differential Operator*. The equation to invert is

$$
P(D)f=g ,
$$

understood as an equation in $L^2(\mathbb{R}^n,\mathbb{B})$, with $P(D)$ the Fourier multiplier by $\sigma_P$. **The whole of the inversion is pointwise in $\zeta$**, so the biquaternion structure and the number of variables are separate questions: what follows holds for every $n$, and the one-variable kernel $W(t,\omega)$ of *Biquaternion Continuous Harmonic Analysis* is the case $n=1$.

**Boundaries.** The zero set $Z(P)$ and the determinant of the regular representation are *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*; the rank and the two annihilators on the null set are *The Biquaternion Fourier Transform: Support and Rank*; the placement of the kernel, which must be fixed before any formula is written, is *The Three Kernel Placements of the Biquaternion Fourier Transform*, and this article uses the **left** placement throughout; the two forms that measure an element are *The Biquaternion Fourier Transform and the Two Quadratic Forms*; the Peirce vocabulary is *Special Element and Peirce Conventions*; and the exponential is *Biquaternion Elementary Functions*.

## The Peirce Frame of the Algebra

### The Frame and Its Units

**Definition (the frame).** Put

$$
\tilde\Pi_1=\tfrac12\bigl(e_t+i\vec e_z\bigr),\qquad \tilde\Pi_2=\tfrac12\bigl(e_t-i\vec e_z\bigr),\qquad \vec\Upsilon_{12}=\tfrac12\bigl(i\vec e_x-\vec e_y\bigr),\qquad \vec\Upsilon_{21}=\tfrac12\bigl(i\vec e_x+\vec e_y\bigr).
$$

**The two mixed units are the $\vec\Upsilon_\pm$ of *Special Element and Peirce Conventions***, §*The Biquaternion Peirce Convention*, where the assignment of a sign to an index is not fixed. **The assignment above is the one that makes the matrix-unit identities hold**, and it is the reverse of the alphabetical reading: a computation, not a convention, checked below.

**Proposition (the four units are matrix units).** With $E_{11}=\tilde\Pi_1$, $E_{12}=\vec\Upsilon_{12}$, $E_{21}=\vec\Upsilon_{21}$ and $E_{22}=\tilde\Pi_2$,

$$
E_{ij}E_{jq}=E_{iq},\qquad E_{11}+E_{22}=e_t,\qquad \vec\Upsilon_{12}^{\ 2}=\vec\Upsilon_{21}^{\ 2}=0 .
$$

*Proof.* Each identity is a product of two elements written out in the four coordinates. The products reduce to the quaternion products of the units: $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$, with a minus sign on the reversed order, and $i$ central. For instance $\tilde\Pi_1\vec\Upsilon_{12}=\tfrac14(i\vec e_x-\vec e_y+i\vec e_z\vec e_x-i\vec e_z\vec e_y)=\tfrac14(i\vec e_x-\vec e_y+i\vec e_y+i\vec e_x)=\tfrac12(i\vec e_x-\vec e_y)=\vec\Upsilon_{12}$, and $\vec\Upsilon_{12}\vec\Upsilon_{21}=\tfrac14(i\vec e_x-\vec e_y)(i\vec e_x+\vec e_y)=\tfrac14(-\vec e_t-\vec e_z+\vec e_z+\vec e_t)$... the two cross terms cancel and the two diagonal terms give $-\tfrac14+\tfrac14$ on the vector part and $\tfrac14+\tfrac14$ on the scalar part, that is $\tfrac12(e_t+i\vec e_z)=\tilde\Pi_1$. The remaining identities are the same computation with the units permuted.

**Remark (what a wrong assignment costs, and why the determinant does not detect it).** With the other sign assignment each product comes out as half the expected unit, so the product rule fails by the factor two, while the determinant formula still holds, because a uniform rescaling of two units multiplies the determinant by a constant. **A check of the determinant alone therefore passes with the wrong frame**, and the eigenvalues read from it are wrong. Every identity above was checked one by one.

### Coordinates, the Product and the Norm

**Definition (Peirce coordinates).** For $Q\in\mathbb{B}$ the four complex numbers $\tilde Q_{ij}$ are defined by

$$
Q=\tilde Q_{11}\tilde\Pi_1+\tilde Q_{12}\vec\Upsilon_{12}+\tilde Q_{21}\vec\Upsilon_{21}+\tilde Q_{22}\tilde\Pi_2 ,
$$

and $\Sigma(Q)$ is the two-by-two complex matrix with entries $\tilde Q_{ij}$, the left index first.

**Theorem (the coordinates are a matrix representation).** The map $Q\mapsto\Sigma(Q)$ is an isomorphism of real algebras from $\mathbb{B}$ onto $M_2(\mathbb{C})$, and

$$
\Sigma(QR)=\Sigma(Q)\Sigma(R),\qquad \Sigma(Q^*)=\Sigma(Q)^{*},\qquad N(Q)=\det\Sigma(Q).
$$

Consequently the spectrum of $Q$ is the spectrum of $\Sigma(Q)$, and $Q$ is a unit exactly when $\Sigma(Q)$ is invertible.

*Proof.* The four units of §*The Frame and Its Units* are a basis: they are linearly independent by inspection of their coordinates, and $\mathbb{B}$ has real dimension eight, which is the real dimension of four complex parameters. On that basis the product rule $E_{ij}E_{jq}=E_{iq}$ is the matrix product rule, so the map is multiplicative; it is additive and real-linear by construction, and injective and surjective by the dimension count. For the star, $\tilde\Pi_i^*=\tilde\Pi_i$ because $\vec e_z$ is reversed twice by the two conjugations of the star, and $\vec\Upsilon_{12}^*=\vec\Upsilon_{21}$ by the same computation with one reversal; these are the conjugate-transpose relations of the four units, and multiplicativity extends them. For the determinant, $\det\Sigma=\tilde Q_{11}\tilde Q_{22}-\tilde Q_{12}\tilde Q_{21}$ is multiplicative and agrees with $N$ on the four units and on sums, and both are quadratic forms on the same eight real coordinates, so they agree everywhere.

**Remark (the matrix model of the earlier article is this matrix, read with the indices exchanged).** The model $\mathsf M(Q)=\begin{pmatrix}Q_t+iQ_z&Q_y+iQ_x\\-Q_y+iQ_x&Q_t-iQ_z\end{pmatrix}$ of *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set* sends $\tilde\Pi_1$ to $E_{22}$ and not to $E_{11}$. **The two matrices are similar, by the matrix that exchanges the two indices**, so the determinant and the spectrum agree and the individual entries do not. A statement about $N$ may be carried from one to the other without care; a statement about a coordinate, an eigenvector or a Peirce index may not.

### The Star, the Trace and the Hilbert–Schmidt Form

**Definition (the trace and the Hilbert–Schmidt form).** For $X,Y\in\mathbb{B}$ put $\mathrm{tr}\,X=\tilde X_{11}+\tilde X_{22}$ and $\langle X,Y\rangle_{\mathrm{HS}}=\mathrm{tr}(X^*Y)$, a positive definite Hermitian form on the eight real coordinates.

**Proposition (the trace is twice the scalar part, and the form is twice the coefficient norm).** For every $Q$,

$$
\mathrm{tr}\,Q=2Q_t,\qquad \langle Q,Q\rangle_{\mathrm{HS}}=\mathrm{tr}(Q^*Q)=2\lVert Q\rVert_E^2 ,
$$

where $\lVert Q\rVert_E^2=\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ is the coefficient norm.

*Proof.* The trace is the trace of the representing matrix, hence equal to the sum of its eigenvalues, and in the model of the remark above the two eigenvalues are $Q_t\pm iB$ with $B^2=Q_x^2+Q_y^2+Q_z^2$; their sum is $2Q_t$. For the form, $\mathrm{tr}(Q^*Q)$ is the sum of the absolute values of the four entries of the representing matrix, which is $\lvert Q_t+iQ_z\rvert^2+\lvert Q_y+iQ_x\rvert^2+\lvert-Q_y+iQ_x\rvert^2+\lvert Q_t-iQ_z\rvert^2$, and each pair contributes twice a modulus, giving $2\sum_\mu\lvert Q_\mu\rvert^2$.

**Remark (the two forms are not the same form).** The form $\langle\cdot,\cdot\rangle_{\mathrm{HS}}$ is positive definite; the algebraic norm $N$ is not, and is isotropic on the null set. **The factor two between the trace and the scalar part enters every formula below**, and a reader who replaces $\mathrm{tr}$ by the scalar part will be wrong by it in a way no homogeneous formula reveals.

## The Degenerate Set in Coordinates

### Rank One, and the Two Kinds of Null Element

**The degenerate set** is $Z=\{\zeta:N(\sigma(\zeta))=0\}$, the set where the symbol is not a unit, as in *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*. **In coordinates its definition is one determinant**, and the determinant of a two-by-two matrix has a normal form.

**Proposition (null means rank at most one).** For $\sigma\in\mathbb{B}$, $N(\sigma)=0$ exactly when $\Sigma(\sigma)$ has rank at most one; and for $\sigma\neq0$ the rank is exactly one, so that $\Sigma(\sigma)=uv^{\mathsf T}$ for a pair of nonzero columns $u,v\in\mathbb{C}^2$.

*Proof.* The determinant is the product of the eigenvalues, so it vanishes exactly when one eigenvalue vanishes, which for a two-by-two matrix is the rank-at-most-one condition; a nonzero matrix of rank at most one has rank one, and a rank-one matrix is the product of a column and a row by definition of rank.

**Theorem (the two halves of the degenerate set).** Let $\sigma\neq0$ with $N(\sigma)=0$. Then exactly one of the following holds.

- $\mathrm{tr}\,\sigma=2\sigma_t\neq0$, and $\sigma=(\mathrm{tr}\,\sigma)\,\tilde\Pi$ with $\tilde\Pi$ a nonzero idempotent.
- $\mathrm{tr}\,\sigma=2\sigma_t=0$, and $\sigma^2=0$: the element is nilpotent.

*Proof.* By Cayley–Hamilton for a two-by-two matrix, $\Sigma^2-(\mathrm{tr}\,\Sigma)\Sigma+(\det\Sigma)e_t=0$; and $\det\Sigma=N(\sigma)=0$, so $\Sigma^2=(\mathrm{tr}\,\Sigma)\Sigma$. If $\mathrm{tr}\,\Sigma\neq0$, the element $\Pi=\Sigma/\mathrm{tr}\,\Sigma$ satisfies $\Pi^2=\Pi$ and is nonzero because $\sigma\neq0$. If $\mathrm{tr}\,\Sigma=0$, the same display reads $\Sigma^2=0$, and a nonzero element whose second power vanishes is nilpotent and is not diagonalisable.

**Remark (this is the correct form of the two halves, and it is cut by the trace).** The degenerate set splits into the nonzero-trace half, where the element is a scalar multiple of an idempotent, and the zero-trace half, where it is nilpotent. **The cut is by $\sigma_t$, which is half the trace, and not by any idempotent.** The reason is structural and is stated in §*What the Central Idempotents Do and Do Not Give*. What the split does give is a complete answer to the question the inversion asks: on the first half the element has one eigenvalue that vanishes and one that does not, and on the second both eigenvalues vanish and the element has no eigenvector basis at all.

**Corollary (the idempotent half carries its projection).** If $\sigma=(\mathrm{tr}\,\sigma)\tilde\Pi$ with $\tilde\Pi^*=\tilde\Pi$, then $\sigma$ has eigenvalues $\mathrm{tr}\,\sigma$ and $0$, the projection onto the surviving part is $\tilde\Pi$, and $\sigma$ acts on $\mathbb{B}$ by left multiplication with image $\mathbb{B}\tilde\Pi$.

*Proof.* $\tilde\Pi^2=\tilde\Pi$ gives $\sigma\tilde\Pi=\sigma$ and $\sigma(e_t-\tilde\Pi)=0$, so the eigenvalues are as stated and the image is contained in $\mathbb{B}\tilde\Pi$; the image is exactly that ideal because $\sigma$ acts as the identity on it up to the scalar.

### The Two-Quaternion Reading

**Definition (the two quaternions of an element).** Write the four complex coordinates of $Q$ as $Q_\mu=a_\mu+ib_\mu$ with $a_\mu,b_\mu$ real, and put

$$
q_0=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z,\qquad q_1=b_te_t+b_x\vec e_x+b_y\vec e_y+b_z\vec e_z ,
$$

so that $Q=q_0+iq_1$ with $q_0,q_1\in\mathbb{H}$ and $i$ the central scalar imaginary.

**Proposition (the null condition links the two quaternions).** For $Q=q_0+iq_1$,

$$
N(Q)=\lvert q_0\rvert^2-\lvert q_1\rvert^2+2i\langle q_0,q_1\rangle ,
$$

where $\lvert\cdot\rvert$ is the quaternion norm and $\langle\cdot,\cdot\rangle$ the real inner product of the four coefficients. Hence $Q$ is null exactly when $\lvert q_0\rvert=\lvert q_1\rvert$ and $\langle q_0,q_1\rangle=0$; and then either $q_0=q_1=0$, or $q_0\neq0$ and $q_1=q_0r$ for a real pure unit quaternion $r$, so that

$$
Q=q_0\bigl(e_t+ir\bigr),\qquad r^2=-e_t .
$$

*Proof.* Expand $N(Q)=\sum_\mu(a_\mu+ib_\mu)^2$ into its real and imaginary parts: the real part is $\sum a_\mu^2-\sum b_\mu^2$ and the imaginary part is $2\sum a_\mu b_\mu$. The two vanishing conditions are the two equations of the display. If $q_0\neq0$ the second gives that $r=q_0^{-1}q_1$ has zero real part and norm one, since $\langle q_0,q_1\rangle=0$ and $\lvert q_1\rvert=\lvert q_0\rvert$; and $q_0=0$ forces $\lvert q_1\rvert=0$.

**Remark (what the reading does and does not say).** The two quaternions are **not independent**: the null condition is two real equations linking them, and it is the statement that one is obtained from the other by left multiplication by a pure unit. **Neither quaternion may vanish except at the origin**, since $q_0=0$ forces $Q=0$. The reading is nevertheless the right one for a computation, because it exhibits the real dimension of the degenerate set: four parameters in $q_0$ and two in $r$, hence six real dimensions in eight, the codimension two of *The Biquaternion Fourier Transform: Support and Rank*.

### What the Central Idempotents Do and Do Not Give

**Proposition (the algebra has no nontrivial central idempotent).** The only idempotents of $\mathbb{B}$ that commute with every element are $0$ and $e_t$.

*Proof.* A central idempotent generates a two-sided ideal, and a two-sided ideal of a full matrix algebra is $0$ or the whole algebra; the corresponding idempotent is then $0$ or $e_t$.

**Remark (where a split by central idempotents does exist, and why it is not this algebra).** A split into two algebras by central idempotents exists in the **split-biquaternion** layer, whose centre is the split-complex algebra $\mathbb{C}_{\mathrm{spl}}=\mathbb{R}[j]/(j^{2}-1)$: the two central idempotents $\tfrac12(e_t\pm j)$ split it as $\mathbb{H}\oplus\mathbb{H}$, by *Split-Biquaternion Algebra*, §*The Algebra Structure*, and each half is a quaternion algebra. There the null condition separates into one condition per half, and one half may vanish while the other does not. **Nothing of that kind is available in $\mathbb{B}$**, which is simple, and a statement about the two halves of a null biquaternion that invokes central idempotents has imported the split layer. The correct statements for $\mathbb{B}$ are the trace cut of §*Rank One, and the Two Kinds of Null Element* and the two-quaternion reading of §*The Two-Quaternion Reading*, and both are proved above.

## Inversion in Peirce Coordinates

### The Pointwise System

**The transform used here is the left placement**: the symbol acts by left multiplication, and $\widehat{P(D)f}=\sigma_P\hat f$ with the product in $\mathbb{B}$, as in *The Fourier Transform and the Symbol of a Differential Operator*. **The right placement transposes every statement below**, by *The Three Kernel Placements of the Biquaternion Fourier Transform*, and is not written out.

**Theorem (the equation is a family of two-by-two systems).** For $f,g\in L^2(\mathbb{R}^n,\mathbb{B})$ the equation $P(D)f=g$ holds exactly when

$$
\Sigma\bigl(\sigma_P(\zeta)\bigr)\,\Sigma\bigl(\hat f(\zeta)\bigr)=\Sigma\bigl(\hat g(\zeta)\bigr)
$$

for almost every $\zeta$, where the product is the matrix product.

*Proof.* The transform is an isometry onto $L^2$ by Plancherel for $\mathbb{B}$-valued functions, quoted from *The Inverse Fourier Transform of a Symbol* with its constant; it intertwines $P(D)$ with the multiplier $\sigma_P$; the coordinates are a multiplicative isomorphism by §*Coordinates, the Product and the Norm*; and a matrix equation holds exactly when its four entries do. **All four statements are pointwise in $\zeta$**, so the equation is equivalent to the displayed system at each frequency separately.

**Corollary (the degenerate set is four real equations at each of its points).** At a frequency where $\sigma_P(\zeta)$ is null and nonzero, the range of the pointwise operator has real dimension four in eight, so the system is solvable exactly on a real four-dimensional subspace of the eight coordinates of $\hat g(\zeta)$.

*Proof.* The rank of left multiplication by a nonzero null element is four, by *The Biquaternion Fourier Transform: Support and Rank*; the range is the image, of real dimension four; and a linear system is solvable exactly on the image.

### The Adjugate Off the Degenerate Set

**Theorem (the inverse is the adjugate).** Let $\sigma$ be a unit, with coordinate matrix $\Sigma=\begin{pmatrix}\tilde\sigma_{11}&\tilde\sigma_{12}\\ \tilde\sigma_{21}&\tilde\sigma_{22}\end{pmatrix}$ and determinant $N(\sigma)$. Then

$$
\sigma^{-1}=\frac{1}{N(\sigma)}\Bigl(\tilde\sigma_{22}\tilde\Pi_1-\tilde\sigma_{12}\vec\Upsilon_{12}-\tilde\sigma_{21}\vec\Upsilon_{21}+\tilde\sigma_{11}\tilde\Pi_2\Bigr).
$$

*Proof.* The inverse of a two-by-two matrix is the adjugate divided by the determinant, and the coordinates are multiplicative; the adjugate has entries $\tilde\sigma_{22},-\tilde\sigma_{12},-\tilde\sigma_{21},\tilde\sigma_{11}$ in the order of the four units, and the display is that matrix written in the algebra.

**Corollary (the inverse is rational in the frequency, with denominator $N(\sigma)$).** The inverse symbol is a quotient of a polynomial of degree at most $m$ in $\zeta$ by the determinant of degree $dm$, and the inversion off the degenerate set is

$$
f=\mathcal F^{-1}\bigl[\sigma^{-1}\hat g\bigr],\qquad f(x)=\int e^{i\zeta\cdot x}\,\sigma(\zeta)^{-1}\hat g(\zeta)\,d\zeta .
$$

*Proof.* $\sigma_P$ is a polynomial of degree $m$ in $\zeta$ with coefficients in $\mathbb{B}$; $N(\sigma_P)$ is a polynomial of degree $dm$ by *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, which computes the degree; the adjugate has entries that are polynomials of degree at most $m$; and the inversion formula is that of *The Fourier Transform and the Symbol of a Differential Operator* applied to the multiplier $\sigma^{-1}$, valid under the integrability of $\sigma^{-1}\hat g$.

**Remark (the degree is not the pole order, and the two are confused in print).** The determinant has degree $dm$ and the inverse has a pole where the determinant vanishes, but **the order of the pole is the multiplicity of the factor and not the degree of the determinant**; that distinction is the subject of *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails* and is not repeated here. What the adjugate adds is the numerator: at a null point of $\sigma$ the adjugate does not vanish, so the pole of the inverse is of the same order as the zero of $N(\sigma)$, and not higher.

### Solvability and the Minimal-Norm Solution

**Theorem (what the degenerate set costs).** Let $\sigma_P$ be the symbol of $P(D)$ and suppose $N(\sigma_P)$ is not identically zero. Then $Z$ has Lebesgue measure zero, and for every $g\in L^2$ there is an $f\in L^2$ with $P(D)f=g$. The solution is not unique, the ambiguity at each point of $Z$ being the four real dimensions of the kernel of left multiplication by $\sigma_P(\zeta)$, and the solution of least norm is

$$
\hat f(\zeta)=\sigma_P(\zeta)^{+}\,\hat g(\zeta),\qquad f=\mathcal F^{-1}\bigl[\sigma_P^{+}\hat g\bigr],
$$

where $\sigma^+$ is the Moore–Penrose inverse of the element, computed in §*The Formulas on the Degenerate Set*.

*Proof.* $N(\sigma_P)$ is a polynomial, real-analytic; if it is not identically zero its zero set has empty interior and measure zero. Off $Z$ the symbol is a unit and $\hat f=\sigma^{-1}\hat g$ solves the equation; on $Z$, a set of measure zero, define $\hat f$ to be zero. The resulting function is in $L^2$, so a solution exists for every $g$. At a point of $Z$ the solutions of the pointwise system differ by the kernel, of real dimension four, and the least-norm choice is the Moore–Penrose solution, which is characterised by lying in the orthogonal complement of the kernel.

**Remark (the degenerate set obstructs uniqueness and boundedness, not existence).** This is the point at which the phrase "inversion on the degenerate set" is usually misread. **A set of measure zero cannot obstruct the solvability of an $L^2$ equation**, because the values of $\hat f$ on it are irrelevant to the norm and to the transform. What the set does obstruct is the uniqueness of the solution and the boundedness of the inverse: $\sigma^{+}$ is bounded exactly when $\sigma$ is bounded away from zero, that is, when $\inf_\zeta\lVert\sigma(\zeta)\rVert>0$, which for a symbol of positive order fails at the origin and at every zero of $\sigma$. The genuine obstruction is the case $N(\sigma_P)\equiv0$, treated in §*Inversion When the Symbol Is Nowhere a Unit*.

**Remark (the adjugate and the Moore–Penrose inverse agree off the degenerate set).** Where $\sigma$ is a unit the two formulas coincide, since $\sigma^{+}=\sigma^{-1}$ there; the two differ only on $Z$, where the adjugate formula has no meaning and the generalised inverse is the only one available. **The inversion is therefore continuous in the symbol away from $Z$**, across which the algebraic inverse blows up and the generalised inverse does not.

## The Exponential on the Degenerate Set

### The Three Cases of the Closed Form

**The three closed forms are quoted, not proved here.** They are those of *Biquaternion Elementary Functions*, §*The Closed Form*, with the hypothesis that $\mathbb{C}[S]$ be the span of $e_t$ and a single element, that is, that $S$ be one biquaternion; and they read, with $B^2=S_x^2+S_y^2+S_z^2$ and $\vec U=\vec S/B$,

$$
\exp S=\begin{cases}\exp(S_t)\bigl(\cos B\,e_t+\sin B\,\vec U\bigr), & B^2\neq0,\\[2pt] \exp(S_t)\bigl(e_t+\vec S\bigr), & B^2=0,\ \vec S\neq0,\\[2pt] \exp(S_t)\,e_t, & \vec S=0.\end{cases}
$$

**Proposition (each closed form is a unit).** In all three cases $N(\exp S)=\exp(2S_t)$, which is never zero.

*Proof.* The norm is multiplicative, so $N(\exp S)=\exp(2S_t)N(\exp\vec S)$, and it remains to compute the second factor. In the first case $N(\vec U)=-1$ for a pure unit and the closed form gives $\cos^{2}B+\sin^{2}B=1$. In the second case $\vec S^{2}=0$ and $N(e_t+\vec S)=(e_t+\vec S)(e_t-\vec S)=e_t-\vec S^{2}=e_t$, the conjugate of a pure element being its negative. In the third case the factor is $N(e_t)=1$.

### Why No Nonzero Null Element Is an Exponential

**Theorem (the degenerate set is outside the image of the exponential).** Let $\sigma\neq0$ with $N(\sigma)=0$. Then there is no $S\in\mathbb{B}$ with $\exp S=\sigma$.

*Proof.* The image of the exponential is the group of units, a statement of *Biquaternion Elementary Functions* whose hypothesis is that the element be a biquaternion and whose proof is the surjectivity of the logarithm onto the units; a nonzero null element is not a unit, by the definition of the null set as the complement of the units; so it is not in the image. **The three cases of §*The Three Cases of the Closed Form* give the same conclusion a second way**, and the second way is the informative one: each closed form is a unit, so no value of the closed form can be null.

**Corollary (the route through the exponential closes exactly on the degenerate set).** The inverse kernel of the transform is an exponential because the frequency enters it through a unit, and the inversion of *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails* is a residue calculus in the variable that carries that exponential. **At a point where the symbol is not a unit there is no exponential to take a residue of**, and the calculus has no object to act on. This is not a defect of that article; it is the reason the present one works in coordinates instead.

**Remark (how the three cases sit on the degenerate set, and why none of them reaches it).** The three cases are cut by $B^2$, not by the norm, and their intersections with $Z\setminus\{0\}$ are as follows.

| Case of the closed form | Condition | Intersection with the null set | Why the closed form misses it |
|---|---|---|---|
| $B^2\neq0$ | the vector part is not isotropic | $\sigma=2\sigma_t\tilde\Pi$, one eigenvalue $0$ | $\exp$ of it has eigenvalues $\exp(2\sigma_t)$ and $1$, neither zero |
| $B^2=0$, $\vec S\neq0$ | the vector part is isotropic and nonzero | $\sigma_t=0$, so $\sigma$ is nilpotent | $\exp$ of a nilpotent is unipotent, hence a unit |
| $\vec S=0$ | the element is central | $\sigma=0$ only | the scalar exponential never vanishes |

**Corollary (nilpotence is invisible to the exponential).** For $\vec S\neq0$ with $\vec S^2=0$ and $S_t=0$, the element is nilpotent and $\exp S=e_t+\vec S$ is unipotent: it is a unit, and it is the identity plus the nilpotent. **The exponential therefore maps the nilpotent ray to a line of units and never returns to the null set**, which is the exact sense in which the exponential parametrisation cannot reach the degenerate half on which the inversion has to be done.

## The Generalised Inverse

### Three Inverses and Their Axioms

**Definition (the Moore–Penrose inverse).** For a linear map between finite-dimensional inner-product spaces the **Moore–Penrose inverse** is the unique map $T^{+}$ satisfying the four Penrose equations

$$
TT^{+}T=T,\qquad T^{+}TT^{+}=T^{+},\qquad (TT^{+})^{*}=TT^{+},\qquad (T^{+}T)^{*}=T^{+}T ,
$$

and its existence and uniqueness in that setting are standard and quoted as such.

**Definition (the Drazin inverse).** For a two-by-two matrix $T$ the **Drazin inverse** is the unique matrix $T^{D}$ commuting with $T$ with $T^{D}TT^{D}=T^{D}$ and $T^{k+1}T^{D}=T^{k}$ for all $k$ at least the index of $T$, the index being the least $k$ with $\operatorname{rank}T^{k+1}=\operatorname{rank}T^{k}$.

**Remark (the two inverses answer different questions, and the difference is the star).** The Moore–Penrose inverse uses the star and the inner product, so it is the answer to the least-norm question; the Drazin inverse uses only the product, so it is the answer to the algebraic question, and it is a polynomial in $T$. **On the degenerate set the two diverge**, and they diverge in a way that §*Which Inverse Belongs to Which Question* turns into a statement about the inversion.

### The Formulas on the Degenerate Set

**Theorem (the Moore–Penrose inverse of a null element).** Let $\sigma\neq0$ with $N(\sigma)=0$. Then

$$
\sigma^{+}=\frac{\sigma^{*}}{\mathrm{tr}(\sigma\sigma^{*})}=\frac{\sigma^{*}}{2\lVert\sigma\rVert_E^{2}} .
$$

*Proof.* In coordinates $\Sigma=uv^{\mathsf T}$ is of rank one by §*Rank One, and the Two Kinds of Null Element*, and $\Sigma^{*}=\bar vu^{*}$. Then $\Sigma\Sigma^{*}\Sigma=\lVert u\rVert^{2}\lVert v\rVert^{2}\Sigma=\mathrm{tr}(\Sigma^{*}\Sigma)\Sigma$ and $\Sigma^{*}\Sigma\Sigma^{*}=\mathrm{tr}(\Sigma^{*}\Sigma)\Sigma^{*}$, because the two scalar factors are the same; dividing by that trace gives the first Penrose equation and the second, and the products $\Sigma\Sigma^{*}$ and $\Sigma^{*}\Sigma$ are Hermitian after the division, which gives the third and the fourth. **The four equations hold in the algebra and not merely on the operator**, since the coordinates are multiplicative. The trace is computed by §*The Star, the Trace and the Hilbert–Schmidt Form*.

**Corollary (the two halves in closed form).** On the idempotent half, with $\sigma=c\tilde\Pi$ and $\tilde\Pi=\tilde\Pi^{*}$ an idempotent and $c\in\mathbb{C}^{\times}$, $\sigma^{+}=c^{-1}\tilde\Pi$. On the nilpotent half $\sigma^{+}=\sigma^{*}/\lVert\sigma\rVert_{\mathrm{HS}}^{2}$.

*Proof.* For the idempotent half, $\sigma\sigma^{*}=\lvert c\rvert^{2}\tilde\Pi$, whose trace is $\lvert c\rvert^{2}$ because a rank-one Hermitian idempotent has trace one; the formula then gives $\sigma^{*}/\lvert c\rvert^{2}=\bar c\tilde\Pi/\lvert c\rvert^{2}=c^{-1}\tilde\Pi$. On the nilpotent half the trace is the Hilbert–Schmidt norm of the element, and nothing cancels.

**Remark (the idempotent must be Hermitian, and this is not a formality).** For a **non-Hermitian** idempotent the formula gives $\tilde\Pi^{*}/\mathrm{tr}(\tilde\Pi\tilde\Pi^{*})$, which is not $\tilde\Pi$; the Moore–Penrose inverse of an oblique projection is not the projection. **The pair $\tilde\Pi_1,\tilde\Pi_2$ of the frame is Hermitian and the mixed units are exchanged by the star**, so the two objects that occur in the frame are of the good kind; a computation that uses an arbitrary idempotent read off a symbol is not.

**Theorem (the Drazin inverse on the two halves).** On the idempotent half, with $\sigma=c\tilde\Pi$ and $\tilde\Pi^2=\tilde\Pi$ and $c\neq0$, $\sigma^{D}=c^{-1}\tilde\Pi$; on the nilpotent half $\sigma^{D}=0$.

*Proof.* For the idempotent half, $\sigma\sigma^{D}=\tilde\Pi=\sigma^{D}\sigma$ and $\sigma^{2}\sigma^{D}=\sigma$, so the index is one and the defining equations hold. For the nilpotent half, $\sigma^{2}=0$ and the index is two; the third requirement at $k=2$ reads $0=\sigma^{2}$, which holds, and at $k=1$ reads $0=\sigma$, which forces $\sigma^{D}=0$ because $\sigma^{D}$ commutes with $\sigma$ and $\sigma\sigma^{D}\sigma=\sigma$ would give $\sigma=0$.

### Which Inverse Belongs to Which Question

**Theorem (the two inverses agree on the idempotent half and differ on the nilpotent half).** For $\sigma=c\tilde\Pi$ with $\tilde\Pi$ Hermitian and $c\neq0$, $\sigma^{+}=\sigma^{D}=\tilde\Pi/c$. For $\sigma$ nilpotent and nonzero, $\sigma^{+}=\sigma^{*}/2\lVert\sigma\rVert_E^{2}\neq0$ while $\sigma^{D}=0$.

*Proof.* The first statement is the two corollaries above. For the second, $\sigma^{+}$ is a nonzero multiple of $\sigma^{*}$, which is nonzero, and $\sigma^{D}=0$; so the two differ, and they differ by the whole of the nilpotent direction.

**Corollary (which to use for the inversion).** The Moore–Penrose inverse is the one that selects the solution of least norm, so it is the one that gives an inversion bounded by $\lVert\sigma^{+}\rVert$ and preserves the $L^2$ estimate of §*Solvability and the Minimal-Norm Solution*. The Drazin inverse is the one that commutes with $\sigma$ and is therefore the one for which the inverted multiplier is again a function of the symbol alone, with no conjugate and no reflection of the frequency.

**Remark (the reflection is not a defect).** The star of an element is not a function of the element alone, and in the frequency variable it reflects the argument, because the star of $P(D)$ is $P(-D)$ with conjugated coefficients. **A Drazin inversion avoids that reflection at the price of killing the nilpotent direction**, so the choice is a choice of purpose: a least-norm solution, or a multiplier algebraic in the symbol.

## Inversion When the Symbol Is Nowhere a Unit

### The Two Model Families

**The case that is genuinely obstructed is $N(\sigma_P)\equiv0$.** Then the symbol is null at every frequency and the pointwise system is singular everywhere; the set is no longer of measure zero, and the range is a proper subspace at every point.

**Theorem (a fixed null coefficient).** Let $S\neq0$ be null and let $\sigma_P(\zeta)=\rho(\zeta)S$ with $\rho$ a scalar polynomial that vanishes only at $\zeta=0$. Then $P(D)f=g$ has a solution exactly when

$$
SS^{+}g=g ,
$$

that is, exactly when $g(x)$ lies in the fixed real subspace $\mathrm{im}L_S$ for almost every $x$; and the solution of least norm is $f=\mathcal F^{-1}\bigl[\rho^{+}S^{+}\hat g\bigr]$.

*Proof.* The pointwise system reads $\rho(\zeta)\Sigma(S)\hat F=\hat G$. For $\zeta\neq0$ the scalar is nonzero, so solvability is $\hat G\in\mathrm{im}L_{\Sigma(S)}$, which is equivalent to $\Sigma(S)\Sigma(S)^{+}\hat G=\hat G$ because the latter is the orthogonal projection onto the image. Both sides are constant in $\zeta$ except through $\hat G$, so the condition is a condition on $g$ alone, and it is exactly $SS^{+}g=g$. The least-norm solution at each frequency is $\rho^{+}\Sigma(S)^{+}\hat G$, and $\rho^{+}$ is $1/\rho$ off the origin and $0$ at the origin.

**Example (the nilpotent family).** Let $N_0=\vec e_x+i\vec e_y$, which is nilpotent, and $P(D)=N_0\Delta$. Its symbol is $\sigma_P(\zeta)=-\lvert\zeta\rvert^{2}N_0$, and $N(\sigma_P)=-\lvert\zeta\rvert^{2}N(N_0)=0$ at every $\zeta$. In coordinates $N_0$ is the matrix with a single entry, so $\mathrm{im}L_{N_0}$ is the set of matrices whose columns lie in one fixed complex line, a real four-dimensional subspace; and the solvability condition $N_0N_0^{+}g=g$ reads $N_0^{*}g=0$ because $N_0^{+}$ is a nonzero multiple of $N_0^{*}$.

$$
N_0=\vec e_x+i\vec e_y,\qquad N_0^{2}=0,\qquad P(D)f=N_0\,\Delta f .
$$

**Example (the idempotent family).** Let $P(D)=\tilde\Pi_1\Delta$. Its symbol is $-\lvert\zeta\rvert^{2}\tilde\Pi_1$, null at every frequency, and the solvability condition is $\tilde\Pi_1 g=g$: **the data must take values in the left ideal $\mathbb{B}\tilde\Pi_1$ at every point**. The solution of least norm is $f=-\Delta^{-1}\tilde\Pi_1 g$, and the whole of the inversion is the ordinary Laplacian inversion followed by a projection.

**Remark (the two conditions are one condition).** In both families the condition is $SS^{+}g=g$, and the two differ only in what the projection is: $N_0N_0^{+}$ projects onto a minimal left ideal reached through a nilpotent, and $\tilde\Pi_1$ projects onto a minimal left ideal reached through an idempotent. **The trace cut of §*Rank One, and the Two Kinds of Null Element* is therefore visible in the inversion as the difference between a projection $PP^{*}$ and a projection $P$**, which is the same difference as the one between the two generalised inverses of §*Which Inverse Belongs to Which Question*.

### What Remains Open

**The open case, stated precisely.** Let $\sigma_P$ be a polynomial symbol with $N(\sigma_P)\equiv0$ and with the null element $\sigma_P(\zeta)$ **not** of the form $\rho(\zeta)S$ for a fixed null $S$. Then the range at each frequency is a four-dimensional subspace depending on $\zeta$, and the solvability condition is that $\hat g(\zeta)$ lie in that subspace for almost every $\zeta$. **The following are open here and are labelled as such.**

- Whether the pointwise conditions are simultaneously satisfiable by the transform of a single function, that is, whether the range of $P(D)$ is closed in $L^2$.
- Whether the spectral projection onto the range varies measurably in $\zeta$ and whether the resulting family defines a bounded projection on $L^2$.
- The description of the kernel of $P(D)$ when the null element varies, which is infinite-dimensional in the two model families and is not described in general.

**Remark (why the constant-coefficient case is not a formality).** In the two model families the projection is constant, so the pointwise conditions assemble into one condition on $g$ and the inversion reduces to a scalar operator after a fixed projection. **When the null element varies, so does the projection, and a family of projections that does not commute with the multiplier need not integrate to a projection on $L^2$**; that is the obstacle, not a gap in technique.

**Remark (what the frame does and does not settle).** Every statement about a single frequency becomes two-by-two linear algebra, settled completely above. **It does not turn a family of frequencies into one matrix problem**: the coordinates of $\sigma_P(\zeta)$ vary with $\zeta$, and the projectors $SS^{+}$ at the null points need not be the coordinate projectors of the frame. The frame serves the pointwise algebra; it is not a diagonalisation of the operator.

## Summary

The Peirce frame of the pair $\tilde\Pi_1,\tilde\Pi_2$ turns the biquaternion algebra into the two-by-two complex matrices: the four units multiply as matrix units, the coordinates are multiplicative, the star is the conjugate transpose, the trace is twice the scalar part, and the algebraic norm is the determinant. **In that frame the whole of the pointwise inversion is two-by-two linear algebra.**

The degenerate set is the zero set of the determinant, and on it a nonzero symbol has rank one. It splits by the trace into two halves: a nonzero-trace element is a scalar multiple of an idempotent, with one eigenvalue zero and one not, and a zero-trace element is nilpotent, with both eigenvalues zero. **The split is cut by the scalar part, which is half the trace, and by nothing else**; the algebra has no nontrivial central idempotent, and a split into two quaternion halves belongs to the split-biquaternion layer. The two-quaternion reading gives the same set in another form: $Q=q_0+iq_1$ is null exactly when $q_1=q_0r$ with $r$ a real pure unit.

Off the degenerate set the inverse is the adjugate divided by the determinant, and the inversion is the Fourier integral of the inverse symbol. On it the Moore–Penrose inverse is $\sigma^{*}/\mathrm{tr}(\sigma\sigma^{*})$, one formula covering both halves, reducing to $\tilde\Pi/c$ on the Hermitian idempotent half and to the normalised conjugate on the nilpotent half. **When the determinant is not identically zero the degenerate set obstructs uniqueness and boundedness but not existence**, because it has measure zero; the least-norm solution is the generalised-inverse one, and the algebraic inverse blows up there while the generalised inverse stays bounded.

The route through the exponential closes before it reaches the set. Each of the three closed forms produces a unit, so no nonzero null element is an exponential of anything, and a residue calculus has no object at a null frequency. **That holds in all three cases at once, and it is why the inversion is done in coordinates.**

When the determinant vanishes identically the obstruction is real: the range is proper at every frequency, the solvability condition is $SS^{+}g=g$, and the inversion is a scalar inversion after a fixed projection. That is proved for the two families in which the null element is fixed up to a scalar; the case of a null element varying with the frequency is open, with the failure of the pointwise projections to integrate named as the obstacle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of real dimension $8$ |
| $e_t$ | The scalar unit |
| $\vec e_x,\vec e_y,\vec e_z$ | The three vector units, each with second power $-e_t$ |
| $i$ | The central scalar imaginary |
| $\tilde\Pi_1,\tilde\Pi_2$ | The complete pair $\tfrac12(e_t\pm i\vec e_z)$, Hermitian idempotents |
| $\vec\Upsilon_{12},\vec\Upsilon_{21}$ | The mixed units $\tfrac12(i\vec e_x\mp\vec e_y)$, nilpotent |
| $E_{ij}$ | The four units, a Peirce basis of $\mathbb{B}$ |
| $\tilde Q_{ij}$ | A Peirce coordinate of $Q$, left index first |
| $\Sigma(Q)$ | The coordinate matrix with entries $\tilde Q_{ij}$ |
| $u,v$ | The two columns of a rank-one coordinate matrix |
| $\star$, $Q^{*}$ | The star of the algebra, quaternion conjugation followed by complex conjugation |
| $\mathrm{tr}$ | The matrix trace, equal to $2Q_t$ |
| $\langle\cdot,\cdot\rangle_{\mathrm{HS}}$ | The Hilbert–Schmidt form $\mathrm{tr}(X^{*}Y)$ |
| $\lVert\cdot\rVert_E$ | The coefficient norm on the eight real coordinates |
| $\lVert\cdot\rVert_{\mathrm{HS}}$ | The norm of the Hilbert–Schmidt form |
| $N$ | The algebraic norm, equal to $\det\Sigma$ |
| $q_0,q_1$ | The two real quaternions of $Q=q_0+iq_1$ |
| $r$ | A real pure unit quaternion, $r^2=-e_t$ |
| $j$ | The split central unit with $j^{2}=e_t$, used once in a boundary remark |
| $\mathbb{B}_{\mathrm{spl}}$ | The split-biquaternion algebra, mentioned only as a boundary |
| $P(D)$ | A constant-coefficient differential operator with coefficients in $\mathbb{B}$ |
| $\Delta$ | The Laplacian, used as the scalar factor of the two model families |
| $\sigma_P$, $\sigma$ | Its symbol, $\sum a_\alpha(i\zeta)^\alpha$ |
| $m$ | The total order of $P(D)$ |
| $d$ | The real dimension of the algebra, $8$ for $\mathbb{B}$ |
| $\zeta$ | The frequency, in $\mathbb{R}^n$ |
| $\omega$ | The real frequency in one variable, used once for the kernel $W(t,\omega)$ |
| $n$ | The number of variables |
| $Z$ | The degenerate set, $\{\zeta:N(\sigma_P(\zeta))=0\}$ |
| $f,g$ | The unknown and the data, $L^2$ functions with values in $\mathbb{B}$ |
| $\hat f,\hat g$ | Their transforms |
| $\mathcal F$, $\mathcal F^{-1}$ | The biquaternion Fourier transform and its inverse, left placement |
| $L_\sigma$ | Left multiplication by $\sigma$ |
| $\sigma^{+}$ | The Moore–Penrose inverse of the element $\sigma$ |
| $\sigma^{D}$ | The Drazin inverse of the element $\sigma$ |
| $T^{+}$, $T^{D}$ | The Moore–Penrose and Drazin inverses of a linear map or a matrix |
| $S$, $N_0$ | A fixed nonzero null element used as a model coefficient |
| $\rho$ | A scalar polynomial multiplier in the model families |
| $B$ | The value with $B^2=S_x^2+S_y^2+S_z^2$ |
| $\vec U$ | The axis $\vec S/B$ when $B^2\neq0$ |
| $\mathbb{H}$ | The real quaternion algebra |
| $\lvert\cdot\rvert$ | The quaternion norm on $q_0$ and $q_1$, and the modulus of a complex frequency |
| $\langle q_0,q_1\rangle$ | The real inner product of the coefficients of two quaternions |

## Further Reading

- *The Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, for the symbol, the block form of left multiplication and the determinant whose zero set is inverted here.
- *The Biquaternion Fourier Transform: Support and Rank*, for the rank four on the null set, the two annihilators, and the codimension of the cone; the present article uses those numbers and does not recompute them.
- *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*, for the residue inversion in a plane of the root, which is the route that closes at the degenerate set.
- *Biquaternion Elementary Functions*, for the three closed forms of the exponential and for the image of the exponential, both quoted here with hypotheses.
- *Special Element and Peirce Conventions*, for the Peirce vocabulary, the case rule of the layer, and the two mixed units whose index assignment is fixed here by computation.
- *The Biquaternion Fourier Transform and the Two Quadratic Forms*, for the positive definite form and the isotropic norm, and for why the two must not be identified; the trace form of §*The Star, the Trace and the Hilbert–Schmidt Form* is the form of that article up to the constant computed here.
- *The Three Kernel Placements of the Biquaternion Fourier Transform*, for the placement of the kernel, which is fixed to the left here and which transposes every formula of §*Inversion in Peirce Coordinates*.
- *The Inverse Fourier Transform of a Symbol*, for Plancherel with its constant, used once and quoted.
- *The Fourier Transform and the Symbol of a Differential Operator*, for the correspondence between the operator and its symbol, and for the inversion formula off the degenerate set.
