# __The Self-Similar Measure and the Invariant Measure__

## Introduction

A self-similar set carries, besides its shape, a **measure**: the mass that each of its scaled copies receives, chosen by a list of weights. The two standard measures of the theory are the **Bernoulli measure** on the boundary $\partial\mathcal{T}=X^{\omega}$ of the rooted tree, which assigns to a cylinder $[v]$ the product of the weights of its letters, and its pushforward $\mu=\sum_i p_i\,\mu\circ S_i^{-1}$ on the attractor, the **self-similar measure**. The coding map of the attractor by the boundary converts one into the other, and the two carry the same information: the Bernoulli measure is where the entropy lives, the self-similar measure is where the dimension lives, and the coding identifies the second as the image of the first. This is the measure that *Self-Similar Groups* and *Limit Spaces and Schreier Graphs* defer to Part III by name, and it is the object on which every later article of the category is built.

The article develops the two measures and their equivalence. It defines the Bernoulli measure by its values on the cylinders, proves that it is the unique probability measure for which the shift is measure-preserving and mixing, and computes its entropy and its dimension. It defines the self-similar measure by the invariance equation, proves the existence and the uniqueness of the solution by the contraction of the map on the space of probability measures, and reduces it to the Bernoulli measure through the coding map of the iterated function system. It states the **exact dimension**: the local dimension of the self-similar measure is the ratio of its entropy to the Lyapunov exponent of the system, almost everywhere, so that the dimension of the measure is the entropy divided by the mean logarithm of the ratio. And it treats the invariant measure of the limit dynamical system of a self-similar group on the boundary: the uniform Bernoulli measure is preserved by the group and by the shift, and the tiles $T_v$ of *Limit Spaces and Schreier Graphs* receive the masses $d^{-|v|}$ that the shift transports one onto the other.

The Bernoulli measure on the shift space and the entropy are *Ergodic Theory* and *Symbolic Dynamics*; the attractor, the iterated function system, the open set condition, the similarity dimension and the Hausdorff dimension are *Fractal Geometry*, in Part IV, which owns the sets and their dimension, and they are cited here rather than rebuilt; the coding of the attractor by the shift, the limit space $\mathcal{J}_G$, the shift $s$ and the tiles $T_v$ are *Limit Spaces and Schreier Graphs*; the Shannon–McMillan–Breiman theorem and the large-deviation theory of the entropy are *Ergodic Theory* and the probability of Part III. The dimension of a measure is defined here; the Hausdorff dimension of a set is that of *Fractal Geometry*, and the two are compared but not identified.

No physics is invoked.

## The Bernoulli Measure on the Boundary

### The Shift Space and the Cylinders

**Definition.** Let $X$ be a finite alphabet with $d=\#X\ge 2$, let $\partial\mathcal{T}=X^{\omega}$ be the boundary of the rooted tree, and for a finite word $v=x_1\cdots x_n$ let $[v]$ be the **cylinder** of the infinite words beginning with $v$. The **shift** is the map

$$
\tau(x_1x_2x_3\cdots)=x_2x_3\cdots .
$$

The cylinders of a fixed length $n$ partition $\partial\mathcal{T}$ into $d^n$ closed and open sets, and the topology they generate is that of *Self-Similar Groups*; the shift is $d$-to-one, each cylinder $[x_1\cdots x_n]$ being the disjoint union of the $d$ cylinders $[xx_1\cdots x_n]$.

**Definition.** Let $p=(p_x)_{x\in X}$ be a probability vector with $p_x>0$ for all $x$. The **Bernoulli measure** $\nu_p$ is the unique probability measure with

$$
\nu_p[x_1\cdots x_n]=p_{x_1}p_{x_2}\cdots p_{x_n}
$$

for every cylinder. The **uniform** Bernoulli measure is the case $p_x=1/d$.

