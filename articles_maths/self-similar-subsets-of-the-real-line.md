# __Self-Similar Subsets of the Real Line__

## Introduction

This article works the simplest instance of the corpus's fractal theory: the compact subsets of the real line that are built from finitely many **contractions** of the line, applied again and again. The prototype is the **middle-third Cantor set**, obtained either by the repeated removal of the open middle thirds of the intervals or, equivalently, as the unique nonempty compact set carried to itself by the two maps $x \mapsto x/3$ and $x \mapsto x/3 + 2/3$. The article describes the construction level by level, the coding of the points by their base-three digits, the identification of the set with the boundary of the binary tree, and the way the levels tile the interval. The general theory is the subject of the lead article *Fractal Geometry* of Part IV, which owns the box-counting and Hausdorff dimensions, the iterated function systems with the open set condition and the similarity dimension; the measures carried by these sets are the subject of the category `## Fractal Analysis` of Part III. Both are cited here and neither is restated.

The line and its isometries are the subject of *Real Line Geometry and Isometries*: the distance $\lvert x-y\rvert$, the translations $x \mapsto x+t$ and the reflections $x \mapsto t-x$, and the interpretation of the interval as a set with a length. The length of an interval and the Lebesgue measure are those of *Measure Theory and Integration*, and the topological properties of the Cantor set — compactness, perfectness, total disconnectedness, homeomorphism with the Cantor discontinuum — are those of *Topological Spaces*. The coding of the dynamics by the shift is that of *Symbolic Dynamics*; the symmetric constructions under an involution are those of *Reversible Iterated Function Systems and the Involution* of Part III. What this article develops is only the one-dimensional shape: the contractions, the levels, the digits, the tree and the tiling.

Throughout, $\mathbb{R}$ is the real line with its usual distance $d(x,y)=\lvert x-y\rvert$, a **similarity** of the line is a map of the form $x \mapsto r x + t$ or $x \mapsto r(-x) + t$ with $r \neq 0$, its **ratio** is $\lvert r\rvert$, and it is a **contraction** when $\lvert r\rvert < 1$. The two middle-third maps are always

$$
f_1(x) = \frac{x}{3}, \qquad f_2(x) = \frac{x}{3} + \frac{2}{3}.
$$

## Contractions and Similarities of the Line

**Definition.** A map $f : \mathbb{R} \to \mathbb{R}$ is a **similarity** if there is $r \neq 0$ with $d(f(x),f(y)) = \lvert r\rvert\,d(x,y)$ for all $x,y$; the number $\lvert r\rvert$ is its **ratio** and $r$ its **signed ratio**. The similarity is **orientation-preserving** if $r>0$ and **orientation-reversing** if $r<0$, and it is a **contraction** if $\lvert r\rvert < 1$.

**Theorem.** Every similarity of $\mathbb{R}$ is of exactly one of the two forms

$$
f(x) = r x + t \quad (\text{orientation-preserving}), \qquad f(x) = r(-x) + t = -r x + t \quad (\text{orientation-reversing}),
$$

with $r>0$, $t \in \mathbb{R}$. A contraction has exactly one fixed point, $t/(1-r)$ in the first case and $t/(1+r)$ in the second, and the two notions coincide with the isometries and the translations of *Real Line Geometry and Isometries* at $\lvert r\rvert = 1$.

*Proof.* A similarity fixes the origin after a translation, so it suffices to determine the maps with $d(f(x),f(y))=\lvert r\rvert\lvert x-y\rvert$ and $f(0)=0$. Such a map sends $1$ to $\pm r$, and the two maps $x \mapsto rx$ and $x \mapsto -rx$ both have the required distance behaviour; conversely a map with $f(0)=0$ and $f(1)=\pm r$ is determined by the two distances $\lvert f(x)\rvert = \lvert r\rvert\lvert x\rvert$ and $\lvert f(x)-f(1)\rvert = \lvert r\rvert\lvert x-1\rvert$, which pin down the sign. The fixed-point statements solve $rx+t=x$ and $-rx+t=x$. $\square$

