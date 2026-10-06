# __The Split-Complex Iterated Function Systems__

## Introduction

An iterated function system on the split-complex plane is a finite family of **split-complex similarities** $S_i(z) = u_i z + v_i$ with $u_i$ a unit of $\mathbb{D}$; its attractor is the invariant compact set of the family. The algebra carries the indefinite form $N(z) = a^2-a'^2$, and this changes the kinematics: a map preserving $N$ is a hyperbolic rotation or a hyperbolic scaling and is **expanding** in the ordinary Euclidean metric, so a system whose contractions are read in $N$ has no attractor in the usual sense; the contractions must be read in the Euclidean coordinates. In those coordinates a split-complex similarity is anisotropic, contracting the two coordinate directions by the singular values $|u_{i+}|$ and $|u_{i-}|$; each coordinate runs a one-dimensional real system, but the **same word** drives both, so the attractor is the image of a single shift space and it is **not** the product of the two real attractors — that product governs a mixed system with one map for each pairing. This article develops the kinematics, the attractor theorem and the dimension formula for these systems, describes the trace of the null cone on the attractor, identifies the symmetry that survives — the conjugation — and compares the construction with the complex systems of *Iterated Function Systems in the Complex Plane*.

The article is the $\mathbb{D}$ instance of the self-similar theory. The general definitions — the attractor and the Hutchinson operator, the open set condition, the similarity dimension — are those of *Fractal Geometry*, the lead article of the subcategory; the product construction and the real self-similar sets in one dimension are those of the same article and of *Fractal Analysis* of Part III; the algebra, the norm and the null cone are those of *Split-Complex Norm and Invertibility* and *Split-Complex Null Quadric and Projective Geometry*; the hyperbolic rotations are those of *Hyperbolic Rotations*; and the Julia sets that the systems approximate are those of *The Split-Complex Julia Sets* and *The Hyperbolic Geometry of the Split-Complex Julia Sets*. No physics is invoked.

## The Similarities and the Contractions

### The Matrix and the Singular Values

**Definition.** A **split-complex similarity** is a map $S(z) = uz+v$ with $u, v \in \mathbb{D}$ and $u$ a unit. Its **singular values** are the two numbers $|u_+|$ and $|u_-|$ obtained from the idempotent coordinates of $u$, and its **Euclidean contraction factor** is $\max\{|u_+|,|u_-|\}$.

**Theorem.** In the basis $\{1,j\}$ the linear part $z \mapsto uz$ of the similarity has the matrix

$$
[u] = \begin{pmatrix} p & q \\ q & p \end{pmatrix}, \qquad u = p+jq ,
$$

of which the eigenvalues are $u_+ = p+q$ and $u_- = p-q$ with eigenvectors $\Pi_+$ and $\Pi_-$, and the singular values $|u_+|, |u_-|$. The map $S$ is a Euclidean contraction exactly when

$$
\max\{|u_+|, |u_-|\} < 1 ,
$$

that is, exactly when both idempotent coordinates of $u$ lie in $(-1,1)$; the determinant of the linear part is $u_+u_- = N(u)$.

**Proof.** The matrix of multiplication by $p+jq$ is read off from $(p+jq)(1) = p+jq$ and $(p+jq)(j) = q+pj$; it is symmetric with trace $2p$ and determinant $p^2-q^2 = N(u)$, and its eigenvalues are $p\pm q$ with the eigenvectors $\Pi_\pm$. A symmetric matrix has the singular values equal to the absolute values of the eigenvalues, and the Euclidean operator norm is the largest singular value. The contraction condition follows.

### The Contraction Must Be Euclidean

**Theorem (the $N$-preserving maps do not contract).** A similarity preserving the form $N$ up to sign has $|N(u)| = 1$, equivalently $|u_+u_-| = 1$, and then

$$
\max\{|u_+|,|u_-|\} \geq 1 ,
$$

