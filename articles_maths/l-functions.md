
# __L-Functions__

## Introduction

A Dirichlet $L$-function is a zeta function with a twist: for a character $\chi$ of the group $(\mathbb{Z}/q\mathbb{Z})^\times$ one forms
$$
L(s,\chi) = \sum_{n\geq1}\frac{\chi(n)}{n^s} = \prod_p \frac{1}{1 - \chi(p)p^{-s}},
$$
a Dirichlet series whose coefficients are the values of the character, with an Euler product over the primes and with an analytic continuation and a functional equation that involve the character through a Gauss sum. The twist is not a cosmetic change: summing $L(s,\chi)$ and $\zeta(s)$ over the characters of $(\mathbb{Z}/q\mathbb{Z})^\times$ isolates the primes in a given arithmetic progression, and the fact that $L(1,\chi)\neq0$ for a nontrivial character is exactly Dirichlet's theorem that every arithmetic progression of coprime integers contains infinitely many primes. This article develops the theory of these functions, and then the general notion of an $L$-function that they exemplify: a Dirichlet series with an Euler product, a functional equation with an explicit Gamma factor and conductor, and a boundedness hypothesis, together with the families attached to Hecke characters, to Galois representations and to automorphic forms.

The analytic machinery is Tate's thesis, the local and global zeta integrals of *Adelic Analysis*, written immediately above: a Hecke character gives a zeta integral, its Euler product the local factors, and the global functional equation gives the functional equation of the associated $L$-function. That article proves the general functional equation; this one states the arithmetic cases, extracts the Dirichlet $L$-functions as the abelian case over $\mathbb{Q}$, and organises the general theory. The counting of primes with the help of the nonvanishing statements is not covered here; the analytic proof of the prime number theorem for the progression $a \bmod q$ and the zero-free regions are; the generalised Riemann hypothesis is stated and discussed; the automorphic $L$-functions and the reciprocity between Galois representations and automorphic forms are the subject of *Automorphic Forms*, in the other category of this Part, and the classical modular case. The $L$-function of an elliptic curve over $\mathbb{Q}$, its modularity and its arithmetic belong to *Elliptic Curves* and to the arithmetic geometry of Part I.

The prerequisites are *Adelic Analysis* for the adelic integrals, the Hecke characters and the functional equations, *Zeta Functions* for the Riemann and Dedekind zeta functions, which are the trivial-character and trivial-representation cases, *Galois Theory* and *Galois Theory of $\mathbb{C}/\mathbb{R}$* for the Galois groups, *Representation Theory* for the characters and the irreducible representations of a finite group, *Algebraic Number Theory* for the arithmetic of $(\mathbb{Z}/q\mathbb{Z})^\times$, the class number formula and the quadratic fields, andfor the Gamma function and the analytic continuation. Throughout, $q \geq 1$ is a modulus, $\chi$ a Dirichlet character modulo $q$, $\chi_0$ the principal character, $\tau(\chi)$ the Gauss sum, and $L(s,\chi)$ the associated Dirichlet $L$-function; the completed $L$-function is written $\Lambda(s,\chi)$, the Euler factors $L_p$, and the general $L$-function attached to a representation $\rho$ is written $L(s,\rho)$. The conventions for the Bernoulli numbers and the Gamma factors are those of *Zeta Functions*.

## Dirichlet Characters

### Definitions

**Definition.** A **Dirichlet character** modulo $q$ is a group homomorphism $\chi : (\mathbb{Z}/q\mathbb{Z})^\times \to \mathbb{C}^\times$, extended to a function on $\mathbb{Z}$ by $\chi(n) = \chi(n \bmod q)$ for $(n,q)=1$ and $\chi(n)=0$ for $(n,q)>1$. The **principal character** $\chi_0$ is the character that is $1$ on all units. The **conductor** of $\chi$ is the smallest positive divisor $f \mid q$ such that $\chi$ is induced from a character modulo $f$, and $\chi$ is **primitive** if its conductor is $q$. A character is **even** if $\chi(-1)=1$ and **odd** if $\chi(-1)=-1$.

