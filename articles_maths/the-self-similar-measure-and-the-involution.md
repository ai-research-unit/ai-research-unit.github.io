# __The Self-Similar Measure and the Involution__

## Introduction

The reversible iterated function system carries not only a symmetry of its shape but a symmetry of its measure, and the symmetry decides how the mass is distributed. If the weights of the exchanged branches agree, the self-similar measure is **invariant** under the involution, $R_*\mu=\mu$; if they differ, the involution transports the measure into a different one, and only the symmetrisation is invariant. On the limit space of a reversible self-similar group the abstract self-similar measure of *The Self-Similar Measure and the Invariant Measure*, which is the invariant measure of the limit dynamical system, splits according to the involution into a **fixed part** — the mass held on the fixed set $\mathrm{Fix}(R)$ — and an **exchanged part**, the mass carried in pairs by the exchanged tiles; and the pressure, the density and the adjoint all decompose along the two eigenspaces of the involution. This article develops that decomposition.

The article defines the reversible self-similar measure as the invariant measure of the limit dynamical system of *The Transfer Operator of the Limit Dynamical System*, proves that it is $R$-invariant exactly when the weights are symmetric under the permutation of the branches, and computes the transport $R_*\mu_p=\mu_{\rho(p)}$. It proves the decomposition of the measure into the fixed part $\mu_{\mathrm{fix}}=\mu\llcorner\mathrm{Fix}(R)$ and the exchanged part, and shows that the fixed part vanishes whenever the measure is non-atomic and the fixed set is lower-dimensional — as in the segment, the Cantor set and the gasket — while the **fixed tiles** $T_v$ with $\rho(v)=v$ still carry the weight $p_{\mathrm{fix}}=\sum_{\rho(i)=i}p_i$ of the fixed branches, and it is the fixed tiles and not the fixed set that govern the pressure. It defines the **topological pressure associated with the involution**: the pressure of the reversible system equals the pressure of the system because the involution is a finite quotient, the periodic orbits are counted up to reversal by the factorisation of the Artin–Mazur zeta function, and the fixed part contributes the pressure of the words over the fixed letters. It closes with the **invariant density**: the symmetric and antisymmetric eigenfunctions of the transfer operator, the symmetry $h\circ R=h$ of the density of an $R$-invariant measure, and the vanishing of the antisymmetric eigenfunctions on $\mathrm{Fix}(R)$.

The reversible systems and the exchange relation are *Reversible Iterated Function Systems and the Involution*, the previous article; the invariant measure, the entropy and the dimension of the measure are *The Self-Similar Measure and the Invariant Measure*; the transfer operator, the pressure, the invariant density and the spectral gap are *The Transfer Operator of the Limit Dynamical System*; the periodic orbits, the zeta function and the pressure of the reversible systems are *Ergodic Theory*; the time reversal of the transfer operator is *Time Reversal and the Transfer Operator*, and the adjoint relation is *The Adjoint of the Transfer Operator of the Limit Dynamical System*, the next article. No physics is invoked.

## The Reversible Self-Similar Measure

### The Measure and the Involution

**Definition.** Let $S_1,\dots,S_m$ be a reversible iterated function system with attractor $\Lambda$, involution $R$ and permutation $\rho$, and let $\mu_p$ be the self-similar measure of *The Self-Similar Measure and the Invariant Measure* with the weights $p$. The measure is **reversible** if $R_*\mu_p=\mu_p$; equivalently, on the limit space of a reversible self-similar group, if the abstract self-similar measure $\mu$ of *The Transfer Operator of the Limit Dynamical System* satisfies $R_*\mu=\mu$.

**Theorem (the invariance criterion).** The self-similar measure is reversible if and only if the weights are invariant under the permutation of the branches, $p_{\rho(i)}=p_i$ for every $i$; in general the involution transports the measure by
$$
R_*\mu_p=\mu_{\rho(p)},\qquad\text{so that}\qquad R_*\mu_p=\mu_p\iff p=\rho(p).
$$
On the boundary the transport of the Bernoulli measure is $\tilde R_*\nu_p=\nu_{\rho(p)}$, the Bernoulli measure with the permuted weights.