with equality exactly for $u \in \{\pm1,\pm j\}$. Hence no $N$-preserving split-complex similarity is a Euclidean contraction, and a system whose "contraction" is measured by $N$ has no attractor in the sense of the Hutchinson theory: the orbits of such a map do not converge in the Euclidean metric.

**Proof.** $N(u) = u_+u_-$ and $|N(u)| = 1$ give $|u_+|\,|u_-| = 1$, so both coordinates are nonzero and $\max\{|u_+|,|u_-|\} \geq 1$ by the inequality of the geometric and the arithmetic mean. Equality $\max = 1$ forces $|u_+| = |u_-| = 1$, hence $u_+ = \pm1$, $u_- = \pm1$ and $u \in \{\pm1, \pm j\}$; these four maps are Euclidean isometries (the identity, the central symmetry and the two reflections in the null lines), so they are not contractions either. Consequently every $N$-preserving similarity has Euclidean contraction factor at least one, and the only contractive members of the $N$-preserving family are excluded from an iterated function system.

**Remark (the consequence for the systems).** The systems of this article therefore take their contractions from the Euclidean structure, not from the form $N$: a similarity is admitted when $\max\{|u_+|,|u_-|\} < 1$, and then the two coordinate directions are contracted by the potentially different factors $|u_+|$ and $|u_-|$. The map is anisotropic: it is a genuine Euclidean similarity only when $|u_+| = |u_-|$, which is the case $u = p$ real, and it is a hyperbolic (Lorentz) boost in the other extreme. This is the sense in which the contraction is read in the Euclidean coordinates.

## The Attractor and the Coding

**Definition.** An **iterated function system of split-complex similarities** is a finite family $\mathcal{S} = \{S_1, \ldots, S_m\}$, $m \geq 2$, of similarities $S_i(z) = u_i z + v_i$ with $\max\{|u_{i+}|,|u_{i-}|\} < 1$ for every $i$. Its **attractor** is the unique nonempty compact set $\Lambda \subseteq \mathbb{D}$ with $\Lambda = \bigcup_i S_i(\Lambda)$.

**Theorem (the attractor and the coding map).** For every such system the attractor exists and is unique. The **coding map**
$$
\tau(\omega) = \lim_{n\to\infty} S_{\omega_1}\circ\cdots\circ S_{\omega_n}(z_0), \qquad \omega = (\omega_1,\omega_2,\ldots) \in \{1,\ldots,m\}^{\mathbb{N}} ,
$$
is well defined and independent of $z_0$, and $\Lambda = \tau\bigl(\{1,\ldots,m\}^{\mathbb{N}}\bigr)$. In the idempotent coordinates
$$
\varphi\bigl(\tau(\omega)\bigr) = \bigl(\tau_+(\omega),\ \tau_-(\omega)\bigr) ,
$$
where $\tau_\pm$ is the coding map of the one-dimensional system $\{x \mapsto u_{i\pm} x + v_{i\pm}\}$ on $\mathbb{R}$; consequently the two projections of the attractor are the two real attractors,
$$
\pi_+(\Lambda) = \Lambda_+, \qquad \pi_-(\Lambda) = \Lambda_- .
$$

**Proof.** Each $S_i$ is a Euclidean contraction of the plane, so the Hutchinson operator is a contraction of the hyperspace and has a unique fixed point, by the attractor theorem of *Fractal Geometry*; the coding map converges uniformly in $\omega$ at the rate of the contraction factors. In the coordinates, $S_i$ acts by $(x,y) \mapsto (u_{i+}x+v_{i+},\, u_{i-}y+v_{i-})$ and $\varphi$ is an isomorphism, so the same word drives the two real systems; taking $\varphi$ of the limit gives the coordinate formula, and projecting it gives the two attractors.