**Remark (the order).** A similarity either preserves or reverses the order of $\mathbb{R}$ according to the sign of its ratio, and the orientation-reversing similarities are exactly the compositions of an orientation-preserving similarity with the reflection $x\mapsto -x$. The order is what the one-dimensional construction is read against: the images of an interval under the maps of a system are pieces placed along the line, and the open set condition of the next article is the statement that these pieces are separated.

**Definition.** Let $f_1,\dots,f_m$ be contractions of $\mathbb{R}$. A nonempty compact set $\Lambda \subseteq \mathbb{R}$ is **invariant** for the system when

$$
\Lambda = \bigcup_{i=1}^m f_i(\Lambda),
$$

and it is **self-similar** when the $f_i$ are similarities. When the system satisfies the separation hypotheses of *Fractal Geometry*, the invariant set is unique and is the **attractor** of the system; the level-$k$ pieces are the sets

$$
\Lambda_{i_1\cdots i_k} = f_{i_1}\circ\cdots\circ f_{i_k}(\Lambda),
$$

indexed by the words $i_1\cdots i_k$ of length $k$ over the alphabet $\{1,\dots,m\}$.

**Remark.** The uniqueness of $\Lambda$ and the convergence of its level-$k$ approximations are the content of the contraction mapping theorem applied to the space of nonempty compact subsets with the Hausdorff metric, and they are stated and proved in *Fractal Geometry*; the reader is referred there once and for all. The present article uses only the one-dimensional case and the explicit pieces, so that the shape can be read off the construction. The identity of the attractor with the limit of the pieces is written

$$
\Lambda = \bigcap_{k \geq 1}\bigcup_{\lvert w\rvert = k} f_{i_1}\circ\cdots\circ f_{i_k}([0,1]),
$$

for a system whose pieces lie in a fixed interval, the union being over the words of length $k$.

## The Middle-Third Construction

### The Levels

**Definition.** The **levels** of the middle-third construction are the compact sets $C_0 = [0,1]$ and

$$
C_{k+1} = \frac{C_k}{3} \cup \left(\frac{C_k}{3} + \frac{2}{3}\right) = f_1(C_k) \cup f_2(C_k),
$$

equivalently, $C_{k+1}$ is obtained from $C_k$ by deleting from every interval of $C_k$ its open middle third. The **middle-third Cantor set** is

$$
C = \bigcap_{k \geq 0} C_k .
$$

**Theorem (the levels).** For every $k \geq 0$ the set $C_k$ is a disjoint union of $2^k$ closed intervals, each of length $3^{-k}$, and the total length of $C_k$ is $(2/3)^k$. The complement $[0,1]\setminus C_k$ is a union of $2^k-1$ pairwise disjoint open intervals whose total length is $1-(2/3)^k$. Consequently $C$ has Lebesgue measure zero.

*Proof.* The statement is by induction on $k$: $C_0=[0,1]$ is one interval of length $1$; if $C_k$ is a union of $2^k$ intervals of length $3^{-k}$, then $f_1(C_k)$ and $f_2(C_k)$ are unions of $2^k$ intervals of length $3^{-(k+1)}$, placed in $[0,1/3]$ and $[2/3,1]$ respectively, and these are disjoint from one another, so $C_{k+1}$ is a disjoint union of $2^{k+1}$ intervals of the stated length. The total length is $2^k3^{-k}$; the gap count and the gap length follow because $[0,1]$ is the disjoint union of the $2^k$ intervals of $C_k$ and the $2^k-1$ open gaps left at the successive stages. The measure of $C$ is the limit of the decreasing lengths $\lvert C_k\rvert = (2/3)^k \to 0$. $\square$

For the first levels this gives: $C_0 = [0,1]$; $C_1 = [0,\tfrac13]\cup[\tfrac23,1]$; $C_2 = [0,\tfrac19]\cup[\tfrac29,\tfrac13]\cup[\tfrac23,\tfrac79]\cup[\tfrac89,1]$; two intervals of length $1/3$, then four of length $1/9$, then eight of length $1/27$, with total lengths $2/3$, $4/9$, $8/27$.