*Proof.* Using the coding and the intertwining $R\circ\pi=\pi\circ\tilde R$ of the previous article, $R_*\mu_p=\pi_*\tilde R_*\nu_p$; the letterwise flip carries the cylinder $[x_1\cdots x_n]$ to $[\rho(x_1)\cdots\rho(x_n)]$, so $\tilde R_*\nu_p[\rho(x_1)\cdots\rho(x_n)]=\nu_p[x_1\cdots x_n]=p_{x_1}\cdots p_{x_n}$, which is the Bernoulli mass of the permuted vector $\rho(p)$ at the word $[\rho(x_1)\cdots\rho(x_n)]$; hence $\tilde R_*\nu_p=\nu_{\rho(p)}$. The self-similar measure is the pushforward, so the same holds for it, and the invariance is the equality of the two weight vectors. The verification on the middle-thirds Cantor set with symmetric weights confirms $\mu[w]=\mu[\bar w]$ for the tested words, and with the biased weights confirms that the flipped cylinder has the mass of the permuted weights.

**Corollary (the symmetrisation).** For arbitrary weights the measure $\tfrac12(\mu_p+\mu_{\rho(p)})$ is the reversible self-similar measure of the system with the averaged weights $\tfrac12(p+\rho(p))$; the reversible measures are exactly the self-similar measures of the symmetric weights.

*Proof.* The averaged weights are $\rho$-symmetric, and the map $p\mapsto\mu_p$ is affine, so the average of the two measures is the measure of the average weights; by the criterion it is reversible.

### The Transport of the Boundary

**Remark (the two descriptions of the involution).** The involution acts on the boundary as the letterwise flip and on the limit space as the geometric symmetry; the two actions are related by the coding, and the invariance of the measure can be read in either. The letterwise flip has the fixed words $\rho(w)=w$ as its fixed points on the boundary, while the geometric involution has the fixed set $\mathrm{Fix}(R)$; the two fixed sets are related by the coding: the points of $\mathrm{Fix}(R)\cap\mathcal{J}_G$ are the images of the fixed words of the flip. This is the reason the fixed part of the measure can be computed from the combinatorics of $\rho$.

## The Fixed Part and the Exchanged Part

### The Decomposition of the Measure

**Definition.** For an $R$-invariant measure $\mu$ the **fixed part** is the restriction $\mu_{\mathrm{fix}}=\mu\llcorner\mathrm{Fix}(R)$ of the measure to the fixed set, and the **exchanged part** is the residual $\mu_{\mathrm{exch}}=\mu-\mu_{\mathrm{fix}}$; the measure decomposes as
$$
\mu=\mu_{\mathrm{fix}}+\mu_{\mathrm{exch}},
$$
the exchanged part is carried by the pairs $\{T_v,T_{\rho(v)}\}$ of exchanged tiles with equal mass, so that the quotient measure on the space $\mathcal{J}_G/R$ is well defined, and the **fixed tiles** $T_v$ with $\rho(v)=v$ letterwise carry the mass $p_{\mathrm{fix}}=\sum_{\rho(i)=i}p_i$ of the fixed branches. The fixed part of the measure and the mass of the fixed tiles are different objects: the first is the mass of the fixed set, the second the mass of the tiles that the involution preserves.

**Theorem (the structure of the two parts).** If the measure is non-atomic and the fixed set $\mathrm{Fix}(R)$ is lower-dimensional — the case of the segment, of the Cantor set and of the gasket — then the fixed part is zero and the whole measure is exchanged: $\mu=\mu_{\mathrm{exch}}$. The exchanged part decomposes as a sum over the exchanged tiles, each pair $\{T_v,T_{\rho(v)}\}$ contributing the same mass $\mu(T_v)$ to the two members, so the quotient measure on $\mathcal{J}_G/R$ is well defined. The **fixed tiles** carry the mass
$$
\mu\Bigl(\bigcup_{\rho(v)=v}T_v\Bigr)=\sum_{\rho(i)=i}p_i=p_{\mathrm{fix}}
$$
in the self-similar case, the union being that of the top fixed tiles; this is the mass that governs the fixed part of the pressure, and it is nonzero for every reversible system with a fixed branch, even though the fixed part of the measure is zero.