**Theorem (the attractor is not a product).** The attractor is contained in the product of the two real attractors,
$$
\Lambda \subseteq \varphi^{-1}\bigl(\Lambda_+ \times \Lambda_-\bigr) ,
$$
and the inclusion is strict in general. The product is the attractor of the $m^2$-element system of the **mixed** similarities, which pairs every first-coordinate map with every second-coordinate map,
$$
\{(x,y) \mapsto (u_{i+}x+v_{i+},\, u_{j-}y+v_{j-})\}_{i,j \in \{1,\ldots,m\}} ,
$$
itself a system of split-complex affine maps with $m^2$ members; the $m$ maps of a given split-complex system, by contrast, drive the two coordinates by the **same** word, so the attractor is the image of a single shift space and the two coordinates are coupled through the coding.

**Proof.** The inclusion is the projection statement of the previous theorem. For the strictness take $u_1 = u_2 = 1/3$, $v_1 = 0$, $v_2 = 2/3$, all real. Both factors are the middle-third Cantor set $C$, and the attractor is the image of $C$ under the diagonal embedding, $\varphi^{-1}\bigl(\{(x,x) : x \in C\}\bigr)$, of Hausdorff dimension $\log2/\log3$, while $\varphi^{-1}(C\times C)$ has dimension $2\log2/\log3$. The product is already not invariant at the first stage: $S_1\bigl(\varphi^{-1}(C\times C)\bigr)\cup S_2\bigl(\varphi^{-1}(C\times C)\bigr)$ omits the two mixed squares and is strictly smaller than $\varphi^{-1}(C\times C)$.

**Definition.** The **similarity dimension of the real factor** $\Lambda_\pm$ is the root $s_\pm$ of

$$
\sum_{i=1}^{m} |u_{i\pm}|^{s_\pm} = 1 ,
$$

provided the root lies in $[0,1]$, which is the case exactly when the open set condition holds; the **sum of the two similarity dimensions** is $s_+ + s_-$.

**Theorem (the dimension).** Assume that the two real systems satisfy the open set condition, so that $0 < \mathcal{H}^{s_+}(\Lambda_+) < \infty$ and $0 < \mathcal{H}^{s_-}(\Lambda_-) < \infty$ by the Moran–Hutchinson theorem. Then:

**(a)** if every $u_i$ is real, $u_i = r_i$, the maps $S_i$ are Euclidean similarities of ratios $|r_i|$, the attractor is a self-similar set of the ratio list $\{r_i\}$, and

$$
\dim_H \Lambda = s, \qquad \sum_{i=1}^{m} r_i^{s} = 1 ,
$$

the common value of $s_+$ and $s_-$;

**(b)** in general

$$
\max\{\dim_H \Lambda_+,\, \dim_H \Lambda_-\} \leq \dim_H \Lambda \leq \min\{\dim_H \Lambda_+ + \dim_H \Lambda_-,\, 2\} ,
$$

with the lower bound from the projections and the upper bound from the inclusion in the product; the upper bound is attained exactly by the mixed system, whose attractor is the product;

**(c)** if the addresses of the $+$-coordinate separate and $|u_{i+}| \geq |u_{i-}|$ for every $i$, then $\Lambda$ is the graph of a Lipschitz function over $\Lambda_+$ and

$$
\dim_H \Lambda = \dim_H \Lambda_+ = s_+ ,
$$

the larger of the two factor dimensions.