**Theorem (the shape).** The set $C$ is compact, perfect, totally disconnected and uncountable; it contains no interval, it is its own boundary, and it is homeomorphic to the Cantor discontinuum of *Topological Spaces*. It is the attractor of the system $\{f_1,f_2\}$ of the two middle-third maps.

*Proof.* As an intersection of nested nonempty compact sets, $C$ is compact and nonempty. It has no isolated point, because a point of $C$ has a neighbourhood in the construction refined at every level, and the two pieces of a level fall one on each side; no point is separated from all the others. It is totally disconnected because any two distinct points of $C$ are separated by some removed middle third, and the gaps are dense in $[0,1]$ in the sense that every interval of positive length contains one. An interval of positive length cannot be contained in $C$, since its length exceeds $3^{-k}$ for large $k$ while the components of $C_k$ have length $3^{-k}$. A nonempty compact perfect totally disconnected metric space is homeomorphic to the Cantor discontinuum by the standard characterisation, and it is uncountable because it is perfect and compact. The invariance $C = f_1(C)\cup f_2(C)$ is the definition of the levels, and the attractor property is the uniqueness of *Fractal Geometry*. $\square$

**Remark (the dimension, cited).** The system has two maps of ratio $1/3$, so its similarity dimension solves $2\cdot3^{-s}=1$, namely $s = \log 2/\log 3 = 0.6309\ldots$; the open set condition holds with $V=(0,1)$, so by the Moran–Hutchinson theorem of *Fractal Geometry* the Hausdorff and box dimensions of $C$ are both this number. The value is recomputed here and the theorem is cited, not proved: the dimension of the Cantor set as a general statement is the lead article's.

### The Digit Coding

**Theorem (the coding).** Every point of $C$ is uniquely of the form

$$
x = \sum_{n \geq 1}\frac{d_n}{3^n}, \qquad d_n \in \{0,2\},
$$

and the map $\{0,2\}^{\mathbb{N}} \to C$, $(d_n) \mapsto \sum_n d_n3^{-n}$, is a homeomorphism. Equivalently, writing $2 = 3-1$, every point of $C$ has a base-three expansion whose digits are all $0$ or $2$, and this expansion is unique.

*Proof.* A point of $C_k$ lies in one of the $2^k$ intervals of $C_k$, and passing from level $k$ to level $k+1$ chooses the left or the right third, so a point of $C$ determines a sequence of choices $d_n \in \{0,2\}$; the intervals of $C_k$ are precisely the sets of points whose first $k$ chosen digits are a fixed word, so two distinct points of $C$ are separated at some level and have distinct digit sequences. This gives the bijection. The map is continuous because two points whose first $k$ digits agree lie in the same interval of $C_k$, of length $3^{-k}$; a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism. For the uniqueness, the only ambiguity in the base-three expansion of a real number is between a terminating expansion $\cdots d\,000\ldots$ and the expansion $\cdots (d-1)222\ldots$ ending in $2$s, and the two expansions differ in the digit $d-1$: if the digits are to lie in $\{0,2\}$, both alternatives cannot have all digits even, since one of $d$ and $d-1$ is odd. Hence the expansion with digits in $\{0,2\}$ is unique. $\square$

**Example.** The left endpoint $0$ has the expansion $0.000\ldots$ and the right endpoint $1$ the expansion $0.222\ldots$; the point $1/4$ has the expansion $0.020202\ldots$, since $\sum_{k\geq0}2\cdot3^{-(2k+1)} = (2/3)/(1-1/9) = 3/4$, which is $1/4$ in the interval; and $1/3 = 0.0222\ldots$ with digits $0,2,2,2,\ldots$, the point being the right endpoint of the first piece and the left endpoint of the first gap. All three are in $C$.

**Remark (the shift).** The digit sequence transforms under the map $x\mapsto 3x \bmod 1$ carried by $C$ into the one-sided shift $(d_1,d_2,\dots)\mapsto(d_2,d_3,\dots)$; the shift of $C$ is the full two-shift, whose topological entropy is $\log 2$. The reading of the dynamics through the shift belongs to *Symbolic Dynamics* and to Part III, and is recorded here only to identify the coding as the dynamical one.

## The Cantor Set as the Boundary of the Binary Tree

