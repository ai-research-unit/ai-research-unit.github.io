# __The Dual-Number Iterated Function Systems__

## Introduction

An iterated function system on the dual numbers is a finite family of **dual similarities** $S_i(z) = u_iz+v_i$ with $u_i$ a unit of $\mathbb{D}'$; in the coordinates $z = x+\varepsilon y$ such a map is

$$
S_i(x+\varepsilon y) = (r_ix+v_{ix}) + \varepsilon\bigl(r_iy+s_ix+v_{iy}\bigr) ,
$$

where $u_i = r_i+\varepsilon s_i$ with $r_i \neq 0$. The real part is a one-dimensional real similarity, and the infinitesimal part is an affine map whose coefficient is again $r_i$ and which is **coupled to the real part** through the term $s_ix$. This article describes the attractors of such systems and proves the collapse: the projection of the attractor is the attractor of the induced real system, the attractor is the graph of a continuous function over it whenever the real address map is injective, and its box dimension equals the dimension of the real attractor; in the decoupled case $s_i = 0$ the attractor is a product of two real self-similar sets, which is the real theory applied twice. In neither case is there a genuinely dual fractal dimension, and the fractal content of the system is the real one.

The article is deliberately short. The definitions of the attractor, the open set condition and the similarity dimension are those of *Fractal Geometry*; the real one-dimensional systems are those of *Fractal Geometry* and *Fractal Analysis* of Part III; the algebra and the parabolic interpretation of the dual numbers are those of *Dual-Numbers Algebra* and *Shears and Parabolic Rotations*; and the complex and split-complex systems compared are those of *Iterated Function Systems in the Complex Plane* and *The Split-Complex Iterated Function Systems*. No physics is invoked, and the box-counting values displayed were recomputed.

## The Contractions and the Projection

**Definition.** A **dual similarity** is $S(z) = uz+v$ with $u$ a unit of $\mathbb{D}'$, and its **linear part** in the basis $\{1,\varepsilon\}$ is the triangular matrix

$$
[u] = \begin{pmatrix} r & 0 \\ s & r \end{pmatrix}, \qquad u = r+\varepsilon s .
$$

An iterated function system is a finite family $\{S_1,\ldots,S_m\}$, $m \geq 2$, of dual similarities that are contractions of the Euclidean plane; its **attractor** is the unique nonempty compact set $\Lambda$ with $\Lambda = \bigcup_i S_i(\Lambda)$.

**Theorem (the Euclidean contraction condition).** The matrix $[u]$ has the singular values the two roots of $\lambda^2-(2r^2+s^2)\lambda+r^4 = 0$, both equal to $|r|$ when $s = 0$ and the larger one strictly greater than $|r|$ when $s \neq 0$. Consequently the Euclidean contraction factor of $S$ is at least $|r|$, and $S$ is a contraction only if $|r| < 1$ and the coupling $s$ is small enough; for $s = 0$ the condition is exactly $|r| < 1$.

**Proof.** The matrix of the linear part is $\begin{pmatrix}r&0\\s&r\end{pmatrix}$, so $[u]^{\mathsf{T}}[u] = \begin{pmatrix}r^2+s^2 & rs\\ rs & r^2\end{pmatrix}$ with trace $2r^2+s^2$ and determinant $r^4$; its eigenvalues are the squares of the singular values, and they are both $r^2$ exactly when $s = 0$.

**Definition.** The **induced real system** is the family $\{x \mapsto r_ix+v_{ix}\}$ of real similarities on the line, with real attractor $A_x$.

**Theorem (the projection).** The projection $\pi(x+\varepsilon y) = x$ of the attractor is the real attractor:

$$
\pi(\Lambda) = A_x .
$$

**Proof.** The projection commutes with the maps, since the $x$-coordinate of $S_i(x+\varepsilon y)$ does not involve $y$; hence $\pi(\Lambda)$ is a nonempty compact set invariant under the induced real system, and it equals its unique attractor.

## The Attractor Is a Graph or a Product

**Theorem (the attractor is a graph).** If the induced real system has a separating address map — the images $r_iA_x+v_{ix}$ are pairwise disjoint — then the attractor is the graph of a continuous function over the real attractor,

$$
\Lambda = \{x+\varepsilon\varphi(x) : x \in A_x\} ,
$$

with $\varphi$ the continuous function determined by $\varphi(S_i(x)) = r_i\varphi(x)+s_ix+v_{iy}$.