**Proof.** (a) A real linear part is a similarity of the plane, so $\Lambda$ is the attractor of the similarity system $\{r_i\}$ and the dimension is its similarity dimension. (b) The projection $\pi_+$ is Lipschitz with $\pi_+(\Lambda) = \Lambda_+$, so $\dim_H \Lambda \geq \dim_H \Lambda_+$ and likewise for the other factor; the upper bound is the inclusion $\Lambda \subseteq \varphi^{-1}(\Lambda_+\times\Lambda_-)$ with the product rule of *Fractal Geometry*. (c) The separation of the $+$-addresses makes each $x \in \Lambda_+$ carry a unique coding $\omega$, so the attractor is the graph of the function $\varphi(x) = \tau_-(\omega)$; two points of $\Lambda_+$ with a common prefix of length $n$ have $|x-x'|$ comparable to $\prod_{k \leq n}|u_{\omega_k+}|$ and the corresponding values differ by at most a multiple of $\prod_{k\leq n}|u_{\omega_k-}| \leq \prod_{k \leq n}|u_{\omega_k+}|$, so the function is Lipschitz and the graph is a bi-Lipschitz image of $\Lambda_+$. Finally $s_+ \geq s_-$, because $\sum_i|u_{i-}|^{s_+} \leq \sum_i|u_{i+}|^{s_+} = 1$ and the defining function of $s_-$ is decreasing.

**Example (the diagonal dust).** Let $S_1(z) = z/3$ and $S_2(z) = z/3 + 2/3$, the translations being real. The two real factors are the middle-third Cantor set $C$, of dimension $s_+ = s_- = \log 2/\log 3 = 0.6309297535\ldots$, the maps are Euclidean similarities, and the attractor is the **diagonal dust**
$$
\Lambda = \varphi^{-1}\bigl(\{(x,x) : x \in C\}\bigr), \qquad \dim_H \Lambda = \frac{\log 2}{\log 3} = 0.6309297535\ldots ,
$$
whose box counts at the scales $3^{-n}$ are exactly $2^n$ — the counts $16, 32, 64, 128, 256$ at $n = 4, \ldots, 8$, recomputed. The product $\varphi^{-1}(C\times C)$, of dimension $2\log2/\log3 = 1.2618595071\ldots$, is **not** the attractor of a two-map system; it is the attractor of the mixed four-map system of the theorem above. The dust is the middle-third Cantor set lying on the real axis of the split plane, and it meets the null cone at the origin, since $0 \in C$.

**Example (a dust away from the null cone).** Let $S_1(z) = z/3 + 1$ and $S_2(z) = z/3 + 5/3$, with real translations. The real factors are Cantor sets contained in the invariant interval $\bigl[\tfrac32,\tfrac52\bigr]$, so the attractor lies in the quadrant $z_+ \geq \tfrac32$, $z_- \geq \tfrac32$ of the idempotent plane, whose closure is disjoint from the null cone; the attractor is a Cantor dust avoiding the zero divisors. The dimension is the same $\log2/\log3$.

**Example (anisotropic ratios).** Let $u = \tfrac{7}{24} + \tfrac{1}{24}j$, so that $u_+ = \tfrac13$, $u_- = \tfrac14$ and $N(u) = \tfrac{1}{12}$; the two ratios are different and both below one. Let $S_1(z) = uz$ and $S_2(z) = uz+1$, the translation $1$ being real. The two real systems are $x \mapsto \tfrac13 x$, $x \mapsto \tfrac13 x+1$ and $y \mapsto \tfrac14 y$, $y \mapsto \tfrac14y+1$. Both satisfy the open set condition, with the Cantor sets of ratios $\tfrac13$ and $\tfrac14$ of dimensions $s_+ = \log2/\log3 = 0.6309297535\ldots$ and $s_- = \log2/\log4 = \tfrac12$; the $+$-addresses separate, since the images $S_1(\Lambda_+) \subseteq [0,\tfrac12]$ and $S_2(\Lambda_+) \subseteq [1,\tfrac52]$ are disjoint, and $u_+ > u_-$, so by the theorem the attractor is the graph of a Lipschitz function over $\Lambda_+$ and
$$
\dim_H \Lambda = \dim_H \Lambda_+ = \frac{\log 2}{\log 3} = 0.6309297535\ldots ,
$$
the larger of the two factor dimensions; the box counting of a sampled orbit at the scales $3^{-n}$ gives counts growing like $2^n$, confirming it. The example shows that the anisotropy of the linear part lets the two coordinate factors have different dimensions, and that the attractor carries the larger of the two: the second dimension is not added, because the two coordinates share the coding. The values were recomputed.