**Definition.** The **full binary tree** $T_2$ has as vertices the finite words $w$ over the alphabet $\{0,1\}$, including the empty word $\varnothing$, with an edge from $w$ to $wi$ for $i \in \{0,1\}$. The **boundary** $\partial T_2$ is the set of right-infinite words $\omega \in \{0,1\}^{\mathbb{N}}$, with the **ultrametric**

$$
d(\omega,\tau) = 2^{-k}, \qquad k = \min\{n : \omega_{n+1} \neq \tau_{n+1}\},
$$

with $d(\omega,\omega)=0$; here $k$ is the length of the longest common prefix of $\omega$ and $\tau$.

**Theorem.** With this distance, $\partial T_2$ is a compact, perfect, totally disconnected metric space, hence homeomorphic to the Cantor discontinuum, and the map

$$
\omega \mapsto \sum_{n\geq1} \frac{2\,\omega_n}{3^n}
$$

is a homeomorphism $\partial T_2 \to C$ onto the middle-third Cantor set. Under it the vertex $w$ of length $k$ corresponds to the cylinder

$$
C_w = \left\{x \in C : \text{the first } k \text{ digits of } x \text{ are } 2w_1,\dots,2w_k\right\} = f_{i_1}\circ\cdots\circ f_{i_k}(C),
$$

of diameter $3^{-k}$, where $i_j = w_j+1$; the $2^k$ cylinders at level $k$ are pairwise disjoint and their union is $C_k$.

*Proof.* The boundary is a closed subset of the compact product $\{0,1\}^{\mathbb{N}}$, hence compact; it has no isolated points because any cylinder splits into the two cylinders of the next level; and any two distinct infinite words are separated at some level, so the space is totally disconnected. The characterisation of the Cantor discontinuum gives the homeomorphism statement. The displayed map is the digit coding of the previous section under the relabelling $0\rightleftarrows 1$ of the alphabet, hence a homeomorphism; the cylinder description is the definition of the level-$k$ pieces, and the diameter is $3^{-k}$ because each piece is an interval of that length. $\square$

**Remark.** The Cantor set is thus the boundary of the binary tree at the two extreme leaves; more generally, the boundary of a rooted tree whose vertices have varying numbers of children is a self-similar set with the corresponding ratios, and a set of the line that is the boundary of a tree is exactly a set coded by its branching. The tree itself with its automorphisms is the subject of the corpus's groups acting on trees, and the identification of the boundary with the limit space of a self-similar group is the subject of *Limit Spaces and Schreier Graphs*.

## The Self-Similar Tiling

**Theorem (the additive tiling).** The middle-third Cantor set satisfies

$$
C + C = [0,2], \qquad C - C = [-1,1],
$$

where $C+C = \{x+y : x,y \in C\}$ and $C-C = \{x-y\}$. Equivalently, every real number in $[0,2]$ is a sum of two points of $C$, and every number in $[-1,1]$ is a difference of two points of $C$.

*Proof.* Because $C = \tfrac13 C \cup \bigl(\tfrac13 C + \tfrac23\bigr)$, the sumset $S = C+C$ satisfies

$$
S = \tfrac13 S \;\cup\; \bigl(\tfrac13 S + \tfrac23\bigr) \;\cup\; \bigl(\tfrac13 S + \tfrac43\bigr),
$$

the three pieces arising from the three ways of adding a left or a right third to a left or a right third. The three maps $x \mapsto x/3$, $x\mapsto x/3+2/3$ and $x\mapsto x/3+4/3$ are contractions of ratio $1/3$, and their images of $[0,2]$ are the three intervals $[0,2/3]$, $[2/3,4/3]$ and $[4/3,2]$, whose union is $[0,2]$. Hence $[0,2]$ is a compact invariant set of the system, and $S$, being a nonempty compact invariant set as well, equals it by the uniqueness of the attractor, a quotient of *Fractal Geometry*. The difference statement follows from the sum statement and the symmetry $C=1-C$, since $C-C = C+(C-1) = (C+C)-1 = [0,2]-1 = [-1,1]$. $\square$