**Proof.** The address map of the real system is injective, so a point of $A_x$ determines its coding and hence the whole orbit of the fibre coordinate; the affine recursion for $y$ along a coding converges because $|r_i| < 1$, and the limit $\varphi(x)$ depends continuously on the coding, hence on $x$. The invariance relation for $\varphi$ is the statement that $S_i$ maps the graph over $A_x$ to the graph over $S_i(A_x)$.

**Theorem (the dimension, equal ratios).** Suppose the real parts of the linear parts are equal, $r_i = r$ for all $i$, with $|r| < 1$, and that the induced real system has a separating address map. Then

$$
\dim_B \Lambda = \dim_B A_x = \dim_H A_x ,
$$

the similarity dimension of the real factor, and the coupling terms $s_i$ do not change the dimension.

**Proof.** At level $n$ the piece $S_\omega(\Lambda)$ of a word $\omega$ of length $n$ has linear part $\begin{pmatrix}r^n&0\\ S_\omega& r^n\end{pmatrix}$ with $S_\omega = \sum_{k=1}^n s_{\omega_k}r^{n-1}$, so $|S_\omega| \leq n\max_i|s_i|\,|r|^{n-1}$; the piece therefore lies in a rectangle of side $|r|^n$ in $x$ and $\mathcal{O}(n|r|^{n-1})$ in $y$, covering $\mathcal{O}(n)$ boxes of the grid of side $|r|^n$. Since the address map separates the pieces, the box count at scale $|r|^n$ is $\mathcal{O}(n)\,m^n$, and the factor $n$ is subexponential: $\dim_B\Lambda = \log m/\log(1/|r|) = \dim_B A_x$. The equality of the box and Hausdorff dimensions of $A_x$ is the Moran–Hutchinson theorem of *Fractal Geometry* under the open set condition.

**Remark (the graph is not Lipschitz).** When some $s_i \neq 0$ the function $\varphi$ is continuous but not Lipschitz: the relation $\varphi(S_i(x)) = r\varphi(x)+s_ix+v_{iy}$ gives the bound $(rL+|s_i|)/r = L+|s_i|/|r|$ for any local Lipschitz constant $L$, larger than $L$, so no finite $L$ works. The loss of regularity is compensated, in the dimension, by the subexponential factor $n$ of the theorem; this is why the dual direction adds no dimension although it does add the coupling.

**Theorem (no product attractor).** No system of dual similarities has an attractor that is a product of two one-dimensional self-similar sets with independent dynamics: the linear part of every dual similarity has the **same** ratio $r_i$ in the two coordinate directions, so a single coding drives both coordinates, and the attractor is the image of one shift space. In the decoupled case $s_i = 0$ the infinitesimal coordinate is still a continuous function of the coding, and the attractor is the graph of that function over $A_x$; when the translations are real, $v_{iy} = 0$, the graph is degenerate and the attractor is the real set $A_x$ itself. A genuinely two-dimensional product $A_x\times A_y$ would require independent ratios in the two directions, which the algebra does not provide.

**Proof.** The linear part of $uz$ is $\begin{pmatrix}r&0\\ s&r\end{pmatrix}$ with the entry $r$ on the diagonal twice; the second coordinate of the orbit is determined by the same sequence of maps as the first, so the coding space maps into the plane with one-dimensional image. The decoupled case $s_i = 0$ leaves the coding dependence intact through the translations $v_{iy}$, and the resulting set is a graph over $A_x$; if in addition all $v_{iy} = 0$, the graph lies on the real axis.

**Example (a lifted Cantor set).** Let $u = \tfrac13+\varepsilon$ and let the translations be $v_1 = 0$, $v_2 = \tfrac23$, both real; the induced real system $\{x/3, x/3+2/3\}$ has the middle-third Cantor set $A_x$ of dimension $\log2/\log3 = 0.6309297535\ldots$, the addresses separate, and the real parts are equal, so the attractor is the graph over the Cantor set and

$$
\dim_B\Lambda = \frac{\log 2}{\log 3} = 0.6309297535\ldots .
$$

The box counts at the scales $3^{-n}$, for the finite set of the $2^{16}$ points belonging to the level-$16$ codings and the grid of side $3^{-n}$ anchored at the origin, are $192, 384, 896, 2048, 4096, 9216$ for $n = 4,\ldots,9$; the ratios to $2^n$ are $12, 12, 14, 16, 16, 18$, of order $n$, as the subexponential factor predicts, and the box dimensions $\log N_n/(n\log3)$ are $1.196, 1.083, 1.031, 0.991, 0.946, 0.923$, decreasing towards $\log2/\log3 = 0.6309297\ldots$. The values were recomputed in exact rational arithmetic; the floating-point counts are unreliable at the grid boundaries at these scales.

