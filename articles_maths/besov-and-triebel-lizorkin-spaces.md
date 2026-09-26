
# __Besov and Triebel–Lizorkin Spaces__

## Introduction

The Sobolev space $W^{k,p}$ measures the smoothness of a function by the square integrability of its derivatives and so measures smoothness and integrability with two indices, the order of differentiation and the exponent of the norm. There is a third and finer invariant of smoothness, the way in which the $L^p$ norms of the successive frequency components of the function decay, and the spaces that record it are the **Besov spaces** $B^s_{p,q}$ and the **Triebel–Lizorkin spaces** $F^s_{p,q}$: three indices now, smoothness $s$, integrability $p$ and a fine index $q$ that measures the distribution of the smoothness across the dyadic frequency scales. The Sobolev spaces are the case $q=2$ of the Triebel–Lizorkin family, the Hölder spaces are the case $p=q=\infty$ of the Besov family, the Hardy space $H^1$ and the space $\mathrm{BMO}$ of bounded mean oscillation are the borderline members $F^0_{1,2}$ and $F^0_{\infty,2}$, and the Besov spaces are the natural class in which the real interpolation of the Sobolev scale is closed.

The article develops the theory from the **Littlewood–Paley decomposition**. A dyadic partition of unity $\{\varphi_j\}_{j\ge0}$ in the frequency variable decomposes a tempered distribution into its frequency layers $\varphi_j(D)f$, and the two families of spaces are defined by the size of the sequences or functions $2^{js}\varphi_j(D)f$ in the appropriate mixed norm: the Besov norm is the $\ell^q$ norm in $j$ followed by the $L^p$ norm in $x$, and the Triebel–Lizorkin norm is the $L^p$ norm followed by the $\ell^q$ norm, so the two differ exactly in the order of the two operations, and coincide only when $p=q$. The theory then consists of the independence of the definition from the partition, the elementary properties of the two scales and their comparison with the classical spaces, the lifting and the Fourier-multiplier properties, the embeddings and the compactness, the trace theorem on a hyperplane, the atomic and molecular decompositions in which the norm is computed from the coefficients of a single expansion, and the interpolation theorems that place the scale exactly at the real and complex interpolation of the Sobolev spaces. The **Bony paraproduct** and the product estimates that follow from the decomposition are recorded, because they are the reason the Besov scale is the natural one for the nonlinear estimates of the theory of partial differential equations.

The Fourier transform, the Schwartz space, the tempered distributions, the Littlewood–Paley maximal function and the Calderón–Zygmund theory are those of *Fourier Analysis on Euclidean Spaces*; the distributional calculus and the convolution of distributions are those of *Distributions and Fundamental Solutions*; the real and complex interpolation methods, and the interpolation of the Sobolev scale, are those of *Interpolation Theory*, to which this article is the supplement of the function spaces. The weak derivatives and the Sobolev spaces $W^{k,p}$ are recalled here in line, as the classical spaces with which the new scales are compared; their systematic development is subsequent to this article, and the scales of this article do not depend on it. The applications of the spaces to elliptic boundary problems, to nonlinear equations and to the calculus of variations are not treated here.

No physics is invoked.

## The Littlewood–Paley Decomposition

### Dyadic Partitions of Unity

**Definition.** A sequence $(\varphi_j)_{j\ge0}$ in the Schwartz class $\mathcal S(\mathbb{R}^n)$ is a **dyadic partition of unity** if there is $\varphi \in C_c^\infty(\mathbb{R}^n)$ with $\varphi(\xi)=1$ for $|\xi|\le1$ and $\operatorname{supp}\varphi\subseteq\{|\xi|\le2\}$, such that

$$
\varphi_0=\varphi, \qquad \varphi_j(\xi)=\varphi(2^{-j}\xi)-\varphi(2^{-j+1}\xi) \quad (j \ge1).
$$

Then $\varphi_j \in C_c^\infty$, $\operatorname{supp}\varphi_j \subseteq\{2^{j-1}\le|\xi|\le2^{j+1}\}$ for $j \ge1$, and

$$
\sum_{j=0}^{\infty}\varphi_j(\xi)=1 \quad (\xi \neq0),
$$

the sum being locally finite; the $\varphi_j$ are the **Littlewood–Paley blocks** and, for $f \in\mathcal S'(\mathbb{R}^n)$, the distributions $\varphi_j(D)f$ are defined by the Fourier multiplier $\varphi_j$, with $\widehat{\varphi_j(D)f}=\varphi_j\hat f$.