**Proposition.** The set $\widehat{G}$ of characters of the finite abelian group $G = (\mathbb{Z}/q\mathbb{Z})^\times$ is a group under pointwise multiplication, isomorphic to $G$; the characters satisfy the orthogonality relations
$$
\sum_{\chi \in \widehat G} \chi(a) = \begin{cases} \varphi(q) & a\equiv1 \pmod q,\\ 0 & \text{otherwise},\end{cases}
\qquad
\sum_{a \in G}\chi(a) = \begin{cases} \varphi(q) & \chi = \chi_0,\\ 0 & \text{otherwise},\end{cases}
$$
and the characters of $(\mathbb{Z}/q\mathbb{Z})^\times$ are exactly the characters of $\mathbb{Z}/q\mathbb{Z}$ whose value at a nonunit is $0$.

**Proof.** The group $(\mathbb{Z}/q\mathbb{Z})^\times$ is finite abelian, hence a direct product of cyclic groups; over $\mathbb{C}$ a cyclic group of order $n$ has exactly $n$ characters, given by $g\mapsto\zeta_n^k$ for the $n$-th roots of unity, and the orthogonality relations are the standard orthogonality of the columns and rows of the character table. $\square$

### Gauss Sums

**Definition.** For a character $\chi$ modulo $q$ the **Gauss sum** is
$$
\tau(\chi) = \sum_{a=1}^{q}\chi(a)\,e^{2\pi i a/q}.
$$
**Theorem (properties of the Gauss sum).** Let $\chi$ be primitive modulo $q$. Then

**(a)** $\lvert\tau(\chi)\rvert = \sqrt q$;

**(b)** $\tau(\chi)\tau(\bar\chi) = \chi(-1)\,q$;

**(c)** $\overline{\tau(\chi)} = \chi(-1)\,\tau(\bar\chi)$, and consequently $\tau(\chi) = \chi(-1)\,\overline{\tau(\bar\chi)}$.

**Proof sketch.** For (a), compute $\lvert\tau(\chi)\rvert^2 = \sum_{a,b}\chi(a)\bar\chi(b)e^{2\pi i(a-b)/q}$ and substitute $a = bu$ for $u$ ranging over the units, using the primitivity to replace the sum over units by a sum over all residues in the resulting Ramanujan sum; the result is $\sum_{u}\chi(u)\sum_{c}e^{2\pi i uc/q} = q$. The identity (b) follows from (a) and the computation of $\tau(\chi)^2$ for the primitive case, and (c) is the substitution $a\mapsto a^{-1}$ in the defining sum. $\square$

**Example.** For the nontrivial character modulo $3$, with $\chi(1)=1$ and $\chi(2)=-1$, the Gauss sum is $\tau = e^{2\pi i/3} - e^{4\pi i/3} = i\sqrt3$, of absolute value $\sqrt3 = \sqrt q$; the associated root number of the next section is $\tau/(i\sqrt3) = 1$. For the character modulo $4$ with $\chi(-1)=-1$, the Gauss sum is $\tau = e^{2\pi i/4} - e^{6\pi i/4} = 2i$, of absolute value $2 = \sqrt4$.

## Dirichlet $L$-Functions

### Definition and Euler Product

**Definition.** For a character $\chi$ modulo $q$, the **Dirichlet $L$-function** is
$$
L(s,\chi) = \sum_{n\geq1}\frac{\chi(n)}{n^s} = \prod_{p}\frac{1}{1-\chi(p)p^{-s}} \qquad (\Re s > 1).
$$
**Theorem (elementary properties).** The series and the product converge absolutely and locally uniformly for $\Re s>1$, the product is the Euler product of the series, and if $\chi\neq\chi_0$ then the series converges conditionally, and the function is continuous, on the half-plane $\Re s>0$; if $\chi = \chi_0$, then $L(s,\chi_0) = \zeta(s)\prod_{p\mid q}(1-p^{-s})$ has the simple pole of $\zeta$ at $s=1$ and no other pole.