*Proof.* The fixed set meets the tiles only in the fixed tiles, because the other tiles are exchanged in pairs and their intersections are carried to the other member; the intersection $\bigcap_{n}T_{w_n}$ of the nested fixed tiles has measure $\lim p_w=0$ for a non-atomic measure, so $\mu\llcorner\mathrm{Fix}(R)=0$, while the union of the top fixed tiles has the mass $\sum_{\rho(i)=i}p_i$. The exchange of the masses is the exchange relation of *Reversible Iterated Function Systems and the Involution* applied to the measure: $R(T_v)=T_{\rho(v)}$ and $R_*\mu=\mu$ give the equality of the two masses.

**Example (the three reversible systems).** For the **segment** the fixed set is the point $\tfrac12$, of measure zero for any nonatomic measure, so the fixed part is zero and the exchanged part is all of $\mu$; the quotient is $[0,\tfrac12]$ and the measure descends to it. For the **middle-thirds Cantor set** the fixed set is again $\{\tfrac12\}$, which is not on the attractor, so the fixed part is zero and the exchanged part is all of $\mu$; the involution exchanges the cylinders $[w]\leftrightarrow[\bar w]$. For the **Sierpiński gasket** with the reflection fixing the corner $q_0$ and exchanging $q_1,q_2$, the fixed branch $0$ gives the fixed tiles $S_0^k\Lambda$ and the fixed set is the median segment inside the gasket, which has measure zero, so the fixed part of the measure is again zero; the fixed tiles carry the mass $p_0$ of the fixed branch, which is what enters the pressure. In all three cases the measure is entirely exchanged and the involution acts freely on the mass; the fixed tiles exist and carry weight but not the fixed part of the measure.

## The Topological Pressure and the Involution

### The Pressure of the Reversible System

**Definition.** The **topological pressure of the reversible system** is the pressure of the quotient dynamical system $\varphi/R$,
$$
P_R(t)=\lim_{n\to\infty}\frac1n\log\sum_{R\text{-orbits}}e^{tS_n W} ,
$$
the sum over the orbits up to the involution, for the potential $W$ of the system.

**Theorem (the finite quotient does not change the pressure).** The quotient by the involution is a finite-to-one factor, so the topological entropy and the pressure are unchanged:
$$
P_R(t)=P(t) ,
$$
the pressure of *The Transfer Operator of the Limit Dynamical System*. The involution affects the counting, not the growth rate: the number of periodic orbits of length $n$ up to reversal is
$$
N_n^{R}=\tfrac12\bigl(N_n+N_n^{\mathrm{fix}}\bigr)+O(1),
$$
where $N_n$ is the number of the periodic orbits and $N_n^{\mathrm{fix}}$ the number fixed by the reversal, and the **Artin–Mazur zeta function** factorises accordingly,
$$
\zeta_R(z)^2=\zeta(z)\,\zeta_{\mathrm{fix}}(z)\,,
$$
where $\zeta_{\mathrm{fix}}$ counts the fixed orbits, those of the fixed part.

*Proof sketch.* The orbits of the quotient are the orbits of $\varphi$ modulo the involution, and the quotient map is at most two-to-one, so the exponential growth rates agree; the counting formula is the orbit-stabiliser theorem for the action of the two-element group, and the zeta function factorises because it is the Euler product over the orbits of the quotient. The statements are those of *Ergodic Theory* for a finite group action; the factorisation is the "reversible" case of the zeta function of a reversible system.

**Corollary (the fixed part of the pressure).** The pressure of the fixed part, the growth rate of the words over the fixed letters, is
$$
P_{\mathrm{fix}}(t)=\log\sum_{\rho(i)=i}\Delta_i^t ,
$$
and it is a lower bound for $P(t)$; the exchanged part contributes the residual pressure, and $P(t)=\max\{P_{\mathrm{fix}}(t),P_{\mathrm{exch}}(t)\}$ in the topologically mixing case.