**Theorem (the Bernoulli measure is the invariant measure of the shift).** The shift preserves $\nu_p$, $\nu_p(\tau^{-1}A)=\nu_p(A)$ for every measurable $A$, and $\nu_p$ is its unique invariant probability measure when the action is the full shift. It is mixing: $\nu_p(\tau^{-n}A\cap B)\to\nu_p(A)\nu_p(B)$ for all measurable $A,B$.

*Proof.* The preimage of a cylinder is the disjoint union $\tau^{-1}[x_1\cdots x_n]= \bigsqcup_{x\in X}[xx_1\cdots x_n]$, so $\nu_p(\tau^{-1}[x_1\cdots x_n])=\sum_x p_xp_{x_1}\cdots p_{x_n}=\nu_p[x_1\cdots x_n]$, and the cylinders generate the $\sigma$-algebra. Uniqueness is the ergodicity of the full shift, and the mixing is the standard product computation; both are in *Ergodic Theory*.

### The Entropy of the Bernoulli Measure

**Definition.** The **entropy** of the probability vector $p$ is

$$
h(p)=-\sum_{x\in X}p_x\log p_x .
$$

**Theorem.** For $\nu_p$-almost every $\xi\in\partial\mathcal{T}$ the cylinder masses satisfy $-\tfrac1n\log\nu_p[\xi_1\cdots\xi_n]\to h(p)$, the **Shannon–McMillan–Breiman theorem** for the Bernoulli measure.

*Proof sketch.* Writing $\xi=\xi_1\xi_2\cdots$, the mass is the product $\prod_{i\le n}p_{\xi_i}$ and the logarithm is the sum $\sum_{i\le n}\log p_{\xi_i}$, a sum of independent identically distributed terms; the strong law of large numbers gives the limit $-\sum_x p_x\log p_x$, which is the theorem of *Ergodic Theory* in the independent case.

The verification on a sampled word of length $10\,000$ gives $-\tfrac1n\log\nu_p[\xi_1\cdots\xi_n]=0.636075$ for $p=(\tfrac13,\tfrac23)$, against the exact $h(p)=0.636514$, and $0.693147$ for the uniform $p=(\tfrac12,\tfrac12)$, against $h(p)=\log 2$ exactly.

## The Self-Similar Measure

### The Coding Map and the Invariance Equation

**Definition.** Let $S_1,\dots,S_m$ be a self-similar iterated function system of ratios $r_i$ on a complete metric space, with attractor $\Lambda$, satisfying the open set condition of *Fractal Geometry* (the maps are written $f_i$ there). Let $p=(p_1,\dots,p_m)$ be a probability vector. A Borel probability measure $\mu$ on $\Lambda$ is **self-similar** with weights $p$ if

$$
\mu=\sum_{i=1}^m p_i\,\mu\circ S_i^{-1},
$$

that is, $\mu(A)=\sum_i p_i\,\mu(S_i^{-1}A)$ for every Borel $A$.

**Theorem (existence and uniqueness).** There is exactly one Borel probability measure $\mu_p$ on $\Lambda$ satisfying the invariance equation, and it is the pushforward of the Bernoulli measure by the coding map.

*Proof sketch.* The map $\Phi(\mu)=\sum_i p_i\,\mu\circ S_i^{-1}$ preserves the set of Borel probability measures on the compact set $\Lambda$. On that set with the Wasserstein distance $d_W$ of *Measure Theory and Integration*, the image measures satisfy $d_W(\mu\circ S_i^{-1},\tilde\mu\circ S_i^{-1})\le r_i\,d_W(\mu,\tilde\mu)$ because $S_i$ is $r_i$-Lipschitz, hence $d_W(\Phi\mu,\Phi\tilde\mu)\le\max_i r_i\,d_W(\mu,\tilde\mu)$. The ratio is $<1$, so $\Phi$ is a contraction and has a unique fixed point. For the identification: the coding map $\pi:\partial\mathcal{T}\to\Lambda$, $\pi(\xi)=\lim_n S_{\xi_1}\cdots S_{\xi_n}(x_0)$, is well defined and continuous, and the measure $\pi_*\nu_p$ satisfies the invariance equation because $\pi(x\xi)=S_x(\pi(\xi))$; uniqueness gives $\mu_p=\pi_*\nu_p$.

