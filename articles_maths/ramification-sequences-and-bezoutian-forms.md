# __Ramification Sequences and Bezoutian Forms__

## Introduction

Let $F$ be a field of characteristic different from $2$. Over the rational function field $F(t)$ the second Milnor $K$-group is described by local data: at each place of $F(t)$ there is a tame symbol, the tame symbols assemble into the ramification map, and Milnor's exact sequence identifies the image of that map with the group of those sequences in a direct sum of square-class groups whose norms cancel. The image is the group $R_2(F)$ of **ramification sequences** of $F$, and the exact sequence leaves open which of its elements are the ramification of a single symbol $\{f,g\}$ of $k_2(F(t))$.

The obstruction to representability is a quadratic form over the base field. To a pair $(f,g)$ of polynomials Becher and Raczek attach the **Bezoutian form** $B(f/g)$, a non-degenerate quadratic form on $F[t]/(g)$ whose class in the Witt group $W(F)$ is computed from the pair by two simple rules, and they relate its triviality to the representability of the sequence of the pair by a symbol. The criterion turns representability into a question about the Witt group, and the worked example of this article answers that question negatively over $\mathbb{Q}$: the sequence has degree $4$, its Bezoutian is a scalar multiple of the Pfister form $\langle\!\langle 2,3\rangle\!\rangle$, that form is anisotropic because $(2,3)_{\mathbb{Q}}$ is a division algebra, and the sequence is therefore not represented by a symbol.

The base is a field $F$ of characteristic not $2$ throughout, and $F(t)$ is its rational function field. The Milnor groups, the symbols and the tame symbol are from *Higher Algebraic K-Theory*; the polynomial algebra and the resultant are from *Polynomial Rings and Rational Functions*; the quadratic forms, their discriminant and their Witt group are from *Quadratic Forms and Polarisation* and *The Witt Group and the Grothendieck–Witt Ring*, whose Pfister forms $\langle\!\langle a,b\rangle\!\rangle$ are used; the classification of forms over $\mathbb{Q}$ behind the Hasse–Minkowski principle is in *Witt's Theorems*; the quaternion algebras and the division criterion are from *Central Simple Algebras and the Brauer Group* and *Division Algebras*.

## The Places of $F(t)$

A **place** of $F(t)$ is a $\mathbb{Z}$-valued valuation that is trivial on $F$, that is, a surjective map $v : F(t)^\times \to \mathbb{Z}$ with $v(xy) = v(x) + v(y)$ and $v(x + y) \geq \min\{v(x), v(y)\}$, whose restriction to $F^\times$ is zero. There are two kinds of places. Each monic irreducible polynomial $p \in F[t]$ determines the valuation $v_p$ with $v_p(p) = 1$, whose residue field is

$$
\kappa_p = F_p = F[t]/(p), \qquad [F_p : F] = \deg p ;
$$

and there is the place at infinity, determined by $v_\infty(h) = -\deg h$, whose residue field is $F_\infty = F$. We write $P$ for the set of monic irreducible polynomials and

$$
P' = P \cup \{\infty\}
$$

for the set of all places. The **degree** of a place is $[\kappa_p : F]$, so a finite place has degree $\deg p$ and the place at infinity has degree $1$.

## The Tame Symbol and Milnor's Exact Sequence

### The Tame Symbol

Recall from *Higher Algebraic K-Theory* that a discrete valuation $v$ of a field, with residue field $\kappa_v$ and uniformiser $\pi$, determines the **tame symbol**

$$
\partial_v : k_2 \longrightarrow k_1(\kappa_v), \qquad \partial_v(\{f,g\}) = (-1)^{v(f)v(g)} u_f^{-v(g)} u_g^{v(f)},
$$

where $f = u_f\pi^{v(f)}$ and $g = u_g\pi^{v(g)}$ are the decompositions into a power of the uniformiser and a unit, and $k_1(\kappa) = \kappa^\times/\kappa^{\times 2}$. That article proves that $\partial_v$ annihilates the defining relations of the symbols, so that it descends to a homomorphism on $k_2$.

At a finite place $p$ of $F(t)$ the uniformiser is $p$ and the decomposition is $f = p^{v_p(f)}u_f$ with $u_f = f/p^{v_p(f)}$, so the entry of a symbol is the class of

$$
(-1)^{v_p(f)v_p(g)}\left(\frac{f}{p^{v_p(f)}}\right)^{-v_p(g)}\left(\frac{g}{p^{v_p(g)}}\right)^{v_p(f)} \quad \text{in } F_p^\times/F_p^{\times 2}.
$$