## The Null Cone

**Definition.** The **null cone** of $\mathbb{D}$ is $\mathcal{N} = \{N = 0\} = \mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$, the union of the two coordinate axes $z_+ = 0$ and $z_- = 0$ of the idempotent plane.

**Theorem (the trace of the null cone on the attractor).** The attractor meets the null cone exactly in the points whose coding has one coordinate equal to $0$,

$$
\Lambda \cap \mathcal{N} = \varphi^{-1}\Bigl(\Lambda \cap \bigl(\{0\}\times\Lambda_-\bigr)\Bigr) \cup \varphi^{-1}\Bigl(\Lambda \cap \bigl(\Lambda_+\times\{0\}\bigr)\Bigr) ,
$$

so that $\Lambda$ meets the null cone if and only if $0$ belongs to $\Lambda_+$ or to $\Lambda_-$; and $\Lambda$ is contained in one of the four open quadrants of $\mathbb{D}\setminus\mathcal{N}$ if and only if $\Lambda_+$ lies in one of the two half-lines $\mathbb{R}_{>0}$, $\mathbb{R}_{<0}$ and $\Lambda_-$ likewise.

**Proof.** $N(z) = z_+z_-$, so $z \in \mathcal{N}$ iff $z_+ = 0$ or $z_- = 0$, and $\Lambda$ is the set of the points $(\tau_+(\omega),\tau_-(\omega))$; a coding with $\tau_\pm(\omega) = 0$ exists exactly when $0 \in \Lambda_\pm$, since the coding map of a factor is onto its attractor. The components of the complement are the four sign quadrants, and $\Lambda \subseteq \varphi^{-1}(\Lambda_+\times\Lambda_-)$ lies in one of them exactly when each factor lies in the corresponding half-line.

**Remark (the open set condition and the indefinite form).** The open set condition is a statement about the Euclidean metric, the only metric in which the maps contract; the form $N$ plays no role in it, and there is no natural "null" version of the condition. A system can satisfy the open set condition with an open set that straddles the null cone, and the dimension statements above are unaffected. What the null cone does govern is the position of the attractor, as the previous theorem shows, and the failure of the polar decomposition on it, which is why the description of every attractor is given in the idempotent coordinates rather than in the split polar coordinates of *Hyperbolic Rotations*.

## The Symmetry

**Definition.** A system $\{S_i\}$ is **conjugation-symmetric** if, for every $i$, the conjugate map $\bar S_i(\bar z) = \bar u_i z + \bar v_i$ is again one of the maps $S_j$; equivalently, if the family is invariant under conjugation up to a permutation of its members.

**Theorem.** If the system is conjugation-symmetric then its attractor is invariant under the conjugation: $\bar\Lambda = \Lambda$. In the idempotent coordinates the conjugation exchanges the two factors, $\varphi(\bar z) = (z_-,z_+)$, so conjugation symmetry of the family forces the two real systems to have the same attractor, $\Lambda_- = \Lambda_+$; the attractor is then a conjugation-invariant subset of $\Lambda_+\times\Lambda_+$, namely the image of the coding, and it is strictly smaller than the product in general — for the system $S_1(z) = z/3$, $S_2(z) = z/3+2/3$ it is the diagonal of $C\times C$.

**Proof.** The attractor is the unique compact invariant set; conjugating the invariance relation $\Lambda = \bigcup S_i(\Lambda)$ and using that the family is closed under conjugation gives $\bar\Lambda = \bigcup \bar S_i(\bar\Lambda) = \bigcup S_j(\bar\Lambda)$, so $\bar\Lambda$ is invariant and equals $\Lambda$ by uniqueness. If $\bar S_i = S_{\sigma(i)}$ for a permutation $\sigma$, then in the coordinates $S_{\sigma(i)+} = S_{i-}$ and $S_{\sigma(i)-} = S_{i+}$, so the two real systems differ only by the reindexing $\sigma$ and have the same attractor; the coding of the conjugate point is obtained by applying $\sigma$ to each letter of the coding, which gives the invariance of $\Lambda$ and shows that $\Lambda$ is properly smaller than the product whenever the two coordinates are not independent.