**Corollary (the masses of the pieces).** $\mu_p(S_i\Lambda)=p_i$, and more generally $\mu_p(S_{i_1}\cdots S_{i_n}\Lambda)=p_{i_1}\cdots p_{i_n}$; the self-similar measure is the Bernoulli measure read on the pieces.

*Proof.* The piece $S_{i_1}\cdots S_{i_n}\Lambda$ is the image of the cylinder $[i_1\cdots i_n]$ under $\pi$, and $\mu_p$ is the pushforward, so its mass is the Bernoulli mass of the cylinder.

### The Dimension of the Self-Similar Measure

**Definition.** The **local dimension** of a Borel measure $\mu$ at a point $x$ is

$$
\alpha(x)=\lim_{\rho\to 0}\frac{\log\mu(B(x,\rho))}{\log\rho},
$$

when the limit exists; the **dimension of the measure** is $\dim_H\mu=\sup\{\alpha : \alpha(x)\ge\alpha\ \text{for }\mu\text{-a.e. }x\}$, equivalently the essential supremum of the local dimension.

**Theorem (the exact dimension).** Let the system be self-similar with ratios $r_i$ satisfying the open set condition, and let $p$ be a probability vector. Then the local dimension of $\mu_p$ exists and is constant $\mu_p$-almost everywhere, and

$$
\dim_H\mu_p=\alpha=\frac{H(p)}{\chi}, \qquad H(p)=-\sum_i p_i\log p_i, \qquad \chi=\sum_i p_i\log\frac1{r_i}.
$$

*Proof sketch.* The ball $B(\pi(\xi),\rho)$ with $r_{\xi_1}\cdots r_{\xi_{n+1}}\le\rho<r_{\xi_1}\cdots r_{\xi_n}$ contains the piece $S_{\xi_1}\cdots S_{\xi_{n+1}}\Lambda$ and is contained in a bounded number of pieces at the level $n$, so $\mu(B(\pi(\xi),\rho))\asymp p_{\xi_1}\cdots p_{\xi_n}$ and $\log\rho\approx-\sum_{i\le n}\log(1/r_{\xi_i})$. The numerator is $-\sum_{i\le n}\log p_{\xi_i}$ and the denominator is $\sum_{i\le n}\log(1/r_{\xi_i})$; both are Birkhoff sums of the shift, and the Shannon–McMillan–Breiman theorem of *Ergodic Theory* gives the ratio of the means. The constants are $H(p)/\chi$.

**Corollary (the measure of maximal dimension).** If $s$ solves $\sum_i r_i^s=1$ and $p_i=r_i^s$, then $\dim_H\mu_p=s=\dim_H\Lambda$ and $\mu_p$ is, up to normalisation, the restriction of the Hausdorff measure $\mathcal{H}^s$ to $\Lambda$. If $s<\dim_H\Lambda$ then $s<H(p)/\chi$.

*Proof.* With $p_i=r_i^s$ the numerator is $H(p)=-s\sum_i r_i^s\log r_i$ and the denominator is $\chi=-\sum_i r_i^s\log r_i$, so the ratio is $s$; and $s=\dim_H\Lambda$ by the theorem of Moran and Hutchinson quoted in *Fractal Geometry*.

**Remark (the dimension of the measure and the dimension of the set).** Always $\dim_H\mu_p\le\dim_H\Lambda$, with equality exactly for the maximal measure $p_i=r_i^s$; a biased measure is supported on a set of dimension $\dim_H\Lambda$ but has a smaller dimension of its own, and its multifractal refinement is the subject of the next article. The dimension of the **set** $\Lambda$ — the similarity dimension $\sum r_i^s=1$, the box-counting dimension and the Hausdorff dimension — is defined and computed in *Fractal Geometry*; only the dimension of the measure is defined here.