**Remark (the sense of the tiling).** The identity $C+C=[0,2]$ is the precise sense in which the Cantor set, though of measure zero, tiles the interval additively: the translates and the sums of two of its points fill the interval exactly, and the same holds for differences. At the level of the construction the tiling is visible directly: the level-$k$ set $C_k$ is a union of $2^k$ intervals of length $3^{-k}$, and $C_k + C_k$ is a union of $4^k$ intervals of length $2\cdot3^{-k}$ whose union is the level-$k$ approximation to $[0,2]$; passing to the limit gives the identity. The one-dimensional additive tiling is the simplest case of the tilings of the corpus's self-similar sets, the general theory being that of *Fractal Geometry*.

**Definition.** The **symmetric Cantor set** is the middle-third Cantor set, which is invariant under the reflection $x \mapsto 1-x$ through the midpoint $1/2$. Its fixed set under the reflection is the pair $\{0,1\}$ of endpoints, and the exchanged pairs of points are the pairs $x$, $1-x$; the quotient of $C$ by the reflection is again compact, perfect and totally disconnected, hence homeomorphic to the Cantor set.

**Remark.** The reversible systems and their symmetric attractors, the fixed sets and the exchanged pairs, are the subject of *Reversible Iterated Function Systems and the Involution* and its companion articles in Part III; the symmetric Cantor set is their one-dimensional model, and the statement is recorded here only to name the example. The symmetric self-similar measure on $C$, invariant under the reflection, is the subject of *The Self-Similar Measure and the Involution*.

## Other Self-Similar Subsets of the Line

**Example (the $r$-Cantor set).** Fix $0<r<1/2$ and let $f_1(x)=rx$, $f_2(x)=rx+(1-r)$. The open set condition holds with $V=(0,1)$, and the attractor $C_r$ is a Cantor set of two equal pieces of ratio $r$; its dimension is the similarity dimension solving $2r^s=1$, namely $s = \log2/\log(1/r)$, by the quoted theorem of *Fractal Geometry*. The case $r=1/3$ is the middle-third set; as $r \to 1/2$ the two pieces fill the interval and the set degenerates to $[0,1]$ with dimension $1$; and for every $r<1/2$ the total length of the level-$k$ set is $(2r)^k \to 0$, so the set has measure zero.

**Example (unequal ratios).** Let $f_1(x)=x/2$ and $f_2(x)=x/4+3/4$, so that the pieces $[0,1/2]$ and $[3/4,1]$ are disjoint and the open set condition holds with $V=(0,1)$. The similarity dimension solves

$$
2^{-s} + 4^{-s} = 1,
$$

and writing $t=2^{-s}$ gives $t+t^2=1$, so $t=(\sqrt5-1)/2$ and

$$
s = \frac{\log\varphi}{\log 2} = 0.6942\ldots, \qquad \varphi = \frac{1+\sqrt5}{2},
$$

by the quoted Moran–Hutchinson theorem. The attractor is a Cantor set of unequal pieces, no two scales equal; it shows that the similarity dimension is not restricted to equal ratios and that the level-$k$ pieces need not have the same length.

**Example (the positive-measure case).** Let $C^{\mathrm{fat}}$ be obtained from $[0,1]$ by deleting, from each of the $2^k$ intervals of level $k$, an open middle interval of length $\varepsilon_k3^{-k}$ with $\sum_k 2^k\varepsilon_k3^{-k}<\infty$. The resulting compact set is perfect and totally disconnected, hence homeomorphic to the Cantor discontinuum, but its Lebesgue measure is positive; its box and Hausdorff dimensions are both $1$, the ambient dimension. It is the boundary case between the Cantor sets and the interval, and it is not the attractor of a system of similarities satisfying the open set condition, because the open set condition forces the measure to vanish in this setting; the construction is the **Smith–Volterra–Cantor set**, treated in *Measure and Category*.

**Remark (what the three examples show).** The dimension of a self-similar subset of the line can be any prescribed number in $(0,1)$, attained by choosing the ratios so that $\sum_i r_i^s=1$ for the desired $s$, and the topology alone does not detect it: the middle-third set, the unequal-ratio set and the fat set are all homeomorphic to the Cantor discontinuum, while their dimensions are $0.6309\ldots$, $0.6942\ldots$ and $1$. The dimension is a statement about the chosen distance and the chosen ratios, exactly as the lead article records; the topology of all three is the same.