**Remark (the hyperbolic symmetry).** The symmetry above is the reflection of the split plane that fixes the null cone and exchanges its two lines, and it is the only symmetry of the systems that comes from the algebra: a non-trivial hyperbolic rotation $z \mapsto e^{js}z$ has the singular values $e^{s}$ and $e^{-s}$, so it expands one null direction and cannot preserve a bounded set with more than one point, and a Euclidean rotation other than $\pm1$ is not a split-complex multiplication at all. So the systems carry the **hyperbolic reflection** symmetry and not a hyperbolic rotation symmetry; the "hyperbolic" Cantor sets and gaskets of the split plane are the conjugation-symmetric attractors, and the sets that are not symmetric are the attractors whose two factor systems are not related by the reindexing.

**Example.** The system of the first example, $S_1(z) = z/3$, $S_2(z) = z/3+2/3$, has real coefficients, hence is conjugation-symmetric with $\Lambda_+ = \Lambda_- = C$; its attractor is symmetric under the conjugation, i.e. under the reflection in the null cone. A system with $S_1(z) = z/3$, $S_2(z) = z/3 + \tfrac12(1+j)$ has the coordinates $v_+ = 1$, $v_- = 0$ and is not conjugation-symmetric; its attractor has $\Lambda_+ \neq \Lambda_-$ and is not symmetric.

## The Hyperbolic Groups and the Null Quadric

**Remark.** In the complex plane the iterated function systems of *Iterated Function Systems in the Complex Plane* are sourced by the Kleinian groups, whose limit sets are the Schottky Cantor sets and the Apollonian gasket, and whose dimension is the critical exponent of the group. The split-complex analogue is degenerate in the group: the isometry group of the form $N$ contains the abelian one-parameter group $SO^+(1,1)$, which acts transitively on each hyperbola and has no nonempty fractal limit set; the natural "limit set at infinity" of the group is the projective null quadric itself, the two points $t = \pm1$ of *Split-Complex Null Quadric and Projective Geometry*, which is a two-point set and not a Cantor set. So the split-complex systems are not obtained from a Kleinian group of the plane; their fractal content is entirely in the pair of real one-dimensional systems, as the coding formula and the dimension statements show. The genuine hyperbolic groups and their limit sets are those of the three-dimensional hyperbolic geometry of *Hyperbolic Geometry*, cited in *Iterated Function Systems in the Complex Plane*, and the two-dimensional Lorentzian picture of the split plane is the boundary case in which the limit set collapses to two points.

**Remark (the comparison with the complex systems).** Two features separate the split-complex systems from the complex ones. First, the contractions are anisotropic: a split-complex similarity has two independent ratios $|u_+|, |u_-|$, whereas a complex similarity has the single ratio $|u|$ and a rotation; the split attractors are therefore the dusts over a pair of real self-similar sets and carry the larger of the two factor dimensions, never a genuinely two-dimensional self-similar set of the complex kind, and the anisotropic ratio is the only extra freedom. Second, there is no rotation in the split-complex similarity group: the multiplications by units are the boosts and the scalings, and a Euclidean rotation other than $\pm1$ is not available, so the split plane admits no Sierpiński-gasket-like attractor with rotational symmetry. The attractors are the "hyperbolic Cantor sets" — the conjugation-symmetric dusts over a real self-similar set — and the "gaskets" only in the loose sense of the finitely many graphs woven over the two factors.

## Summary