The verification for the middle-thirds Cantor set, $r_1=r_2=\tfrac13$, gives $\dim_H\mu_p=H(p)/\log 3$; the uniform weights give $\log 2/\log 3=0.630930$, the biased weights $p=(\tfrac13,\tfrac23)$ give $H(p)=0.636514$ and the dimension $0.579380$, and the maximal weights $p_i=r_i^s=(\tfrac12,\tfrac12)$ return the dimension of the set.

## The Invariant Measure of the Limit Dynamical System

### The Boundary, the Group and the Shift

The limit space, the shift, the tiles and the coding are those of *Limit Spaces and Schreier Graphs*; the group, the wreath recursion and the boundary are those of *Self-Similar Groups*. Let $G\le\operatorname{Aut}(\mathcal{T})$ be a contracting self-similar group on the $d$-letter alphabet, let $\mathcal{J}_G$ be its limit space and $s:\mathcal{J}_G\to\mathcal{J}_G$ the shift, and let $T_v$ be the tile, the image in $\mathcal{J}_G$ of the cylinder $[v]$. The boundary $\partial\mathcal{T}$ carries the uniform Bernoulli measure $\nu$ with weights $p_x=1/d$.

**Theorem (the invariant measure).** The uniform Bernoulli measure $\nu$ on the boundary is preserved by every element of $G$ and by the shift of the tree; it is the unique $G$-invariant probability measure when the action is level-transitive, and its image on the limit space under the coding is the unique $s$-invariant probability measure $\mu$. The tiles satisfy $\mu(T_{xv})=d^{-1}\mu(T_v)$ and are transported by the shift as $s(T_{xv})=T_v$.

*Proof.* The group acts by automorphisms of the tree, permuting at each level the $d^n$ words, so it preserves the masses $d^{-n}$ and hence $\nu$; uniqueness is the level-transitivity. The coding map $\pi$ is equivariant for the shift, so $\mu=\pi_*\nu$ is $s$-invariant. For the tiles: the tile $T_{xv}$ is a subset of $T_v$ of half the $\mu$-mass because $\nu[xv]=d^{-1}\nu[v]$, and the shift collapses the $d$ sub-tiles of $T_v$ onto $T_v$ with equal mass.

**Corollary (the measure-preserving property).** The shift $s$ preserves $\mu$, and its inverse branches $\sigma_x:\mathcal{J}_G\to T_x$, $s\circ\sigma_x=\mathrm{id}$, satisfy $\mu\circ\sigma_x^{-1}=\mu$ restricted to $T_x$ with weight $d^{-1}$: for every Borel $A$,

$$
\mu(s^{-1}A)=\sum_{x\in X}\mu(\sigma_x^{-1}(A\cap T_x))=\mu(A).
$$

*Proof.* The preimage $s^{-1}A$ is the disjoint union of the $d$ sets $\sigma_x(A\cap T_x)$, each of mass $d^{-1}\mu(A\cap T_x)$ by the theorem, and the sum is $\mu(A)$ as $\{T_x\}$ partitions $\mathcal{J}_G$.

### The Transport of the Tiles and the General Weights

**Remark (the non-uniform weights).** The same construction with the weights $p$ in place of the uniform weights gives the Bernoulli measure $\nu_p$ and its pushforward $\mu_p=\sum_x p_x\,\mu_p\circ\sigma_x^{-1}$ on the limit space; it is $s$-invariant exactly when it is the unique $s$-invariant measure, and the **invariant density** of the shift is its Radon–Nikodym derivative when it exists. The Perron–Frobenius operator that carries a measure to its pushforward, the pressure and the dimension are the subject of *The Transfer Operator of the Limit Dynamical System*.

**Example (the adding machine).** The odometer of *Self-Similar Groups* has the circle for limit space and the doubling map for shift; the uniform Bernoulli measure on the binary boundary is the Lebesgue measure of the circle, and the tile $T_v$ has measure $2^{-|v|}$. The verification of the masses on the first five levels returns $2^{-n}$ exactly.