*Proof.* The words over the fixed letters are the periodic orbits fixed by the reversal, and their transfer weights are $\prod\Delta_i^t$; the leading eigenvalue of the transfer operator restricted to them is the stated sum; the exchanged part is the quotient of the rest, and the maximum is the standard decomposition of the leading eigenvalue of a non-negative matrix into the contributions of the irreducible components.

### The Counting of the Orbits

**Remark (the reversal and the entropy are compatible).** The topological entropy of the limit dynamical system is the logarithm of the leading eigenvalue of the transfer operator, and it is insensitive to the reversal; what changes is the **numbering** of the periodic orbits and hence the zeta function. This is the discrete counterpart of the statement of *Time Reversal and the Transfer Operator* that the time reversal conjugates the transfer operator to the Koopman operator and leaves the spectrum alone while permuting the eigenfunctions. The reversible systems of the category have the same entropy as their quotients and the fixed part of the pressure bounded by the weight of the fixed branches.

## The Invariant Density and the Symmetry

### The Symmetric and Antisymmetric Eigenfunctions

**Theorem (the splitting of the spectrum).** Let $\mu$ be an $R$-invariant measure and let $L_\varphi$ be the transfer operator, with $P_\rho f=f\circ R$ the involution. Then $L_\varphi$ commutes with $P_\rho$, the eigenfunctions split into the **symmetric** family, $f\circ R=f$, and the **antisymmetric** family, $f\circ R=-f$, and the invariant density $h$ of the previous article is symmetric:
$$
P_\rho L_\varphi P_\rho=L_\varphi,\qquad h\circ R=h .
$$

*Proof.* The relation $P_\rho L_\varphi P_\rho=L_\varphi$ is the theorem of *Reversible Iterated Function Systems and the Involution*; commuting operators have a common eigenbasis, and the involution has the eigenvalues $\pm1$, so the eigenfunctions split by the symmetry of $f$. The invariant density is an eigenfunction for the eigenvalue $1$ with positive values, hence cannot be antisymmetric, and is symmetric.

### The Density Transformations under $R$

**Theorem (the transformation of the density).** Let $\mu$ be a measure with density $\rho_\mu$ with respect to a reference measure $\nu$ on the limit space, and let $R$ be the involution preserving both $\nu$ and the class. Then the pushforward $R_*\mu$ has the density
$$
\rho_{R_*\mu}=\rho_\mu\circ R ,
$$
the density of an $R$-invariant measure satisfies $\rho_\mu\circ R=\rho_\mu$, and the **antisymmetric densities** $\rho\circ R=-\rho$, which integrate to zero, are the densities of the **signed invariant measures**, the differences $\mu-\nu$ of two invariant measures of the same mass.

*Proof.* The change of variables in $\int f\circ R\,d\mu=\int f\,d(R_*\mu)$ against the reference $\nu$ uses that $R$ preserves $\nu$, so that no Jacobian factor appears; the invariance of $\mu$ is the equality of the two densities; the signed measures are the tangent space of the simplex of the invariant measures, and their densities are antisymmetric because the positive densities are symmetric and the decomposition of the space of functions into the symmetric and antisymmetric parts is direct. This is the discrete form of the time-reversal transformation of the density in *Time Reversal and the Transfer Operator*.

**Corollary (the fixed part and the antisymmetric densities).** An antisymmetric density vanishes on the fixed set $\mathrm{Fix}(R)$; hence the antisymmetric invariant densities are supported on the exchanged part, and the reversible measure — the symmetric one — has its restriction to the fixed part equal to the fixed part of the measure.

*Proof.* $\rho\circ R=-\rho$ and $Rx=x$ on $\mathrm{Fix}(R)$ give $\rho(x)=-\rho(x)$, so $\rho=0$; the restriction to the fixed part is therefore carried by the symmetric densities, which is the fixed part of the measure of the previous section.