**Proof.** Absolute convergence for $\sigma>1$ is the Euler product theorem. For a nonprincipal character the partial sums of the coefficients are bounded by $\varphi(q)$ because the character sums over complete residue systems vanish; summation by parts then gives the convergence for $\sigma>0$. The principal character factors out the finitely many primes dividing $q$. $\square$

### Analytic Continuation and the Functional Equation

**Definition.** Let $\chi$ be primitive modulo $q$ and let $a = 0$ if $\chi$ is even and $a = 1$ if $\chi$ is odd. The **completed $L$-function** is
$$
\Lambda(s,\chi) = \Bigl(\frac{q}{\pi}\Bigr)^{(s+a)/2}\Gamma\Bigl(\frac{s+a}{2}\Bigr)L(s,\chi),
$$
and the **root number** is $\epsilon_\chi = \dfrac{\tau(\chi)}{i^{a}\sqrt q}$.

**Theorem (functional equation of the Dirichlet $L$-function).** Let $\chi$ be primitive modulo $q$. Then $L(s,\chi)$ has an analytic continuation to an entire function of $s$, and
$$
\Lambda(s,\chi) = \epsilon_\chi\,\Lambda(1-s,\bar\chi), \qquad \lvert\epsilon_\chi\rvert = 1 .
$$
For a nonprimitive character the same statements hold after removing the finitely many Euler factors of the inducing modulus, and for the principal character the completed function has poles at $s=0$ and $s=1$ corresponding to the pole of $\zeta$.

**Proof sketch (theta and Gauss sums).** One forms the twisted theta series $\theta_\chi(t) = \sum_{n\geq1}\chi(n)e^{-\pi n^2t/q}$, with the variant $\sum_n n\,\chi(n)e^{-\pi n^2t/q}$ when $\chi$ is odd; Poisson summation applied to the twisted Gauss sum produces the transformation law of $\theta_\chi$ under $t\mapsto1/t$, and the constant in that law is precisely the root number $\epsilon_\chi = \tau(\chi)/(i^a\sqrt q)$; the Mellin transform of the appropriate power of $t$ times $\theta_\chi$ is then the completed $L$-function $\Lambda(s,\chi)$, and the functional equation follows from the transformation law. The adelic proof is the one of *Adelic Analysis*: the character $\chi$ determines a Hecke character of the idele class group of $\mathbb{Q}$, and the completed $L$-function is the global zeta integral of that character, so the functional equation is Poisson summation. $\square$

**Corollary (the zeros of a Dirichlet $L$-function).** A Dirichlet $L$-function with $\chi\neq\chi_0$ has no zero in $\Re s>1$, by the Euler product, and no zero at $s=1$, by the nonvanishing theorem below; its trivial zeros are the poles of the Gamma factor of its completed function, at $s=-1,-3,-5,\dots$ when $\chi$ is odd and at $s=0,-2,-4,\dots$ when $\chi$ is even, the point $s=0$ being a zero for every even character except the principal character modulo $1$, for which $L(0,\chi_0) = \zeta(0) = -\tfrac12$; hence all its nontrivial zeros lie in the critical strip $0\le\Re s\le1$. The analogue of the Riemann hypothesis asserts that they all satisfy $\Re s = \tfrac12$, and the generalised Riemann hypothesis is the statement for all the Dirichlet $L$-functions at once, treated.