## Summary

The self-similar subsets of the real line are the attractors of finitely many contractions $f_1,\dots,f_m$, each a similarity $x\mapsto rx+t$ or $x\mapsto -rx+t$, and the prototype is the middle-third Cantor set, the attractor of $x\mapsto x/3$ and $x\mapsto x/3+2/3$. The levels of the middle-third construction are disjoint unions of $2^k$ closed intervals of length $3^{-k}$, of total length $(2/3)^k$, and the limit has measure zero; it is compact, perfect, totally disconnected and uncountable, homeomorphic to the Cantor discontinuum and to the boundary of the binary tree. Every point of the set has a unique base-three expansion with digits in $\{0,2\}$, the map from the digit space to the set is a homeomorphism, and the shift on the digits is the tripling map $x\mapsto 3x\bmod1$. The set tiles the interval additively, $C+C=[0,2]$ and $C-C=[-1,1]$, and it is invariant under the reflection $x\mapsto1-x$, its reversible structure being the one-dimensional model of the symmetric constructions of Part III.

The dimension of the middle-third set is $\log2/\log3$, that of the Sierpiński triangle $\log3/\log2$, and the general self-similar set with the open set condition has the similarity dimension solving $\sum_i r_i^s=1$; these are quoted from the lead article *Fractal Geometry* of Part IV, which owns the Hausdorff and box dimensions, the open set condition and the Moran–Hutchinson theorem, and the present article recomputes only the numbers. The iterated function systems on the line, together with the Hutchinson operator, the address map and the examples as systems, are the subject of *Iterated Function Systems on the Real Line*; the real quadratic family and its bifurcations are the subject of *The Real Quadratic Family and Its Bifurcations*; and the measures carried by these sets are the subject of the category `## Fractal Analysis` of Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $d(x,y)=\lvert x-y\rvert$ | The distance of the line |
| $f_i$, $r_i$, $m$ | The contractions, their ratios, their number |
| $\Lambda$, $\Lambda_w$ | The attractor; the level-$k$ piece of a word $w$ |
| $f_1(x)=x/3$, $f_2(x)=x/3+2/3$ | The two middle-third maps |
| $C_k$, $C$ | The level-$k$ set; the middle-third Cantor set $\bigcap_kC_k$ |
| $\{0,2\}^{\mathbb{N}} \to C$ | The digit coding, a homeomorphism |
| $T_2$, $\partial T_2$ | The full binary tree; its boundary, homeomorphic to $C$ |
| $C+C=[0,2]$, $C-C=[-1,1]$ | The additive tiling by the Cantor set |
| $C_r$, $C^{\mathrm{fat}}$ | The $r$-Cantor set; the positive-measure Smith–Volterra–Cantor set |
| $\log2/\log3$, $\log\varphi/\log2$ | Dimensions, quoted from *Fractal Geometry* |

## Further Reading

- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd edition (Wiley, 2014), for the similarity dimension, the open set condition and the Cantor set.
- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* **30** (1981), 713–747, for the attractor of an iterated function system.
- Patrizia A. P. Moran, "Additive functions of intervals and Hausdorff measure", *Mathematical Proceedings of the Cambridge Philosophical Society* **42** (1946), 15–23, for the exact dimension of a self-similar set.
- Benoit B. Mandelbrot, *The Fractal Geometry of Nature* (Freeman, 1982), for the middle-third set, its arithmetic and its additive properties.
- Georg Cantor, "Über unendliche, lineare Punktmannigfaltigkeiten V", *Mathematische Annalen* **21** (1883), 545–591, for the original construction and the set that bears his name.
- Felix Hausdorff, "Dimension und äußeres Maß", *Mathematische Annalen* **79** (1918), 157–179, for the dimension and the measure of the set.
- John C. Oxtoby, *Measure and Category*, 2nd edition (Springer, 1980), for the Smith–Volterra–Cantor set and the measure-zero and positive-measure constructions.