**Example (the decoupled case).** Let $u = \tfrac13$ (so $s = 0$) and let the translations be $v_1 = 0$, $v_2 = \tfrac23+\varepsilon\tfrac13$. The dynamics in the two coordinates share the ratio $\tfrac13$ and differ in the translations, so the attractor is the graph of the continuous function over $C$ determined by the second coordinate, of box dimension $\log2/\log3 = 0.6309297535\ldots$, and the box counts at the scales $3^{-n}$ are exactly $2^n$ — the counts $16, 32, 64, 128, 256, 512$ at $n = 4,\ldots,9$, recomputed — confirming that no second dimension is gained; the attractor is not the product $C\times C'$ of two Cantor sets, which no dual system can produce.

## The Comparison with the Complex and the Split-Complex Systems

**Remark.** The three systems differ in exactly one place: what the algebra's second direction does. In $\mathbb{C}$ the similarity group contains the rotations, and the systems produce genuinely two-dimensional self-similar sets — the Sierpiński gasket, the Koch curve, the Julia sets as limits of conformal systems — as in *Iterated Function Systems in the Complex Plane*. In $\mathbb{D}$ the multiplication by a unit is an anisotropic scaling with singular values $|u_+|,|u_-|$ and no rotation, and the two coordinate directions are driven by the same word, so the systems produce Lipschitz graphs over one-dimensional real self-similar sets rather than products, as in *The Split-Complex Iterated Function Systems*; the product of the two real attractors is the attractor of the mixed system, not of the split one. In $\mathbb{D}'$ the multiplication is triangular, its linear part has the two equal singular values only when the coupling vanishes, and every system has the attractor a one-dimensional graph over a real self-similar set: the second direction is not independent but the derivative direction of the first, and it never supplies a second generating coordinate. The comparison is sharp: the complex system has two generating directions (the ratio and the rotation), the split-complex system has two generating ratios, and the dual system has one generating ratio and a derivative.

## Summary

A dual similarity $S(z) = uz+v$ has the triangular linear part $\begin{pmatrix}r&0\\s&r\end{pmatrix}$, a Euclidean contraction only if $|r| < 1$ and the coupling $s$ is small; its real part is a real similarity and the infinitesimal part is an affine map coupled to the real part. The projection of the attractor of a dual iterated function system is the attractor $A_x$ of the induced real system, and the attractor is the graph $\{x+\varepsilon\varphi(x) : x \in A_x\}$ of a continuous function whenever the real addresses separate. When the real parts of the linear parts are equal the box dimension of the attractor equals the dimension of the real attractor, the coupling contributing only the subexponential factor $n$ and making the graph continuous but not Lipschitz; and no dual system produces a product of two independent one-dimensional attractors, because the linear part has the same ratio in both coordinates, so the attractor is always the image of a single shift space. There is therefore no genuinely dual fractal dimension: the second direction records the derivative of the first and never generates new fractal structure. The definitions are those of *Fractal Geometry*; the complex and split-complex systems compared are those of *Iterated Function Systems in the Complex Plane* and *The Split-Complex Iterated Function Systems*; and the infinitesimal interpretation of the coupling is that of *Shears and Parabolic Rotations*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S(z) = uz+v$, $u = r+\varepsilon s$ | Dual similarity |
| $\begin{pmatrix}r&0\\s&r\end{pmatrix}$ | Triangular matrix of the linear part |
| $r_i$, $s_i$ | Real part, coupling of the $i$-th linear part |
| $A_x$, induced real system | Projection and its real attractor |
| $\Lambda = \{x+\varepsilon\varphi(x)\}$ | Attractor as a graph over $A_x$ |
| $s_i = 0$ | Decoupled case: $\varphi$ depends on the coding through the translations only |
| $\dim_B\Lambda = \dim_BA_x$ (equal ratios) | The dual direction adds no dimension |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the attractor theorem and the open set condition.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd edition (Wiley, 2014), for the similarity dimension and the dimensions of the self-affine sets.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the dual numbers and their infinitesimal interpretation.
- Michael F. Barnsley, *Fractals Everywhere*, 2nd edition (Academic Press, 1993), for the affine and the triangular iterated function systems.