At the place at infinity the uniformiser is $1/t$, and the entry of a symbol lies in $F^\times/F^{\times 2}$.

### Milnor's Exact Sequence

**Theorem (Milnor).** Let $F$ be a field of characteristic not $2$. The tame symbols at the places of $F(t)$ sum to the **ramification map**

$$
\partial = \sum_{p \in P'} \partial_p : k_2(F(t)) \longrightarrow \bigoplus_{p \in P'} k_1(\kappa_p),
$$

the norm maps of the residue field extensions sum to $N : \bigoplus_{p\in P'}k_1(\kappa_p) \to k_1(F)$, the place at infinity contributing the identity of $k_1(F)$, and the sequence

$$
0 \longrightarrow k_2(F) \longrightarrow k_2(F(t)) \xrightarrow{\ \partial\ } \bigoplus_{p \in P'} k_1(\kappa_p) \xrightarrow{\ N\ } k_1(F) \longrightarrow 0
$$

is exact.

The first map is extension of scalars from $F$ to $F(t)$. The theorem is Milnor's, and it is quoted here as standard; it appears in the literature with the two kinds of place of the function field in the middle term, the finite places and the place at infinity.

**Definition.** The **group of ramification sequences** of $F$ is

$$
R_2(F) = \ker N = \operatorname{im}\partial \subseteq \bigoplus_{p \in P'} k_1(\kappa_p),
$$

the equality being exactness of the sequence at the middle term.

Exactness at $k_2(F(t))$ says that a class of $k_2(F(t))$ has trivial ramification sequence exactly when it comes from $k_2(F)$; exactness at the middle term says that the sequences arising are exactly those of norm $1$.

### Ramification Sequences

**Definition.** For a finite set $S \subseteq P'$ its **degree** is $\deg(S) = \sum_{p \in S}[\kappa_p : F]$. For a sequence $\rho = (\rho_p)_{p \in P'}$ the **support** is the finite set

$$
\operatorname{Supp}(\rho) = \{p \in P' : \rho_p \neq 1\},
$$

and the **degree** of $\rho$ is $\deg(\rho) = \deg(\operatorname{Supp}\rho)$. A ramification sequence $\rho \in R_2(F)$ is **represented by a symbol** if there are $f, g \in F(t)^\times$ with $\rho = \partial(\{f,g\})$.

Since the symbols generate $k_2(F(t))$ and $\partial$ is additive, the sequences of symbols generate $R_2(F)$; the question is whether a given sequence is the sequence of one symbol, and it is the question the Bezoutian form answers.

**Remark.** The norm condition of the exact sequence is a genuine restriction, and it fixes the entry at the place at infinity once the finitely many entries at the finite places are given. For a finite place $p$ and a constant $c \in F^\times$ the class of $c$ is the class of the constant in $\kappa_p^\times/\kappa_p^{\times 2}$, whose norm to $F$ is $c^{[\kappa_p : F]}$; so the product of the norms of the finite entries must be trivial in $k_1(F)$, and the entry at infinity is then forced.

**Definition (the sequence of a pair).** Let $g \in F[t]$ be monic and square-free and let $f \in F[t]$ be coprime to $g$. Write $R(f/g)$ for the element of $R_2(F)$ whose entries are

$$
R(f/g)_p = \{f\} \quad \text{for every } p \in P \text{ dividing } g, \qquad R(f/g)_p = 1 \quad \text{for every other finite place } p,
$$

the entry at infinity being the one that the norm condition forces. The definition is the source's, and it is the shape a sequence takes when its support is the set of factors of a square-free polynomial.

## The Bezoutian Form

### The Coefficient Functional $s_g$

**Definition.** Let $g \in F[t]$ be monic of degree $n$ and square-free, and let $\theta$ be the class of $t$ in the $n$-dimensional $F$-algebra $E_g = F[t]/(g)$, so that $1, \theta, \ldots, \theta^{n-1}$ is an $F$-basis of $E_g$. The **coefficient functional** is the $F$-linear map

$$
s_g : E_g \longrightarrow F, \qquad s_g(\theta^i) = 0 \ \ (0 \leq i \leq n-2), \qquad s_g(\theta^{n-1}) = 1,
$$

so that $s_g(y)$ is the coefficient of $\theta^{n-1}$ in the expansion of $y$ in the basis. For $y \in F[t]$ of degree less than $n$ it is the coefficient of $t^{n-1}$. For $n = 1$ and $g = t + c$ the algebra is $F$ and $s_g(y) = y(-c)$.

**Proposition (trace description).** Let $g \in F[t]$ be monic of degree $n$ and square-free, let $\alpha_1, \ldots, \alpha_n$ be its roots in a splitting field, and let $y \in F[t]$. Then

$$
s_g(y \bmod g) = \sum_{i=1}^n \frac{y(\alpha_i)}{g'(\alpha_i)} = \operatorname{Tr}_{E_g/F}\!\left(\frac{y(\theta)}{g'(\theta)}\right),
$$

the last term being the trace of the element $y(\theta)/g'(\theta)$ of $E_g$ over $F$.

**Proof.** Write $y = qg + r$ with $\deg r < n$. Then $s_g(y \bmod g) = s_g(r)$ is the coefficient of $t^{n-1}$ in $r$, and $y(\alpha_i) = r(\alpha_i)$ for every $i$, because $g(\alpha_i) = 0$. The partial fraction decomposition of $r/g$ is

$$
\frac{r(t)}{g(t)} = \sum_{i=1}^n \frac{r(\alpha_i)/g'(\alpha_i)}{t - \alpha_i},
$$

because $g$ is monic and square-free, so that the residues at its simple poles are $r(\alpha_i)/g'(\alpha_i)$. Expanding $\frac{1}{t-\alpha_i} = t^{-1} + \alpha_it^{-2} + \cdots$ at infinity gives

$$
\frac{r(t)}{g(t)} = t^{-1}\left(\sum_{i=1}^n\frac{r(\alpha_i)}{g'(\alpha_i)}\right) + O(t^{-2}),
$$

while $\deg r < n$ and $g$ monic of degree $n$ give $\frac{r(t)}{g(t)} = r_{n-1}t^{-1} + O(t^{-2})$, where $r_{n-1}$ is the coefficient of $t^{n-1}$ in $r$. Comparing the coefficients of $t^{-1}$ gives the first identity, and the second is the definition of the trace of $y(\theta)/g'(\theta)$. $\square$

### The Bezoutian Form of a Pair

**Definition.** Let $g \in F[t]$ be monic of degree $n$ and square-free and let $f \in F[t]$ be coprime to $g$. The **Bezoutian form** of $f$ modulo $g$ is the quadratic form

$$
q_{f,g} : E_g \longrightarrow F, \qquad q_{f,g}(x) = s_g\big(f(\theta)x^2\big),
$$

and its class in the Witt group of *The Witt Group and the Grothendieck–Witt Ring* is written

$$
B(f/g) = [q_{f,g}] \in W(F).
$$

The polar form of $q_{f,g}$ is the bilinear form $b(x,y) = s_g(f(\theta)xy)$, so in the basis $1, \theta, \ldots, \theta^{n-1}$ the Gram matrix is

$$
G = (G_{ij})_{0 \leq i,j \leq n-1}, \qquad G_{ij} = s_g(f\theta^{i+j}), \qquad q_{f,g}\Big(\sum_{i=0}^{n-1}x_i\theta^i\Big) = \sum_{i,j} G_{ij}x_ix_j .
$$

The matrix $G$ is symmetric because $i + j = j + i$, so $q_{f,g}$ is a quadratic form in the sense of *Quadratic Forms and Polarisation*, with $q(x) = B(x,x)$ for its polar form $B$.

**Remark (invariance).** For $g$ monic and square-free and $f$ coprime to $g$ the Bezoutian depends on the pair only through the class of $f$ modulo $g$ and modulo squares: for $h \in F[t]$ coprime to $g$ and $c \in F^\times$ one has

$$
q_{f h^2, g} \cong q_{f,g} \ \text{ via } x \mapsto hx, \qquad q_{cf,g} = c\,q_{f,g}, \qquad q_{f^{-1},g} \cong q_{f,g} \ \text{ via } x \mapsto fx,
$$

on $E_g$. In particular $B(f/g)$ depends on $f$ only through its class in $E_g^\times/E_g^{\times 2}$, and the element $R(f/g)$ of the definition above is therefore attached to the pair in a way compatible with the form.

**Theorem (non-degeneracy).** Let $g \in F[t]$ be monic and square-free and $f \in F[t]$ coprime to $g$. Then the Bezoutian form $q_{f,g}$ is non-degenerate. It is degenerate for every $f$ sharing a factor with $g$.

**Proof for $n = 1$.** Here $g = t + c$ and $\theta = -c$, so $E_g = F$, $s_g$ is the identity of $F$, and $q_{f,g}(x) = f(-c)x^2$. This is non-degenerate exactly when $f(-c) \neq 0$, that is, exactly when $t + c$ does not divide $f$. The general case is the theorem of Becher and Raczek, and is quoted. $\square$

The non-degeneracy is the reason the Bezoutian is taken over the square-free $g$ and the coprime $f$: the form is then a genuine element of the Witt group, and its triviality is a meaningful condition.

**Remark (the classical Bezoutian).** The name of the form is that of the classical **Bezoutian** of the pair, the polynomial

$$
\operatorname{Bez}(f,g)(x,y) = \frac{f(x)g(y) - f(y)g(x)}{x-y},
$$

whose coefficient matrix $\mathcal{B}(f,g)$ is symmetric, whose determinant is $\pm\operatorname{Res}(f,g)$, and which is non-degenerate exactly when $\gcd(f,g) = 1$. The form $q_{f,g}$ above is the normalisation of Becher and Raczek, and it is a different quadratic form from the one of the classical matrix in general: for $f = t - 2$ and $g = t^2 - 2t - 2$ the classical form is negative definite, while $q_{f,g}$ is positive definite. The classical Bezoutian and its determinant are treated in the further reading below.

### The Computation Rules

The Bezoutian is computable without diagonalising a matrix, by two rules which decompose the modulus and exchange the numerator with the modulus; the rules are those of Becher and Raczek, and they are quoted.

**Proposition (first rule).** Let $f, g_1, g_2 \in F[t]$ be pairwise coprime, with $g_1$ and $g_2$ monic and square-free. Then in $W(F)$

$$
B\!\left(\frac{f}{g_1g_2}\right) = B\!\left(\frac{fg_2}{g_1}\right) + B\!\left(\frac{fg_1}{g_2}\right).
$$

The form on the left lives on $E_{g_1g_2}$, of dimension $\deg g_1 + \deg g_2$, and the two forms on the right live on $E_{g_1}$ and $E_{g_2}$; the two sides have the same dimension, so the equality of Witt classes is an isometry of quadratic forms.

**Theorem (second rule).** Let $f, g \in F[t]$ be monic, square-free and coprime. Then

$$
B\!\left(\frac{f}{g}\right) + B\!\left(\frac{g}{f}\right) = \begin{cases} 0 & \text{if } \deg f \equiv \deg g \bmod 2, \\[2pt] [1] & \text{if } \deg f \not\equiv \deg g \bmod 2, \end{cases}
$$

where $[1]$ is the class of the one-dimensional form $\langle 1\rangle$.

**The second rule in a special case.** Take $f = t$ and $g = t^2 - 1$. Here $E_g = F[t]/(t^2-1)$ with $\theta^2 = 1$, and $q_{t,g}(x) = s_g(\theta x^2)$ has Gram matrix

$$
G_{ij} = s_g(\theta^{i+j+1}), \qquad G = \begin{pmatrix} s_g(\theta) & s_g(\theta^2) \\ s_g(\theta^2) & s_g(\theta^3)\end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix},
$$

because $s_g(1) = s_g(\theta^3) = 0$ and $s_g(\theta) = 1$; so $q_{t,g} = \langle 1,1\rangle$. On the other side $E_t = F[t]/(t) = F$, so $q_{g,t}(x) = s_t((\theta^2 - 1)x^2) = s_t(-x^2)$ is the form $\langle -1\rangle$. The sum is $[\langle 1,1,-1\rangle] = [\langle 1\rangle]$ in $W(F)$, because $\langle 1,-1\rangle$ is the hyperbolic plane, in agreement with the rule, the degrees $1$ and $2$ having opposite parity.

### A Lemma on Even Degrees

The following computation is the one used in the example; it expresses the Bezoutian of a pair whose modulus is a product of two even-degree factors through a Pfister form.

**Lemma (Becher).** Let $a_1, a_2 \in F^\times$ and let $g_1, g_2 \in F[t]$ be monic of even degree, coprime, and such that $g_1t$ is a square modulo $g_2$. Let $f \in F[t]$ be such that $a_if$ is a square modulo $g_i$ for $i = 1, 2$. Then

$$
B\!\left(\frac{f}{g_1g_2}\right) \sim \big[\langle\!\langle a_1a_2, g_2(0)\rangle\!\rangle\big],
$$

where $\sim$ means equality up to a scalar: $\alpha \sim \alpha'$ if and only if $\alpha' = c\,\alpha$ in $W(F)$ for some $c \in F^\times$.

**Proof.** Write $b = g_2(0)$. By the second rule applied to the monic coprime pair $t, g_2$, whose degrees have opposite parity, and the elementary descriptions $B(g_2/t) = [b]$ and $B(t/g_2) = [1] - [b]$,

$$
B\!\left(\frac{t}{g_2}\right) = [1] - B\!\left(\frac{g_2}{t}\right) = [1] - [b].
$$

Because $g_1t$ is a square modulo $g_2$, the invariance of $q_{f,g}$ under multiplication of $f$ by a square and under inversion gives $B(g_1/g_2) = B(t/g_2)$, so $B(g_1/g_2) = [1]-[b]$; and the second rule applied to the pair $g_1, g_2$, whose degrees have the same parity, gives $B(g_2/g_1) = -B(g_1/g_2) = [b]-[1]$. Since $a_if$ is a square modulo $g_i$, the form $B(fg_j/g_i)$ differs from $a_iB(g_j/g_i)$ by a scalar, so the first rule gives

$$
B\!\left(\frac{f}{g_1g_2}\right) = B\!\left(\frac{fg_2}{g_1}\right) + B\!\left(\frac{fg_1}{g_2}\right) \sim a_1\big([b]-[1]\big) + a_2\big([1]-[b]\big).
$$

As forms, the last sum is $\langle a_1b, -a_1, a_2, -a_2b\rangle$, whose multiset of square classes is $\{a_1b,\,-a_1,\,a_2,\,-a_2b\}$. The Pfister form has

$$
a_2\langle\!\langle a_1a_2, b\rangle\!\rangle = \langle a_2, -a_1a_2^2, -a_2b, a_1a_2^2b\rangle \cong \langle a_2, -a_1, -a_2b, a_1b\rangle,
$$

the two entries $-a_1a_2^2$ and $a_1a_2^2b$ being the square multiples $-a_1$ and $a_1b$ of the corresponding entries, and the multiset of square classes is the same one. Hence the two forms are isometric up to the scalar, as claimed. $\square$

## The Criterion of Becher and Raczek

**Theorem (the criterion).** Let $g \in F[t]$ be monic and square-free and let $f \in F[t]$ be coprime to $g$, and let $R(f/g) \in R_2(F)$ be the sequence of the pair. Then $R(f/g)$ is represented by a symbol if and only if

$$
B(f/g) = 0 \quad \text{in } W(F).
$$

The two implications are the lemma and the theorem of Becher and Raczek, quoted as standard: a symbol whose ramification is the sequence of a pair has trivial Bezoutian, and a pair whose Bezoutian is trivial has its sequence represented by a symbol.

**Proposition (the concrete form).** Let $a_1, a_2 \in F^\times$ and let $g_1, g_2 \in F[t]$ be monic of even degree and coprime, with $g_1t$ a square modulo $g_2$. Assume that the quadratic form $\langle 1, -a_1a_2\rangle$ over $F(t)$ does not represent $g_2(0)$, and that $a_i$ is a non-square in $\kappa_p$ for every irreducible factor $p$ of $g_i$. Then

$$
\partial\big(\{g_1, a_1\} + \{g_2, a_2\}\big) \neq \partial(\sigma) \qquad \text{for every symbol } \sigma \in k_2(F(t)).
$$

**Proof.** Write $\rho = \partial(\{g_1,a_1\}+\{g_2,a_2\}) \in R_2(F)$. The hypotheses on the $a_i$ give $\operatorname{Supp}(\rho) = \{p \in P : p \text{ divides } g_1g_2\}$ and $\deg(\rho) = \deg g_1 + \deg g_2$. If a symbol $\sigma$ had $\partial(\sigma) = \rho$, then by the structure of the sequences of symbols there would be polynomials $f, h$ and a square-free $g$, pairwise coprime, with $g = g_1g_2$, such that $\sigma = \{f, gh\}$ and $\partial(\sigma) = R(f/g)$; the criterion would give $B(f/g) = 0$. Moreover $R(f/g_1) + R(f/g_2) = R(f/g) = \partial(\sigma) = \rho = R(a_1/g_1) + R(a_2/g_2)$, because the support of $R(f/g)$ splits into the places dividing $g_1$ and those dividing $g_2$; comparing the entries at the places dividing $g_i$ gives $R(f/g_i) = R(a_i/g_i)$, that is, $a_if$ is a square modulo $g_i$. The lemma then gives $B(f/g) \sim [\langle\!\langle a_1a_2, g_2(0)\rangle\!\rangle]$, so $a_2\langle\!\langle a_1a_2, g_2(0)\rangle\!\rangle$ is hyperbolic and the form $\langle 1, -a_1a_2\rangle$ represents $g_2(0)$, against the hypothesis. $\square$

## The Example over $\mathbb{Q}$

Take $F = \mathbb{Q}$, $a = 2$, $b = 3$, and

$$
g_1 = t^2+3t+2 = (t+1)(t+2), \qquad g_2 = t^2+2t+2 = (t+1)^2+1,
$$

so that $g_2$ is irreducible with $g_2(0) = a = 2$ and residue field $F_{g_2} = \mathbb{Q}(i)$, and $g_1, g_2$ are monic of degree $2$, coprime and square-free. The hypotheses of the proposition hold: $a_1 = a = 2$ is a non-square modulo each of the factors $t+1$ and $t+2$ of $g_1$, whose residue field is $\mathbb{Q}$, and $a_2 = ab = 6$ is a non-square in $\mathbb{Q}(i)$; and the form $\langle 1,-a_1a_2\rangle = \langle 1, -12\rangle$ does not represent $g_2(0) = 2$, because the quaternion algebra $(12,2)_{\mathbb{Q}} = (3,2)_{\mathbb{Q}}$ is non-split, having Hilbert symbol $-1$ at $2$ and at $3$. The same holds over $\mathbb{Q}(t)$, the map $\operatorname{Br}(\mathbb{Q}) \to \operatorname{Br}(\mathbb{Q}(t))$ being injective.

The class

$$
\xi = \{g_1, a\} + \{g_2, ab\} = \{g_1,2\} + \{g_2,6\} \in k_2(\mathbb{Q}(t))
$$

has the ramification sequence

$$
\rho_{t+1} = \{2\}, \qquad \rho_{t+2} = \{2\}, \qquad \rho_{g_2} = \{6\}, \qquad \operatorname{Supp}\rho = \{t+1, t+2, g_2\},
$$

of degree $1 + 1 + 2 = 4$, and the entry at infinity is $1$: the sum of the norms of the finite entries is $2 \cdot 2 \cdot N_{\mathbb{Q}(i)/\mathbb{Q}}(6) = 2 \cdot 2 \cdot 6^2 = 144$, a square of $\mathbb{Q}$, hence trivial in $k_1(\mathbb{Q})$, so the norm condition forces $\rho_\infty = 1$ and $\rho \in R_2(\mathbb{Q})$ is a genuine ramification sequence of degree $4$.

If $\rho$ were represented by a symbol, the pair would be $(f, g_1g_2)$ for some $f$ with $a_if$ a square modulo $g_i$, by the argument of the proposition. The canonical representative is the solution of the congruences $f \equiv 2 \pmod{g_1}$, $f \equiv 6 \pmod{g_2}$ by an element of degree less than $4$, namely

$$
f = -2t^3-10t^2-16t-6 .
$$

Indeed $2f \equiv 4$ modulo $g_1$ and $6f \equiv 36$ modulo $g_2$ are squares, so the pair satisfies the hypotheses of the lemma with $a_1 = 2$, $a_2 = 6$ and $b = g_2(0) = 2$.

The Bezoutian form $q_{f,g_1g_2}$ on $\mathbb{Q}[t]/(g_1g_2)$ has dimension $4$, and in the basis $1, \theta, \theta^2, \theta^3$ its Gram matrix $G_{ij} = s_g(f\theta^{i+j})$ is

$$
G = \begin{pmatrix}
-2 & 0 & 4 & -6\\
0 & 4 & -6 & -2\\
4 & -6 & -2 & 30\\
-6 & -2 & 30 & -86
\end{pmatrix},
$$

symmetric, of determinant $144$ and signature $(2,2)$. Its Lagrange diagonalisation over $\mathbb{Q}$ is

$$
q_{f,g_1g_2} \cong \langle -2, 4, -3, 6\rangle \cong 6\,\langle 1,-2,-3,6\rangle = 6\,\langle\!\langle 2,3\rangle\!\rangle,
$$

so the Bezoutian is a scalar multiple of the Pfister form $\langle\!\langle a_1a_2, g_2(0)\rangle\!\rangle = \langle\!\langle 12, 2\rangle\!\rangle = \langle\!\langle 2,3\rangle\!\rangle$ of the lemma, as it must be. That Pfister form is the norm form of the quaternion algebra $(2,3)_{\mathbb{Q}}$, and that algebra is a division algebra, so the form is anisotropic; hence the Bezoutian form is anisotropic, in particular not hyperbolic, and $B(f/g_1g_2) \neq 0$ in $W(\mathbb{Q})$. By the criterion, the sequence $\rho$ is not represented by a symbol.

## The Biquaternion Division Algebras

The same computation, over a general field, gives the biquaternion division algebras over $F(t)$ of *Division Algebras*. With $g_1 = t^2+(a+1)t+a$ and $g_2 = t^2+at+a$ the class $\{g_1,a\}+\{g_2,ab\}$ corresponds, under the dictionary between $k_2$ and the two-torsion of the Brauer group of *Central Simple Algebras and the Brauer Group*, to the biquaternion algebra

$$
B = (g_1, a)_{F(t)} \otimes_{F(t)} (g_2, ab)_{F(t)},
$$

and the ramification of $B$ differs from the ramification of every quaternion algebra over $F(t)$ exactly when the sequence is not represented by a symbol. Becher's theorem states the equivalence.

**Theorem (Becher).** Let $a, b \in F^\times$ with $a \notin F^{\times 2}$ and $b \notin aF^{\times 2} \cup (a-4)F^{\times 2}$. Then the following are equivalent:

1. $\{a,b\} = 0$ in $k_2(F)$, that is, the quaternion algebra $(a,b)_F$ is split;
2. $\partial(\{g_1,a\}+\{g_2,ab\}) = \partial(\sigma)$ for some symbol $\sigma \in k_2(F(t))$, where $g_1 = t^2+(a+1)t+a$ and $g_2 = t^2+at+a$.

In particular, if $(a,b)_F$ is not split, then the ramification of $B$ is not the ramification of any quaternion algebra over $F(t)$, a situation the source records by saying that $B$ has Faddeev index $4$; then $B$ is a division algebra over $F(t)$ that contains no quaternion algebra defined over $F$.

**Theorem (Becher, existence over a general field).** Assume that $k_2(F) \neq 0$ and that $F$ is not real euclidean, the set of squares of $F$ not being an ordering. Then there is a field element $a$ and a $b$ as above such that the ramification sequence $\rho = \partial(\{g_1,a\}+\{g_2,ab\})$ of degree $4$ is not represented by a symbol, and the algebra $B$ above is a division algebra that does not contain any quaternion algebra defined over $F$.

The example of this article is the case $F = \mathbb{Q}$, $a = 2$, $b = 3$ of the two theorems.

## Summary

Let $F$ be a field of characteristic not $2$. The places of the rational function field $F(t)$ are the monic irreducible polynomials $p \in F[t]$, with residue field $\kappa_p = F[t]/(p)$, and the place at infinity, with residue field $F$. The tame symbol at a place is the homomorphism $\partial_p(\{f,g\}) = (-1)^{v(f)v(g)}u_f^{-v(g)}u_g^{v(f)}$ into $k_1(\kappa_p) = \kappa_p^\times/\kappa_p^{\times 2}$, and by **Milnor's exact sequence**

$$
0 \to k_2(F) \to k_2(F(t)) \xrightarrow{\ \partial\ } \bigoplus_{p \in P'} k_1(\kappa_p) \xrightarrow{\ N\ } k_1(F) \to 0
$$

the ramification map is injective on $k_2(F)$ and its image is the **group of ramification sequences** $R_2(F)$, the kernel of the norm. The support and the degree of a sequence measure the places carrying it, and a sequence is **represented by a symbol** when it is $\partial(\{f,g\})$ for a single symbol.

The **Bezoutian form** of $f$ modulo a monic square-free $g$ is the form $q_{f,g}(x) = s_g(f(\theta)x^2)$ on $E_g = F[t]/(g)$, where $s_g$ is the coefficient of $\theta^{n-1}$ in the basis $1,\theta,\ldots,\theta^{n-1}$; equivalently $s_g(y\bmod g) = \operatorname{Tr}_{E_g/F}(y(\theta)/g'(\theta))$. It is non-degenerate exactly when $f$ is coprime to $g$, and its class $B(f/g)$ in the Witt group is computed by the two rules

$$
B\!\left(\frac{f}{g_1g_2}\right) = B\!\left(\frac{fg_2}{g_1}\right) + B\!\left(\frac{fg_1}{g_2}\right), \qquad
B\!\left(\frac{f}{g}\right) + B\!\left(\frac{g}{f}\right) = 0 \ \text{or}\ [1],
$$

the second value occurring when the degrees of $f$ and $g$ have opposite parity. For monic $g_1, g_2$ of even degree with $g_1t$ a square modulo $g_2$ and $a_if$ a square modulo $g_i$, $B(f/g_1g_2)$ is a scalar multiple of the Pfister form $\langle\!\langle a_1a_2, g_2(0)\rangle\!\rangle$. The criterion of Becher and Raczek reads the representability of the sequence $R(f/g)$ by a symbol from the vanishing of $B(f/g)$, and the concrete form of the criterion is the proposition above: under its hypotheses no symbol has the same ramification as $\{g_1,a_1\}+\{g_2,a_2\}$.

Over $\mathbb{Q}$ the class $\{g_1,2\}+\{g_2,6\}$ with $g_1 = (t+1)(t+2)$ and $g_2 = t^2+2t+2$ has a ramification sequence of degree $4$ with entries $2$, $2$, $6$ and norm $144$, and the Bezoutian form of the pair with $f = -2t^3-10t^2-16t-6$ has determinant $144$, signature $(2,2)$ and diagonalisation $\langle -2,4,-3,6\rangle \cong 6\langle\!\langle 2,3\rangle\!\rangle$. The Pfister form is the norm form of the division algebra $(2,3)_{\mathbb{Q}}$, so it is anisotropic and the sequence is not represented by a symbol. The corresponding biquaternion algebra over $\mathbb{Q}(t)$ is a division algebra that contains no quaternion algebra defined over $\mathbb{Q}$, and Becher's theorems give the same conclusion over every field that is not real euclidean and has a non-split quaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $F(t)$ | Field of characteristic not $2$; its rational function field |
| $P$, $P'$ | Monic irreducible polynomials of $F[t]$; the places $P \cup \{\infty\}$ |
| $v_p$, $v_\infty$ | Valuation of a finite place; valuation $-\deg$ of the place at infinity |
| $\kappa_p$, $F_p$ | Residue field of the place $p$; for $p \in P$ it is $F[t]/(p)$ |
| $[\kappa_p : F]$ | Degree of a place |
| $k_2$, $k_1$ | Milnor groups modulo $2$ of *Higher Algebraic K-Theory* |
| $\partial_p$, $\partial$ | Tame symbol at $p$; the ramification map, the sum of the tame symbols |
| $N$ | Sum of the norm maps of the residue extensions |
| $R_2(F)$ | Group of ramification sequences, $\ker N = \operatorname{im}\partial$ |
| $\operatorname{Supp}\rho$, $\deg\rho$ | Support and degree of a ramification sequence |
| $R(f/g)$ | The sequence with entry $\{f\}$ at each divisor of $g$ and $1$ elsewhere |
| $E_g = F[t]/(g)$ | The $F$-algebra of a monic square-free $g$, of degree $n$ |
| $\theta$ | The class of $t$ in $E_g$ |
| $s_g$ | Coefficient functional of $\theta^{n-1}$; $\operatorname{Tr}_{E_g/F}(\cdot/g'(\theta))$ |
| $q_{f,g}$, $B(f/g)$ | Bezoutian form of $f$ modulo $g$; its class in $W(F)$ |
| $G_{ij} = s_g(f\theta^{i+j})$ | Gram matrix of the Bezoutian form |
| $\langle\!\langle a,b\rangle\!\rangle$ | Pfister form $\langle 1,-a,-b,ab\rangle$ |
| $\sim$ | Equality of Witt classes up to a scalar |
| $\operatorname{Bez}(f,g)$, $\mathcal{B}(f,g)$ | Classical Bezoutian and its coefficient matrix |
| $g_1$, $g_2$ | The polynomials $t^2+(a+1)t+a$ and $t^2+at+a$ of the application |

## Further Reading

- John Milnor, *Algebraic K-Theory and Quadratic Forms* (Inventiones Mathematicae 9, 1970, 318–344), for the tame symbol and the exact sequence for a rational function field.
- Philippe Gille and Tamás Szamuely, *Central Simple Algebras and Galois Cohomology* (Cambridge University Press, 2006), for the exact sequence in the form quoted here and for the dictionary between $k_2$ and the two-torsion of the Brauer group.
- Karim Johannes Becher and Rafał Raczek, *Ramification Sequences and Bezoutian Forms* (Journal of Algebra 476, 2017, 26–47), for the Bezoutian form, its non-degeneracy, the computation rules and the criterion.
- Karim Johannes Becher, *Biquaternion Division Algebras over Rational Function Fields* (Journal of Pure and Applied Algebra 223, 2019, 2911–2919), for the two theorems of the application and the Faddeev index.
- Uwe Helmke and Paul A. Fuhrmann, *Bezoutians* (Linear Algebra and its Applications 122–124, 1989, 1039–1097), for the classical Bezoutian, its symmetry, its determinant and the resultant.
- Richard Elman, Nikita Karpenko and Alexander Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms* (American Mathematical Society Colloquium Publications 56, 2008), for the classification of forms over $\mathbb{Q}$ by dimension, discriminant, signature and Hasse invariant used in the example.