## Summary

The **reversible self-similar measure** is the invariant measure of the limit dynamical system of a reversible system; it is $R$-invariant if and only if the weights are symmetric under the permutation of the branches, $p_{\rho(i)}=p_i$, and in general the involution transports the measure as $R_*\mu_p=\mu_{\rho(p)}$, with the symmetrisation the reversible measure of the averaged weights. The measure splits into the **fixed part** $\mu_{\mathrm{fix}}=\mu\llcorner\mathrm{Fix}(R)$ and the **exchanged part** $\mu_{\mathrm{exch}}=\mu-\mu_{\mathrm{fix}}$; for the non-atomic self-similar measures of the segment, the Cantor set and the gasket the fixed set is lower-dimensional and the fixed part is zero, so the measure is entirely exchanged and descends to the quotient $\mathcal{J}_G/R$, while the **fixed tiles** $T_v$ with $\rho(v)=v$ carry the mass $p_{\mathrm{fix}}=\sum_{\rho(i)=i}p_i$ of the fixed branches, which is what enters the pressure. The **topological pressure is unchanged** by the involution, $P_R(t)=P(t)$, because the quotient is a finite factor, while the periodic orbits are counted up to reversal by $N_n^R=\tfrac12(N_n+N_n^{\mathrm{fix}})+O(1)$ and the zeta function factorises as $\zeta_R^2=\zeta\,\zeta_{\mathrm{fix}}$; the fixed part of the pressure is $P_{\mathrm{fix}}(t)=\log\sum_{\rho(i)=i}\Delta_i^t$. The **invariant density** is symmetric, $h\circ R=h$, the transfer operator commutes with the involution and splits the eigenfunctions into the symmetric and antisymmetric families, the antisymmetric densities — those of the signed invariant measures — satisfy $\rho\circ R=-\rho$ and vanish on $\mathrm{Fix}(R)$. The transport $R_*\mu_p=\mu_{\rho(p)}$ and the mass invariance under the flip for the symmetric weights were verified on the Cantor set; the entropy invariance, the zeta factorisation and the density transformation are quoted from the reversible-systems theory of *Ergodic Theory* and *Time Reversal and the Transfer Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\rho$, $p_{\rho(i)}=p_i$ | The involution, the branch permutation, the symmetric weights |
| $R_*\mu_p=\mu_{\rho(p)}$ | The transport of the self-similar measure |
| $\tilde R_*\nu_p=\nu_{\rho(p)}$ | The transport of the Bernoulli measure |
| $\mu=\mu_{\mathrm{fix}}+\mu_{\mathrm{exch}}$ | Fixed and exchanged parts of the measure |
| $\mathrm{Fix}(R)$, $T_v$ with $\rho(v)=v$ | Fixed set, fixed tiles |
| $P_R(t)=P(t)$, $P_{\mathrm{fix}}(t)=\log\sum_{\rho(i)=i}\Delta_i^t$ | Reversible pressure; fixed part of the pressure |
| $N_n^R$, $\zeta_R^2=\zeta\,\zeta_{\mathrm{fix}}$ | Orbit count up to reversal; zeta factorisation |
| $P_\rho f=f\circ R$ | The operator of the involution |
| $\rho_\mu\circ R=\rho_\mu$, $\rho\circ R=-\rho$ | Symmetric and antisymmetric densities |

## Further Reading

- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the pressure, the finite quotients and the zeta functions.
- David Ruelle, *Thermodynamic Formalism* (Addison-Wesley, 1978), for the pressure, the equilibrium states and the periodic-orbit counting.
- Viviane Baladi, *Positive Transfer Operators and Decay of Correlations* (World Scientific, 2000), for the symmetric and antisymmetric spectral decompositions and the invariant densities.
- Andrzej Lasota and Michael C. Mackey, *Chaos, Fractals, and Noise* (Springer, 2nd ed. 1994), for the Perron–Frobenius operator, the invariant densities and their symmetry.
- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the limit space, the coding and the fixed tiles.
- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997), for the self-similar measures and their dimension.