**Theorem (Bernstein's inequalities).** Let $k \in \mathbb{N}_0$, $1\le p\le r\le\infty$, and let $f \in L^p(\mathbb{R}^n)$ have $\operatorname{supp}\hat f \subseteq\{|\xi|\le R\}$. Then

$$
\|\partial^\alpha f\|_{L^r}\le C\,R^{|\alpha|+n(\frac1p-\frac1r)}\|f\|_{L^p} \quad (|\alpha|=k),
$$

with a constant depending on $k,n$ but not on $R$ or $f$; in particular the frequency localisation allows any derivative to be traded for a power of the frequency and any higher $L^r$ norm to be traded for the $L^p$ norm at the cost of $R^{n(1/p-1/r)}$.

*Proof (sketch).* One writes $f=\phi*f$ for a suitable Schwartz function $\phi$ with $\hat\phi=1$ on the support of $\hat f$, applies the derivative to the convolution kernel and uses Young's inequality, together with the scaling estimate $\|\phi_R\|_{L^r}\le CR^{n(1/p-1/r)}\|\phi_R\|_{L^p}$ for the rescaled kernel $\phi_R$. $\square$

Bernstein's inequalities are the analytic engine of the whole theory: they convert the size of a frequency-localised piece into the size of its derivatives, and they show that the smoothness $s$ must be measured by the factor $2^{js}$ attached to the block at frequency $2^j$.

### The Two Scales

**Definition.** Let $s \in\mathbb{R}$, $0<p\le\infty$ and $0<q\le\infty$, and let $(\varphi_j)$ be a dyadic partition of unity. For $f \in\mathcal S'(\mathbb{R}^n)$ put

$$
\|f\|_{B^s_{p,q}}=\Bigl(\sum_{j=0}^{\infty}\bigl(2^{js}\|\varphi_j(D)f\|_{L^p}\bigr)^q\Bigr)^{1/q},
\qquad
\|f\|_{F^s_{p,q}}=\Bigl\|\Bigl(\sum_{j=0}^{\infty}\bigl(2^{js}|\varphi_j(D)f|\bigr)^q\Bigr)^{1/q}\Bigr\|_{L^p},
$$

with the usual modification $\sup_j$ when $q=\infty$ and, in the $F$-case, the modification $\sup_j2^{js}|\varphi_j(D)f(x)|$ when $p=\infty$. The **Besov space** $B^s_{p,q}$ is the set of $f \in\mathcal S'$ with $\|f\|_{B^s_{p,q}}<\infty$, and the **Triebel–Lizorkin space** $F^s_{p,q}$ is the set of $f \in\mathcal S'$ with $\|f\|_{F^s_{p,q}}<\infty$, both understood modulo polynomials when the seminorm vanishes on them.

**Theorem (independence of the partition).** The spaces $B^s_{p,q}$ and $F^s_{p,q}$ do not depend on the choice of the dyadic partition of unity, and the norms obtained from two different partitions are equivalent.

*Proof (sketch).* If $(\psi_k)$ is another partition, then $\varphi_j(D)f=\sum_k\varphi_j(D)\psi_k(D)f$, and the sum is over the finitely many $k$ with $2^k$ comparable to $2^j$, by the support condition; the kernel of $\varphi_j(D)\psi_k(D)$ is a Schwartz function whose $L^1$ norm is controlled uniformly, so Young's inequality bounds each block of the first partition by the corresponding block of the second, and the two-sided estimate follows by symmetry and by the triangle inequality in the appropriate mixed norm. $\square$

**Proposition (elementary properties).** Let $s \in\mathbb{R}$ and $0<p,q\le\infty$.

(i) $B^s_{p,q}$ and $F^s_{p,q}$ are complete quasi-normed spaces, and they are Banach spaces when $p \ge1$ and $q \ge1$.

(ii) $F^s_{p,p}=B^s_{p,p}$ with equivalent quasi-norms, and for $0<p<\infty$, $0<q\le\infty$,

$$
B^s_{p,\min(p,q)} \hookrightarrow F^s_{p,q}\hookrightarrow B^s_{p,\max(p,q)} ,
$$

so the Besov scale brackets the Triebel–Lizorkin scale and the two coincide at $q=p$.

(iii) For fixed $s,p$ the family is monotone in $q$: $B^s_{p,q_1}\hookrightarrow B^s_{p,q_2}$ and $F^s_{p,q_1}\hookrightarrow F^s_{p,q_2}$ whenever $q_1\le q_2$.

(iv) The spaces are invariant under the lifted Laplacian: $I_\sigma=(1-\Delta)^{-\sigma/2}$, defined by the multiplier $(1+|\xi|^2)^{-\sigma/2}$, is an isomorphism of $B^s_{p,q}$ onto $B^{s-\sigma}_{p,q}$ and of $F^s_{p,q}$ onto $F^{s-\sigma}_{p,q}$ for every $\sigma \in\mathbb{R}$.

(v) The Schwartz class $\mathcal S$ is dense in $B^s_{p,q}$ and in $F^s_{p,q}$ when $p,q<\infty$, the dual of $B^s_{p,q}$ is $B^{-s}_{p',q'}$ for $1\le p,q<\infty$, and the dual of $F^s_{p,q}$ is $F^{-s}_{p',q'}$ for $1<p<\infty$ and $1\le q<\infty$, where $1/p+1/p'=1$ and $1/q+1/q'=1$.

*Proof (sketch).* Completeness is the completeness of the mixed sequence and function spaces, the map $f\mapsto(\varphi_j(D)f)$ being an isometry into a closed subspace for the Besov scale; the continuous inclusions in (ii) and (iii) are consequences of the embeddings of the sequence spaces $\ell^{q_1}\hookrightarrow\ell^{q_2}$, Minkowski's integral inequality and the support condition; the lifting (iv) is the comparison of the multipliers $(1+|\xi|^2)^{-\sigma/2}$ with $2^{-j\sigma}$ on the support of $\varphi_j$; and (v) is the standard duality, obtained from the duality of the underlying sequence spaces and the density of $\mathcal S$. $\square$

## Comparison with the Classical Spaces

### Sobolev, Hölder and Hardy Spaces

**Definition.** For $s \in\mathbb{R}$ and $1<p<\infty$ the **Bessel potential space** $H^s_p$ is the space of $f \in\mathcal S'$ with

$$
\|f\|_{H^s_p}=\bigl\|(1+|\xi|^2)^{s/2}\hat f\,\check{\ }\bigr\|_{L^p}<\infty ,
$$

and for $k \in\mathbb{N}_0$ and $1\le p\le\infty$ the **Sobolev space** $W^{k,p}$ is the space of $f \in L^p$ whose distributional derivatives of order at most $k$ lie in $L^p$, with the norm $\bigl(\sum_{|\alpha|\le k}\|\partial^\alpha f\|_{L^p}^p\bigr)^{1/p}$ for $p<\infty$ and $\max_{|\alpha|\le k}\|\partial^\alpha f\|_{L^\infty}$ for $p=\infty$. For $s>0$ the **Hölder–Zygmund space** $\Lambda^s=C^s$ is the space of $f \in C_b(\mathbb{R}^n)$ with $\|\Delta_h^kf\|_\infty\le C|h|^s$, where $k$ is the least integer exceeding $s$ and $\Delta_hf=f(\cdot+h)-f(\cdot)$.

**Theorem (identifications).** For $1<p<\infty$, $1\le q\le\infty$, $s \in\mathbb{R}$ and $k \in\mathbb{N}_0$:

(i) $F^s_{p,2}=H^s_p$, so the Triebel–Lizorkin scale with $q=2$ is the Sobolev scale with the improved integrability of the potential;
(ii) $F^k_{p,2}=W^{k,p}$ for $k \in\mathbb{N}_0$;
(iii) $B^s_{2,2}=F^s_{2,2}=H^s=H^s_2$, and $B^k_{2,2}=W^{k,2}=H^k$;
(iv) $B^s_{\infty,\infty}=\Lambda^s=C^s$ for $s>0$, and $B^0_{\infty,\infty}=L^\infty$ modulo polynomials;
(v) $F^0_{1,2}=H^1_{\mathrm{Har}}$, the real Hardy space, and $F^0_{\infty,2}=\mathrm{BMO}$;
(vi) $F^0_{p,2}=L^p$ for $1<p<\infty$.

*Proof (sketch).* For (i) one uses the multiplier theorem of *Fourier Analysis on Euclidean Spaces* to compare the norm $\bigl\|(\sum_j|\varphi_j(D)f|^2)^{1/2}\bigr\|_{L^p}$ with $\|(1-\Delta)^{s/2}f\|_{L^p}$, the two multipliers being comparable on the support of each block; (ii) adds Bernstein's inequality to compare the $L^p$ norms of the derivatives; (iii) is the case $p=q=2$ of (i) and the Plancherel theorem; (iv) is the classical characterisation of the Hölder–Zygmund spaces by the decay of the Littlewood–Paley blocks; (v) is the atomic description of the Hardy space and the John–Nirenberg inequality for $\mathrm{BMO}$; and (vi) is the case $s=0$ of (i). These identifications are standard and are cited below. $\square$

**Corollary (the classical scales as one-parameter families).** The Sobolev spaces, the Hölder–Zygmund spaces, the Hardy space and $\mathrm{BMO}$ are all members of the two scales, and the scales therefore carry the classical spaces with their interpolation and their embeddings as special cases; the spaces $W^{k,p}$ and $H^k$ are the cases $q=2$ of the Triebel–Lizorkin family, and the embeddings proved there follow from the general embeddings of the next section.

### Difference and Heat-Kernel Characterisations

**Theorem (difference characterisation of Besov spaces).** Let $s>0$, $0<p,q\le\infty$, and let $k$ be an integer with $k>s$. Then $f \in B^s_{p,q}$ if and only if

$$
\|f\|_{L^p}+\Bigl(\int_0^\infty\bigl(t^{-s}\sup_{|h|\le t}\|\Delta_h^kf\|_{L^p}\bigr)^q\,\frac{dt}{t}\Bigr)^{1/q}<\infty ,
$$

with the $\sup$ modification for $q=\infty$; the quantity is an equivalent quasi-norm. The classical Besov definition by the modulus of continuity is therefore the same scale, and for $p=q=\infty$ the characterisation reduces to the Hölder condition of order $s$.

*Proof (sketch).* The equivalence of the difference and the frequency descriptions is the standard Littlewood–Paley–Stein argument: the difference $\Delta_h^k$ annihilates the frequencies below $|h|^{-1}$, so the integral over $t\approx2^{-j}$ sees exactly the block $\varphi_j(D)f$, and the two sides are comparable by Bernstein's inequality in both directions. $\square$

**Theorem (heat-kernel characterisation).** Let $s>0$ and let $e^{t\Delta}$ be the heat semigroup. Then $f \in B^s_{p,q}$ if and only if

$$
\|f\|_{L^p}+\Bigl(\int_0^\infty\bigl(t^{-s/2}\|(t\Delta)^me^{t\Delta}f\|_{L^p}\bigr)^q\,\frac{dt}{t}\Bigr)^{1/q}<\infty
$$

for any integer $m>s/2$, and the analogous characterisation holds for $F^s_{p,q}$ with the $L^p$ norm taken after the $L^q$ norm in $t$; the characterisations are equivalent quasi-norms.

The heat-kernel description is the form in which the scale is used for the regularity of parabolic equations; it is the semiclassical-frequency version of the Littlewood–Paley definition, with $t$ playing the role of $2^{-2j}$. The proof is the standard one, cited below.

## Embeddings, Traces and Compactness

### Sobolev-Type Embeddings

**Theorem (embeddings).** Let $s,s' \in\mathbb{R}$, $0<p,p',q,q'\le\infty$.

(i) If $s-\frac np=s'-\frac{n}{p'}$ and $p\le p'$, then $B^s_{p,q}\hookrightarrow B^{s'}_{p',q}$ and $F^s_{p,q}\hookrightarrow F^{s'}_{p',q}$; in particular $B^s_{p,q}\hookrightarrow L^{p'}(\mathbb{R}^n)$ for the exponent $p'$ determined by $s-\frac np=-\frac{n}{p'}$ when $p'>p$ and $q\le\min(p',2)$, since then $B^0_{p',q}\hookrightarrow B^0_{p',\min(p',2)}\hookrightarrow F^0_{p',2}=L^{p'}$ by (ii) of the elementary properties, whereas at the critical exponent $q=\infty$ the embedding into $L^{p'}$ fails; and $B^s_{p,q}\hookrightarrow\Lambda^{s-n/p}$ when $s>\frac np$.

(ii) If $s>\frac np$ then $B^s_{p,q}\hookrightarrow L^\infty$ and $F^s_{p,q}\hookrightarrow L^\infty$, and the spaces are algebras under pointwise multiplication for $s>\frac np$.

(iii) On a bounded domain with the cone condition the strict inequality $s-\frac np>s'-\frac{n}{p'}$ gives a compact embedding $B^s_{p,q}(\Omega)\hookrightarrow B^{s'}_{p',q}(\Omega)$ (Rellich–Kondrachov), and the same holds when $s-\frac np=s'-\frac{n}{p'}$ with $p<p'$; the compactness fails on $\mathbb{R}^n$ itself, where the scaling of a fixed function makes the embedding non-compact. In particular, on a bounded domain $B^s_{p,q}\hookrightarrow\hookrightarrow B^{s'}_{p,q}$ for every $s>s'$ and every $q$, the gain $s-s'$ being strictly positive, and $B^s_{p,q}\hookrightarrow\hookrightarrow\Lambda^{s-n/p}$ for $s>\frac np$.