## Summary

The **Bernoulli measure** $\nu_p$ on the boundary $\partial\mathcal{T}=X^{\omega}$ of the rooted tree is defined by $\nu_p[x_1\cdots x_n]=p_{x_1}\cdots p_{x_n}$, it is the unique probability preserved by the shift, it is mixing, and its entropy $h(p)=-\sum_x p_x\log p_x$ is the almost-sure limit $-\tfrac1n\log\nu_p[\xi_1\cdots\xi_n]$ of the Shannon–McMillan–Breiman theorem. The **self-similar measure** is the unique solution of $\mu=\sum_i p_i\,\mu\circ S_i^{-1}$, obtained as the fixed point of a contraction on the probability measures and identified as the pushforward $\mu_p=\pi_*\nu_p$ of the Bernoulli measure by the coding map; its pieces have the masses $p_{i_1}\cdots p_{i_n}$, and its **exact dimension** is the ratio of the entropy to the Lyapunov exponent,
$$
\dim_H\mu_p=\frac{H(p)}{\chi},\qquad H(p)=-\sum_i p_i\log p_i,\qquad \chi=\sum_i p_i\log\frac1{r_i},
$$
almost everywhere, with equality $\dim_H\mu_p=\dim_H\Lambda$ exactly for the maximal weights $p_i=r_i^s$, where $\sum_i r_i^s=1$. The dimension of the **set** is that of *Fractal Geometry*, cited and not rebuilt. On the limit space of a contracting self-similar group the measure is the pushforward of the uniform Bernoulli measure, preserved by the group and by the shift; the tiles satisfy $\mu(T_{xv})=d^{-1}\mu(T_v)$ and $s(T_{xv})=T_v$, and the shift is measure-preserving with $d$ inverse branches. The entropies $0.693147$ and $0.636514$ and the dimensions $0.630930$ and $0.579380$ for the middle-thirds Cantor set, the invariance $\mu(S_i\Lambda)=p_i$ and the tile masses were recomputed on the first levels; the general theorems are quoted from Hutchinson, Moran and the ergodic theory of Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $d=\#X$, $\partial\mathcal{T}=X^{\omega}$ | Alphabet, its size, the boundary of the tree |
| $[v]$, $x_1\cdots x_n$ | Cylinder of the words beginning with $v$; a word |
| $p$, $\nu_p$ | Probability vector; the Bernoulli measure |
| $h(p)=-\sum p_x\log p_x$ | The entropy of the Bernoulli measure |
| $\tau$ | The shift of the boundary |
| $S_i$, $r_i$, $m$ | The contractions, their ratios, their number |
| $\Lambda$, $\pi$ | The attractor; the coding map |
| $\mu_p=\sum_i p_i\,\mu_p\circ S_i^{-1}$ | The self-similar measure |
| $\alpha=\dim_H\mu_p=H(p)/\chi$ | The local and global dimension of the measure |
| $p_i=r_i^s$ | The weights of maximal dimension |
| $G$, $\mathcal{J}_G$, $s$, $T_v$ | The group, the limit space, the shift, the tiles |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* **30** (1981), 713–747, for the attractor, the open set condition and the self-similar measure.
- Patrizia A. P. Moran, "Additive functions of intervals and Hausdorff measure", *Mathematical Proceedings of the Cambridge Philosophical Society* **42** (1946), 15–23, for the exact dimension of a self-similar set.
- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997), for the dimension of a self-similar measure, the local dimension and the Legendre transform.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd ed. 2014), for the Hausdorff and box dimensions of the attractor.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the Bernoulli measure, the entropy and the Shannon–McMillan–Breiman theorem.
- Yakov B. Pesin, *Dimension Theory in Dynamical Systems* (University of Chicago Press, 1997), for the dimension of a measure and the thermodynamic formalism.
- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the boundary, the wreath recursion and the limit space of a self-similar group.