**Theorem (nonvanishing at $s=1$ and Dirichlet's theorem).** For every character $\chi\neq\chi_0$ modulo $q$, $L(1,\chi)\neq0$. Consequently, for every $a$ with $(a,q)=1$ the sum $\sum_{p}\frac{1}{p^s}$ over the primes $p\equiv a \pmod q$ behaves like $\frac{1}{\varphi(q)}\log\frac{1}{s-1}$ as $s\to1^+$, and there are infinitely many such primes.

**Proof sketch.** For a real character $\chi$ the product $\zeta(s)L(s,\chi)$ has nonnegative Dirichlet coefficients, since $\sum_{d\mid n}\chi(d) = \prod_{p^a\|n}(1+\chi(p)+\cdots+\chi(p)^a)\geq0$ for every $n$; its Euler product has a logarithm with nonnegative coefficients, and at every square $m^2$ coprime to $q$ the coefficient satisfies $\sum_{d\mid m^2}\chi(d)\geq1$, so the coefficients are not all zero and the abscissa of convergence of the series is finite. If $L(1,\chi)$ vanished with a simple zero, the pole of $\zeta$ would cancel and $\zeta(s)L(s,\chi)$, being a Dirichlet series with nonnegative coefficients and a finite abscissa of convergence, would be entire — which Landau's theorem of *Zeta Functions* forbids, since such a series is singular at its abscissa. Alternatively, and cleanly for a primitive real character, the class number formula of *Algebraic Number Theory* exhibits the value directly, $L(1,\chi_d) = 2\pi h/(w\sqrt{\lvert d\rvert})>0$ for the quadratic field of discriminant $d$ associated with $\chi$, which settles the primitive case and with it the nonprimitive one, whose Euler factors at the primes dividing $q$ are finite and nonzero at $s=1$. For a non-real character one applies the same argument to
$$
F(s) = \zeta(s)^2L(s,\chi)L(s,\bar\chi),
$$
whose Euler product has the logarithm
$$
\sum_{p}\sum_{k\geq1}\frac{1}{k}\bigl(2+\chi(p)^k+\bar\chi(p)^k\bigr)p^{-ks}, \qquad 2+\chi(p)^k+\bar\chi(p)^k = 2+2\operatorname{Re}\chi(p)^k \geq 0,
$$
so that the Dirichlet coefficients of $F$ are nonnegative and $F$ is not identically zero; moreover $F(s)\geq1$ for real $s>1$, since its logarithm has nonnegative coefficients. If $L(1,\chi)$ vanished then $L(1,\bar\chi)$ would vanish as well, since the two are conjugate; a zero of order $k$ of $L(s,\chi)$ at $s=1$ together with a zero of order $m$ of $L(s,\bar\chi)$ would leave a zero of order $k+m-2$ in $F$ at $s=1$, which the inequality $F(s)\geq1$ forbids unless $k+m = 2$, so the vanishing would be simple and $F$ would be holomorphic and nonzero at $s=1$; but the coefficient of $p^{-s}$ in the logarithm of $F$ is $2+2\operatorname{Re}\chi(p)$, whose sum over the primes diverges, because $\sum_p2/p$ diverges while $\sum_p(\chi(p)+\bar\chi(p))/p$ converges for a nonprincipal character by partial summation against bounded character sums; hence the Dirichlet series of $\log F$ has abscissa of convergence $1$ and is singular there by Landau's theorem, in contradiction with the regularity of $F$ at $s=1$. The stated asymptotic follows by writing the indicator of the progression $a \bmod q$ as an average of characters with the orthogonality relations. $\square$

### Special Values

**Definition.** The **generalised Bernoulli numbers** of a primitive character $\chi$ modulo $q$ are defined by
$$
\sum_{a=1}^{q}\chi(a)\frac{t\,e^{at}}{e^{qt}-1} = \sum_{n\geq0}B_{n,\chi}\frac{t^n}{n!}.
$$
**Theorem (values at nonpositive integers).** For a primitive character $\chi$ modulo $q$ and every $n\geq1$,
$$
L(1-n,\chi) = -\frac{B_{n,\chi}}{n}, \qquad\text{in particular}\qquad L(0,\chi) = -\frac{1}{q}\sum_{a=1}^{q}a\,\chi(a) .
$$
**Proof sketch.** The generalised Bernoulli numbers generate the values by the same Mellin-transform argument as for the trivial character, with the twisted theta series replacing the theta function; the second formula is the case $n=1$ and is computed directly from the definition. $\square$

**Theorem (values at $1$ and the class number formula).** For the primitive quadratic character $\chi_d$ of a quadratic field $K = \mathbb{Q}(\sqrt d)$ of discriminant $d$,
$$
L(1,\chi_d) = \begin{cases} \dfrac{2\pi h}{w\sqrt{\lvert d\rvert}} & d<0,\\[2mm] \dfrac{2h\log\varepsilon}{\sqrt d} & d>0,\end{cases}
$$
where $h$ is the class number, $w$ the number of roots of unity and $\varepsilon>1$ the fundamental unit. The formula is the class number formula of *Zeta Functions* for a quadratic field, written in terms of the character, and it shows that $L(1,\chi_d)$ is a computable positive number, the positivity being itself a nontrivial statement.

## The General Theory of $L$-Functions

### The Axioms and the Completed Function

**Definition.** An **$L$-function** in the analytic sense is a function of the form $L(s) = \sum_{n\ge1}a_nn^{-s}$ with $a_1=1$ satisfying: the **Ramanujan bound** $a_n \ll n^{\epsilon}$ together with the absolute convergence of the series and its Euler product for $\Re s>1$; an **Euler product** of **degree** $d$, $L(s) = \prod_p \prod_{j=1}^d(1-\alpha_{j,p}p^{-s})^{-1}$ with $\lvert \alpha_{j,p}\rvert \leq 1$; and a **functional equation** of the form
$$
\Lambda(s) = \epsilon\, \overline{\Lambda(1-\bar s)},\qquad \Lambda(s) = Q^{s/2}\prod_{j=1}^{d}\Gamma\Bigl(\frac{s+\kappa_j}{2}\Bigr)L(s),
$$
with $Q>0$ the **conductor**, $\kappa_j$ the **spectral parameters** and $\lvert\epsilon\rvert=1$ the root number. The **Selberg class** is the subclass of these functions whose Dirichlet coefficients and Euler factors satisfy the additional analytic axioms of Selberg; it contains the Riemann zeta function, the Dirichlet $L$-functions, the Dedekind zeta functions and the Hecke $L$-functions, and it is conjectured that it contains all the $L$-functions of arithmetic origin.

**Proposition (uniqueness of the data).** The conductor, the degree, the spectral parameters and the root number are determined by the function; the product of two $L$-functions of degrees $d_1,d_2$ is an $L$-function of degree $d_1+d_2$; and $L(s)$ has no zero in $\Re s>1$, by the Euler product and the Ramanujan bound.

**Proof.** The Euler product determines the local factors $p^{-s}\mapsto L_p$ and hence the degree; the functional equation then determines the Gamma factors up to the classification of the products of Gamma functions; multiplicativity of the degree is the multiplicativity of the local factors. Nonvanishing for $\Re s>1$ is the convergence of the logarithm of the Euler product. $\square$

### Hecke $L$-Functions

**Definition.** Let $K$ be a number field and $\chi$ a Hecke character of $\mathbb{A}_K^\times$ trivial on $K^\times$, with local components $\chi_v$. The **Hecke $L$-function** is
$$
L(s,\chi) = \prod_v L_v(s,\chi_v), \qquad L_v(s,\chi_v) = \frac{1}{1-\chi_v(\varpi_v)q_v^{-s}} \text{ for } v \text{ unramified},
$$
with the Archimedean factors given by Gamma functions according to the infinity type of $\chi$.

**Theorem (Hecke; Tate).** For every Hecke character $\chi$ the product converges for $\Re s > 1$, extends meromorphically to $\mathbb{C}$ with a functional equation $\Lambda(s,\chi) = \epsilon(s,\chi)\Lambda(1-s,\chi^{-1})$, and is entire when $\chi$ is not a power of the norm character; for $\chi$ trivial it is the Dedekind zeta function of $K$.

**Proof.** This is the main theorem of *Adelic Analysis*: the $L$-function is the normalised global zeta integral of $\chi$ against a factorisable Schwartz–Bruhat function, the Euler product is the product of the local integrals, and the functional equation is Poisson summation together with the local functional equations. The claims about the poles are read off from the local factors of the norm character. $\square$

### Artin $L$-Functions

**Definition.** Let $L/K$ be a finite Galois extension of number fields with group $G$, and let $\rho : G \to GL_n(\mathbb{C})$ be a representation. For a prime $v$ of $K$ unramified in $L$ with Frobenius conjugacy class $\mathrm{Frob}_v \subseteq G$, the **local factor** is $\det(1-\rho(\mathrm{Frob}_v)N(v)^{-s})^{-1}$, and the **Artin $L$-function** $L(s,\rho,L/K)$ is the product of these factors with the ramified and Archimedean factors inserted according to the standard rules.

**Theorem (factorisation of the Dedekind zeta function).** With $L/K$ and $G$ as above, summing over the irreducible complex representations $\rho$ of $G$,
$$
\zeta_L(s) = \prod_{\rho} L(s,\rho,L/K)^{\dim\rho},
$$
so the Dedekind zeta function of the extension is the product of the Artin $L$-functions of the irreducible representations of the group.

**Proof sketch.** The identity is the decomposition of the regular representation. Artin $L$-functions are multiplicative in induction: for a subgroup $H \subseteq G$ and a representation $\sigma$ of $H$ one has $L(s,\mathrm{Ind}_H^G\sigma,L/K) = L(s,\sigma,L/L^H)$, and taking $H = 1$ gives $L(s,\mathrm{Reg}_G,L/K) = L(s,1,L/L) = \zeta_L(s)$; on the other side $\mathrm{Reg}_G = \bigoplus_\rho\rho^{\oplus\dim\rho}$ for the irreducible complex representations of the finite group $G$, and Euler factors multiply, so $\zeta_L(s) = \prod_\rho L(s,\rho,L/K)^{\dim\rho}$. At a prime $v$ of $K$ unramified in $L$ both sides are $\det(1-\mathrm{Frob}_vN(v)^{-s}\mid\mathbb{C}[G])^{-1} = \prod_{\mathfrak{P}\mid v}(1-N(v)^{-f_{\mathfrak{P}}s})^{-1}$, the eigenvalues of the Frobenius on the regular representation being the values $\chi(\mathrm{Frob}_v)$ with the multiplicities $\dim\rho$. The ramified and Archimedean places are handled by the definitions of the local factors. $\square$

**Conjecture (Artin).** If $\rho$ is irreducible and nontrivial then $L(s,\rho,L/K)$ is entire. The conjecture is known for one-dimensional $\rho$, where the Artin $L$-function is a Hecke $L$-function by class field theory, and in the case of the two-dimensional representations of certain groups, where the modularity theorems give it; the general case is open and is one of the guiding problems of the theory. The comparison of the Artin and automorphic descriptions of an $L$-function is the reciprocity conjectures, whose analytic side is the subject of *Automorphic Forms* and whose classical modular case is not covered here.

## Summary

A Dirichlet character modulo $q$ is a character of the finite abelian group $(\mathbb{Z}/q\mathbb{Z})^\times$, extended by $0$ off the units; the characters satisfy the orthogonality relations, and the Gauss sum $\tau(\chi) = \sum_a\chi(a)e^{2\pi ia/q}$ of a primitive character has absolute value $\sqrt q$ and satisfies $\tau(\chi)\tau(\bar\chi) = \chi(-1)q$. The Dirichlet $L$-function $L(s,\chi) = \sum_n\chi(n)n^{-s}$ has an Euler product over the primes, converges absolutely for $\Re s>1$, converges conditionally for $\Re s>0$ when $\chi$ is nonprincipal, and is entire in that case; its completion $\Lambda(s,\chi) = (q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi)$, with $a = 0$ or $1$ according to the parity of $\chi$, satisfies the functional equation $\Lambda(s,\chi) = \epsilon_\chi\Lambda(1-s,\bar\chi)$ with the root number $\epsilon_\chi = \tau(\chi)/(i^a\sqrt q)$ of absolute value $1$. The values at the nonpositive integers are the generalised Bernoulli numbers, $L(1-n,\chi) = -B_{n,\chi}/n$, and the value at $1$ for a quadratic character is the class number formula.

The nonvanishing $L(1,\chi)\neq0$ for nonprincipal $\chi$ is the analytic input of Dirichlet's theorem on primes in arithmetic progressions, and it is proved by a positivity argument on the product of zeta and $L$-functions. The general theory organises the examples — Dirichlet, Dedekind, Hecke and Artin $L$-functions and their automorphic analogues — by the data of an Euler product of a given degree, a functional equation with a conductor, spectral parameters and a root number, and by the Ramanujan bound; the Dedekind zeta function of a Galois extension factors as the product of the Artin $L$-functions of the irreducible representations of its group, the Hecke $L$-functions are the zeta integrals of the Hecke characters of the adeles and their functional equations are Tate's, and the Artin conjecture that the nontrivial Artin $L$-functions are entire is open beyond the low-dimensional and solvable cases.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $q$ | Modulus of a Dirichlet character |
| $\chi$, $\chi_0$ | Dirichlet character modulo $q$, principal character |
| $\varphi(q)$ | Euler's totient, order of $(\mathbb{Z}/q\mathbb{Z})^\times$ |
| $f$, conductor | Least modulus from which $\chi$ is induced; $\chi$ primitive if $f=q$ |
| even, odd | $\chi(-1)=1$, $\chi(-1)=-1$ |
| $\tau(\chi)$ | Gauss sum $\sum_{a=1}^q\chi(a)e^{2\pi ia/q}$ |
| $L(s,\chi)$ | Dirichlet $L$-function, its Euler product over $p$ |
| $a$ | $0$ for even $\chi$, $1$ for odd $\chi$ |
| $\Lambda(s,\chi)$ | Completed $L$-function, $(q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi)$ |
| $\epsilon_\chi = \tau(\chi)/(i^a\sqrt q)$ | Root number, $\lvert\epsilon_\chi\rvert=1$ |
| $B_{n,\chi}$ | Generalised Bernoulli numbers, $L(1-n,\chi) = -B_{n,\chi}/n$ |
| $\chi_d$, $d$ | Quadratic character, fundamental discriminant |
| $h$, $w$, $\varepsilon$ | Class number, roots of unity, fundamental unit |
| $L(s,\rho,L/K)$ | Artin $L$-function of a representation $\rho$ of the Galois group |
| $d$, $Q$, $\kappa_j$, $\epsilon$ | Degree, conductor, spectral parameters, root number of a general $L$-function |
| $\mathrm{Frob}_v$ | Frobenius conjugacy class at an unramified prime |
| $\zeta_L = \prod_\rho L(s,\rho,L/K)^{\dim\rho}$ | Factorisation of the Dedekind zeta function |







## Further Reading

- Harold Davenport, *Multiplicative Number Theory* (3rd ed., Springer, 2000), for the Dirichlet $L$-functions, the functional equation and Dirichlet's theorem.
- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the modern treatment of the $L$-functions, their conductors and their analytic properties.
- Erich Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen* (Mathematische Zeitschrift 1, 1918, and 6, 1920), for the Hecke $L$-functions and their functional equations.
- Emil Artin, *Zur Theorie der $L$-Reihen mit allgemeinen Gruppencharakteren* (Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 8, 1931), for the Artin $L$-functions and the factorisation of the Dedekind zeta function.
- John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (doctoral thesis, Princeton, 1950), for the adelic proof of the functional equation of a Hecke $L$-function.
- Atle Selberg, *Old and new conjectures and results about a class of Dirichlet series* (Proceedings of the Amalfi Conference on Analytic Number Theory, 1992), for the axioms of the Selberg class.
- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory* (2nd ed., Springer, 1990), for the characters, the Gauss sums and the class number formula.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for the Artin $L$-functions and the reciprocity laws of class field theory.