*Proof (sketch).* By Bernstein's inequality each block $\varphi_j(D)f$ satisfies $\|\varphi_j(D)f\|_{L^{p'}}\le C2^{jn(1/p-1/p')}\|\varphi_j(D)f\|_{L^p}$, and the gain $2^{j(s-s')}$ in the embedding is exactly the factor $2^{jn(1/p-1/p')}$ when $s-\frac np=s'-\frac{n}{p'}$; the sum is then dominated by the Besov norm, giving (i), and (ii) is the case $p'=\infty$. For (iii) one splits the sum into the finitely many low frequencies, which are compact by the Arzelà–Ascoli theorem on a bounded domain, and the tail, whose norm is small uniformly on the unit ball, the strict gain in the smoothness making the tail small and the boundedness of the domain making the low frequencies compact. $\square$

**Corollary (comparison with the Sobolev embeddings).** For $1<p<\infty$ the embedding $W^{k,p}\hookrightarrow L^{p'}$ with $\frac1{p'}=\frac1p-\frac kn$, and its compact form when $p'<\infty$, are the case $q=2$ of the theorem, by the identification $W^{k,p}=F^k_{p,2}$; the embedding $W^{k,p}\hookrightarrow\Lambda^{k-n/p}$ into the Hölder–Zygmund class of exponent $k-n/p$ is the corresponding statement, in the Zygmund convention when $k-\frac np$ is an integer. These are the Sobolev and Rellich–Kondrachov theorems, recovered here from the scale.

### Traces and the Boundary

**Theorem (trace).** Let $s>\frac1p$, $0<p,q\le\infty$ in the range for which the trace is classically defined, and let $\gamma f=f(\cdot,0)$ be the trace on the hyperplane $\mathbb{R}^{n-1}\times\{0\}$. Then $\gamma$ extends to a bounded linear map

$$
\gamma:B^s_{p,q}(\mathbb{R}^n)\to B^{s-\frac1p}_{p,q}(\mathbb{R}^{n-1}) \quad \text{and} \quad \gamma:F^s_{p,q}(\mathbb{R}^n)\to F^{s-\frac1p}_{p,q}(\mathbb{R}^{n-1}),
$$

and the maps are surjective, with a bounded right inverse (an extension operator) in each case; the loss $\frac1p$ is sharp.

*Proof (sketch).* The Fourier description in the normal variable turns the trace into the restriction of a frequency-localised function, and the factor $2^{-j/p}$ lost in the normal variable is exactly the exponent shift; the extension is obtained by extending each block separately with a Schwartz cutoff. The sharpness is shown by testing on a function that concentrates at the boundary. $\square$

The theorem is the model of the trace theorems of the scale; it shows that the loss of $\frac1p$ derivatives is exactly the price of restriction to a hyperplane, and it is the analytical basis of the boundary-value problems in the scale, whose theory belongs andboth. The spaces on a domain $\Omega$ are defined by restriction, $B^s_{p,q}(\Omega)=\{f|_\Omega:f \in B^s_{p,q}(\mathbb{R}^n)\}$ with the quotient norm, and the extension and trace theorems identify them with the intrinsic definitions for the smooth domains.

## Atomic and Molecular Decompositions

**Definition.** Let $s \in\mathbb{R}$, $0<p,q\le\infty$ and let $K \in\mathbb{N}_0$ with $K>s$ and $K$ integer. A **$(s,p)$-atom** is a function $a$ supported in a dyadic cube $Q$ of side length $2^{-j}$ such that $|\partial^\alpha a(x)|\le C\,2^{j(n/p+|\alpha|)}$ for $|\alpha|\le K$, and $\int x^\beta a(x)\,dx=0$ for $|\beta|\le K-1$; a **molecule** is a function with the same cancellation and a decay $\prod_{l}(1+2^j|x_l-x_{Q,l}|)^{-M}$ for a large $M$ in place of the support condition.

**Theorem (atomic decomposition).** Let $s \in\mathbb{R}$, $0<p,q\le\infty$, $K>s$, and let $f \in B^s_{p,q}$. Then there exist atoms $a_{j,\nu}$ and coefficients $\lambda_{j,\nu}$ with

$$
f=\sum_{j,\nu}\lambda_{j,\nu}\,a_{j,\nu}, \qquad
\|f\|_{B^s_{p,q}}\approx\Bigl(\sum_{j}\bigl(2^{js}\bigl(\sum_{\nu}|\lambda_{j,\nu}|^p\bigr)^{1/p}\bigr)^q\Bigr)^{1/q},
$$

the sum converging in $\mathcal S'$; and conversely every such sum with the mixed norm finite converges to an element of $B^s_{p,q}$. The same statement holds for $F^s_{p,q}$ with the coefficient norm replaced by

$$
\Bigl\|\Bigl(\sum_{j}\bigl(2^{js}\sum_{\nu}|\lambda_{j,\nu}|\,\mathbf 1_{Q_{j,\nu}}\bigr)^q\Bigr)^{1/q}\Bigr\|_{L^p},
$$

so that the Triebel–Lizorkin norm is the $L^p$ norm of the maximal function of the coefficients and the Besov norm is their mixed norm. The molecular decompositions hold with molecules in place of atoms and the same coefficient norms.

*Proof (sketch).* The atoms are built from the Littlewood–Paley blocks: for a dyadic cube $Q$ of side $2^{-j}$ one takes the product of $\varphi_j(D)f$ with a cutoff adapted to $Q$ and corrects the moments, which is possible because $K>s$; the converse is the estimate of each atom in the scale by Bernstein's inequality and the cancellation (the cancellation is what makes the estimate sharp in $s$). The computations are the standard ones, cited below. $\square$

The atomic decomposition is the bridge from the Fourier description to the real-variable description: it shows that membership in the scale is a condition on a single expansion in localised, oscillating pieces, and it is the form in which the spaces are used in harmonic analysis and in the theory of singular integrals of *Fourier Analysis on Euclidean Spaces*. The wavelet characterisations are the orthonormal version of the same expansion, with $\lambda_{j,\nu}=\langle f,\psi_{j,\nu}\rangle$ for a wavelet basis $\{\psi_{j,\nu}\}$, and the coefficient norm is then exactly the norm of the scale.

## Interpolation and Products

### The Scale as the Interpolation of the Sobolev Spaces

**Theorem (real interpolation).** Let $s_0,s_1 \in\mathbb{R}$ with $s_0 \neq s_1$, $0<p,q,q_0,q_1\le\infty$ and $\theta \in(0,1)$; put $s=(1-\theta)s_0+\theta s_1$. Then

$$
\bigl(B^{s_0}_{p,q_0},B^{s_1}_{p,q_1}\bigr)_{\theta,q}=B^s_{p,q}, \qquad
\bigl(F^{s_0}_{p,q_0},F^{s_1}_{p,q_1}\bigr)_{\theta,q}=B^s_{p,q}
$$

with equivalent quasi-norms, the real method being taken in the sense of *Interpolation Theory*; the real interpolation of the two scales is therefore the Besov scale, whatever the originating family.

*Proof (sketch).* The $K$-functional of the pair is computed blockwise: the frequency blocks of the two spaces are Sobolev-type spaces of a single scale, and the $K$-functional of a piece $\varphi_j(D)f$ is comparable to $\min(2^{js_0},2^{js_1})$-weighted versions of its norm, so the $K$-functional of $f$ is equivalent to a mixed norm in the blocks; the $\theta,q$ norm then produces the Besov norm with exponent $q$, and the equality of the two families follows from the comparison of the scales. The details are the standard ones of the theory. $\square$

**Theorem (complex interpolation and the interpolation of the Sobolev scale).** Let $s_0 \neq s_1$, $0<p,q\le\infty$ and $\theta \in(0,1)$, and put $s=(1-\theta)s_0+\theta s_1$. Then

$$
\bigl[B^{s_0}_{p,q},B^{s_1}_{p,q}\bigr]_\theta=B^s_{p,q}, \qquad
\bigl[F^{s_0}_{p,q},F^{s_1}_{p,q}\bigr]_\theta=F^s_{p,q},
$$

the complex method preserving the family and the fine index; in particular the complex interpolation of the Sobolev spaces $H^{s_0}_p$ and $H^{s_1}_p$ is $H^s_p$, the classical interpolation theorem of the Sobolev scale.

*Proof (sketch).* The complex method is applied blockwise, and the $q$-summation is preserved because the interpolation of the sequence spaces $\ell^q$ with the same $q$ is again $\ell^q$; for the $F$-case one uses the description by the maximal function of the blocks and the interpolation of the mixed norm. $\square$

The two theorems are the reason the scale is the natural one for interpolation: the real method moves among the Besov spaces and closes the Sobolev scale under interpolation, while the complex method preserves the fine index; the classic theorems of *Interpolation Theory* are the special cases $q=2$ of the pair.

### The Paraproduct and Product Estimates

**Definition.** For $f,g \in\mathcal S'$ the **Bony paraproduct** is the decomposition

$$
fg=\sum_{j,k}\varphi_j(D)f\,\varphi_k(D)g
=\underbrace{\sum_{j}\sum_{k\le j-2}\varphi_j(D)f\,\varphi_k(D)g}_{T_fg}
+\underbrace{\sum_{k}\sum_{j\le k-2}\varphi_j(D)f\,\varphi_k(D)g}_{T_gf}
+\underbrace{\sum_{|j-k|\le1}\varphi_j(D)f\,\varphi_k(D)g}_{R(f,g)},
$$

in which $T_fg$ collects the terms in which the frequency of $f$ dominates, $T_gf$ the terms in which that of $g$ dominates, and the remainder $R$ the terms of comparable frequency.

**Theorem (product estimates).** Let $s>0$, $1\le p,p_1,p_2,q\le\infty$ with $\frac1p=\frac1{p_1}+\frac1{p_2}$. Then the pointwise product is bounded:

$$
\|fg\|_{B^s_{p,q}}\le C\|f\|_{B^s_{p_1,q}}\|g\|_{L^{p_2}}+C\|f\|_{L^{p_1}}\|g\|_{B^s_{p_2,q}},
$$

and the same inequality holds for the Triebel–Lizorkin scale with $B$ replaced by $F$ throughout; for $s>\frac np$ the product is bounded in the space itself, which is then an algebra.

*Proof (sketch).* The paraproduct is estimated term by term: in $T_fg$ the frequency of the product is that of $f$, so the derivative of order $s$ is carried by $f$ and $g$ enters only through its $L^{p_2}$ norm; in $R(f,g)$ the frequencies are comparable, so Bernstein's inequality distributes the smoothness; and the mixed norms are estimated by Hölder and Young. $\square$

The paraproduct is the standard tool of the nonlinear theory: the product estimates in the Besov scale are exactly what the fixed-point arguments for quasilinear and nonlinear equations need, and the borderline cases $s=\frac np$ are handled by the refined estimates of the same decomposition. The applications belong .

## Summary

The Besov spaces $B^s_{p,q}$ and the Triebel–Lizorkin spaces $F^s_{p,q}$ are the two three-parameter scales of smoothness obtained from a dyadic partition of unity $(\varphi_j)$ in the frequency variable. The Besov quasi-norm is $\bigl(\sum_j(2^{js}\|\varphi_j(D)f\|_{L^p})^q\bigr)^{1/q}$, the $\ell^q$ norm over the frequency blocks followed by the $L^p$ norm in space, and the Triebel–Lizorkin quasi-norm is $\bigl\|\bigl(\sum_j(2^{js}|\varphi_j(D)f|)^q\bigr)^{1/q}\bigr\|_{L^p}$, the same quantities with the two operations interchanged; they coincide when $p=q$, and in general $B^s_{p,\min(p,q)}\hookrightarrow F^s_{p,q}\hookrightarrow B^s_{p,\max(p,q)}$. The definitions are independent of the partition, the spaces are complete quasi-Banach (Banach for $p,q \ge1$), the lifting $I_\sigma=(1-\Delta)^{-\sigma/2}$ shifts the smoothness index by $\sigma$, and the scale is monotone in $q$. **Bernstein's inequalities** trade derivatives for powers of the frequency, and they are the analytic reason for the factor $2^{js}$.

The classical spaces are members of the scale: $F^s_{p,2}=H^s_p$ is the Bessel potential space, $F^k_{p,2}=W^{k,p}$ is the Sobolev space, $B^s_{\infty,\infty}=C^s$ is the Hölder–Zygmund space, $F^0_{1,2}=H^1$ is the real Hardy space and $F^0_{\infty,2}=\mathrm{BMO}$; the difference and heat-kernel characterisations identify the scale with the classical Besov definition by the modulus of continuity. The **Sobolev-type embeddings** hold with the exponent determined by $s-\frac np$, they are compact under the strict inequality (Rellich–Kondrachov), and for $s>\frac np$ the spaces are algebras; the **trace** on a hyperplane lands in the scale with the loss $\frac1p$, sharply, and the spaces on a domain are defined by restriction with the corresponding extension theorems. The **atomic and molecular decompositions** compute the quasi-norm from the coefficients of an expansion in localised oscillating pieces, and the wavelet characterisations are the orthonormal form of the same statement. **Real interpolation** of the scales gives the Besov scale, $\bigl(B^{s_0}_{p,q_0},B^{s_1}_{p,q_1}\bigr)_{\theta,q}=B^s_{p,q}$, and **complex interpolation** preserves the family and the fine index, so the Sobolev scale is closed under interpolation; the **Bony paraproduct** decomposes a product into the terms dominated by either factor and the comparable-frequency remainder, and the resulting product estimates make the spaces with $s>\frac np$ algebras and supply the nonlinear estimates of the theory of partial differential equations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $s$ | smoothness index, $s \in\mathbb{R}$ |
| $p,q$ | integrability and fine indices, $0<p,q\le\infty$ |
| $\varphi_j$, $(\varphi_j)$ | Littlewood–Paley blocks, dyadic partition of unity |
| $\varphi_j(D)$ | Fourier multiplier by $\varphi_j$ |
| $B^s_{p,q}$ | Besov space |
| $F^s_{p,q}$ | Triebel–Lizorkin space |
| $\|f\|_{B^s_{p,q}}$, $\|f\|_{F^s_{p,q}}$ | the corresponding quasi-norms |
| $H^s_p$ | Bessel potential (Sobolev) space |
| $W^{k,p}$, $H^k$ | Sobolev spaces |
| $\Lambda^s=C^s$ | Hölder–Zygmund space |
| $H^1$, $\mathrm{BMO}$ | real Hardy space, bounded mean oscillation |
| $\Delta_h$ | difference operator, $\Delta_hf=f(\cdot+h)-f(\cdot)$ |
| $e^{t\Delta}$ | heat semigroup |
| $I_\sigma$ | lifting, $(1-\Delta)^{-\sigma/2}$ |
| $(\cdot,\cdot)_{\theta,q}$ | real interpolation functor |
| $[\,\cdot,\cdot\,]_\theta$ | complex interpolation functor |
| $T_fg$, $R(f,g)$ | Bony paraproduct terms |
| $a_{j,\nu}$, $\lambda_{j,\nu}$ | atoms and coefficients |
| $\psi_{j,\nu}$ | wavelet basis |



## Further Reading

- Sergei M. Nikolskii, *Approximation of Functions of Several Variables and Imbedding Theorems* (Springer, 1975), for the difference definition of the Besov spaces and the embedding theory.
- Oleg V. Besov, "Investigation of a class of function spaces in connection with the embedding and extension theorems", *Trudy Matematicheskogo Instituta imeni V. A. Steklova* 60 (1961), 42–81, and "On some families of functional spaces: imbedding and extension theorems", *Doklady Akademii Nauk SSSR* 126 (1959), 1163–1165, for the original Besov scale.
- Alberto P. Calderón, "Intermediate spaces and interpolation, the complex method", *Studia Mathematica* 24 (1964), 113–190, for the complex interpolation and the interpolation of the scale.
- Jacques-Louis Lions and Jaak Peetre, "Sur une classe d'espaces d'interpolation", *Publications Mathématiques de l'IHÉS* 19 (1964), 5–68, for the real method and the identification of the interpolation spaces of the Sobolev scale.
- Hans Triebel, *Theory of Function Spaces* (Birkhäuser, 1983), for the systematic theory of the Besov and Triebel–Lizorkin spaces.
- Hans Triebel, *Interpolation Theory, Function Spaces, Differential Operators* (North-Holland, 1978), for the interpolation of the scale and its applications to differential operators.
- Jaak Peetre, *New Thoughts on Besov Spaces* (Duke University Press, 1976), for the difference and oscillation characterisations.
- Jean-Michel Bony, "Calcul symbolique et propagation des singularités pour les équations aux dérivées partielles non linéaires", *Annales Scientifiques de l'École Normale Supérieure* 14 (1981), 209–246, for the paraproduct and the nonlinear product estimates.
- Ronald R. Coifman and Yves Meyer, *Au-delà des opérateurs pseudo-différentiels* (Astérisque 57, 1978), for the atomic and molecular decompositions and the wavelet characterisations.