A split-complex similarity is a map $z \mapsto uz+v$ with $u$ a unit; in the idempotent coordinates it contracts the two coordinate directions by the singular values $|u_+|$ and $|u_-|$, so it is Euclidean-contractive exactly when both lie in $(-1,1)$, and it is anisotropic unless $u$ is real. No $N$-preserving map is a Euclidean contraction, so the systems take their contractions from the Euclidean metric and not from the split form; this is the sense in which the contraction is read in the Euclidean coordinates. The attractor of such a system is, through the idempotent isomorphism, the image of the shift space under the coding map, $\Lambda = \varphi^{-1}\bigl(\{(\tau_+(\omega),\tau_-(\omega))\}\bigr)$; its two projections are the two real attractors, and it is **not** their product, because the two coordinates are driven by the same word. The product $\Lambda_+\times\Lambda_-$ is the attractor of the mixed system of the $m^2$ paired maps, and it is strictly larger in general; its dimension is the sum $s_+ + s_-$ of the two similarity dimensions, which is therefore an upper bound for the dimension of the attractor, attained only in the mixed case. When the linear parts are real the attractor is a self-similar set of dimension $s$ solving $\sum_i r_i^s = 1$, and when the $+$-addresses separate with $|u_{i+}| \geq |u_{i-}|$ the attractor is a Lipschitz graph over $\Lambda_+$ of dimension $s_+$; the examples give the diagonal dust of dimension $\log2/\log3$, a dust avoiding the null cone, and an anisotropic case of the same dimension $\log2/\log3$.

The null cone meets the attractor exactly where a factor contains $0$, and the attractor is confined to one of the four quadrants of the idempotent plane exactly when both factors avoid $0$ with a fixed sign. The symmetry compatible with the split structure is the conjugation, which exchanges the two factors and holds exactly for the conjugation-symmetric systems; hyperbolic rotations cannot preserve a bounded attractor, and Euclidean rotations are not split-complex multiplications. The group-theoretic source of the complex systems — the Kleinian limit sets — degenerates here: the isometry group is abelian and its only limit set is the two-point null quadric. The definitions and the dimension theorem are those of *Fractal Geometry*; the algebra and the null cone are those of *Split-Complex Norm and Invertibility* and *Split-Complex Null Quadric and Projective Geometry*; the complex systems compared are those of *Iterated Function Systems in the Complex Plane*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S(z) = uz+v$ | Split-complex similarity |
| $u_\pm = p\pm q$ | Idempotent coordinates of $u = p+jq$; the singular values of the linear part |
| $\max\{\lvert u_+\rvert,\lvert u_-\rvert\}$ | Euclidean contraction factor |
| $\Lambda = \varphi^{-1}\bigl(\{(\tau_+(\omega),\tau_-(\omega))\}\bigr)$ | Attractor, the image of the coding; not a product |
| $\pi_\pm(\Lambda) = \Lambda_\pm$ | Projections of the attractor: the two real attractors |
| $s_\pm$ | Similarity dimension of the real factor, root of $\sum_i\lvert u_{i\pm}\rvert^{s}=1$ |
| $s_+ + s_-$ | Dimension of the product, the mixed system; an upper bound in general |
| $r_i$ real, $\sum_i r_i^s = 1$ | Dimension when the linear parts are real |
| $\mathcal{N} = \{z_+z_- = 0\}$ | Null cone, the two coordinate axes |
| conjugation-symmetric | Family invariant under $z\mapsto\bar z$ up to reindexing; $\Lambda_- = \Lambda_+$ |
| $SO^+(1,1)$ | Abelian hyperbolic rotation group; no fractal limit set |
| $t = \pm1$ | The projective null quadric, the degenerate limit set |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the attractor theorem and the open set condition.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd edition (Wiley, 2014), for the similarity dimension and the product rule.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex (hyperbolic) plane and its similarities.
- Michael F. Barnsley, *Fractals Everywhere*, 2nd edition (Academic Press, 1993), for the anisotropic affine systems and their attractors.
- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for the hyperbolic isometries and the limiting behaviour of the discrete groups.
